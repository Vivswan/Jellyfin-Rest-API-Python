import copy
import json
import os
import re
from pathlib import Path

import requests


def to_snake_case(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()


def save_openapi_json(url, openapi_json_path):
    content = requests.get(url).text
    with open(openapi_json_path, "w") as file:
        file.write(content)


def json_type_to_python_str(json_type):
    if json_type == 'string':
        responses = 'str'
    elif json_type == 'number':
        responses = 'float'
    elif json_type == 'integer':
        responses = 'int'
    elif json_type == 'boolean':
        responses = 'bool'
    elif json_type == 'null':
        responses = 'None'
    elif json_type == 'array':
        responses = 'List'
    else:
        responses = 'object'
    return responses


def create_tree(openapi_json_path):
    dict_tree = {}
    with open(openapi_json_path, "r") as file:
        openapi = json.loads(file.read())

    paths = openapi["paths"]
    for path_name in paths:
        path_body = paths[path_name]
        section = path_name.split("/")[1]

        if section not in dict_tree:
            dict_tree[section] = {}

        if path_name not in dict_tree[section]:
            dict_tree[section][path_name] = copy.deepcopy(path_body)

    return dict_tree


def json_schema_to_python_function(location, schema):
    function_name = schema["operationId"]
    parameters = {}
    optional_parameters = []
    required_parameters = []
    default_parameters = []
    nullable_parameters = []
    non_required_parameters = []
    ref_parameter = []
    responses = None

    imports_list = set()

    if "parameters" in schema:
        for parameter in schema["parameters"]:
            name = to_snake_case(parameter["name"])
            parameters[name] = copy.deepcopy(parameter["schema"])
            parameters[name]['original_name'] = parameter["name"]

            if parameter["in"] == "query":
                if "description" in parameter and "optional" in parameter["description"].lower():
                    optional_parameters.append(name)
                if "nullable" in parameter["schema"] and parameter["schema"]["nullable"]:
                    nullable_parameters.append(name)
            if "default" in parameter["schema"]:
                default_parameters.append(name)
            if name not in optional_parameters + nullable_parameters + default_parameters:
                required_parameters.append(name)
            else:
                non_required_parameters.append(name)
    if "requestBody" in schema:
        if "application/json" in schema["requestBody"]['content']:
            request_body_schema = schema["requestBody"]['content']["application/json"]["schema"]
            name = to_snake_case("request_body")
            parameters[name] = copy.deepcopy(request_body_schema)
            parameters[name]['original_name'] = "requestBody"
            if "nullable" in request_body_schema:
                nullable_parameters.append(name)
            if 'required' in schema["requestBody"] and name not in nullable_parameters:
                required_parameters.append(name)
            else:
                non_required_parameters.append(name)
        elif "image/*" in schema["requestBody"]['content']:
            pass
            # TODO
            # print(schema["requestBody"])
        else:
            raise NotImplemented
    if "responses" in schema:
        if '200' in schema["responses"]:
            responses = "python_response"
            status = schema["responses"]['200']
            if 'content' in status:
                if 'application/json' in status['content']:
                    json_response = status['content']['application/json']['schema']
                    if "$ref" in json.dumps(json_response):
                        if 'type' in json_response:
                            ref = json_response['items']['$ref'].split('/')[-1]
                            responses = "List[" + ref + "]"
                            imports_list.add("from typing import List")
                            imports_list.add(f"#{ref}")
                        else:
                            responses = json_response['$ref'].split('/')[-1]
                            imports_list.add(f"#{responses}")
                    else:
                        responses = json_type_to_python_str(json_response['type'])
                        if responses == 'List':
                            responses = "List[" + json_type_to_python_str(json_response['items']['type']) + "]"
                            imports_list.add("from typing import List")
        elif '204' in schema["responses"]:
            responses = None
        else:
            raise NotImplemented

    content = ""
    # content += " " * 4 + f"#          parameters={list(parameters.keys())}\n"
    # content += " " * 4 + f"# required_parameters={required_parameters}\n"
    # content += " " * 4 + f"# nullable_parameters={nullable_parameters}\n"
    arg_text = ""
    for parameter_name in required_parameters + non_required_parameters:
        parameter = parameters[parameter_name]
        if "description" in parameter:
            content += " " * 4 + f"# {to_snake_case(parameter_name)}: {parameter['description']}\n"

        if '$ref' in json.dumps(parameter):
            is_array = False
            ref = None
            if 'type' in parameter:
                if parameter['type'] == "array":
                    is_array = True
                else:
                    raise NotImplemented
                if 'items' in parameter and '$ref' in parameter['items']:
                    ref = parameter['items']['$ref']
            else:
                if 'allOf' in parameter and len(parameter['allOf']) == 1 and '$ref' in parameter['allOf'][0]:
                    ref = parameter['allOf'][0]['$ref']
            if ref is not None:
                python_type = ref.split('/')[-1]
                imports_list.add("#" + python_type)
                ref_parameter.append(parameter_name)
            else:
                python_type = 'object'

            if is_array:
                python_type = f"List[{python_type}]"
                imports_list.add("from typing import List")

            if parameter_name in required_parameters:
                arg_text += f", {to_snake_case(parameter_name)}: {python_type}"
            else:
                arg_text += f", {to_snake_case(parameter_name)}: Optional[{python_type}] = None"
                imports_list.add("from typing import Optional")
        elif 'type' in parameter:
            python_type = json_type_to_python_str(parameter['type'])
            if python_type == "List" and 'items' in parameter and 'type' in parameter['items']:
                python_type += "[" + json_type_to_python_str(parameter['items']['type']) + "]"

            if parameter_name in required_parameters:
                arg_text += f", {to_snake_case(parameter_name)}: {python_type}"
            else:
                arg_text += f", {to_snake_case(parameter_name)}: Optional[{python_type}]"
                imports_list.add("from typing import Optional")
                if parameter_name in default_parameters:
                    arg_text += f" = {parameter['default']}"
                else:
                    arg_text += f" = None"
        else:
            raise NotImplemented

        # print(parameter)
    responses_type = 'Any'
    if responses is not None:
        if responses == "python_response":
            imports_list.add("from requests import Response")
            responses_type = "Response"
        else:
            responses_type = responses

    content += " " * 4 + f"def {to_snake_case(function_name)}(self{arg_text}) -> {responses_type}:\n"
    content += " " * 8 + f"url_path = '{location}'\n"
    content += " " * 8 + f"responses_type = {responses_type}\n"
    content += " " * 8 + "request_args = {}\n"
    for parameter_name in required_parameters + non_required_parameters:
        if parameter_name == 'request_body':
            continue
        original_name = parameters[parameter_name]['original_name']
        indent = 8
        if parameter_name in non_required_parameters:
            content += " " * indent + f"if {parameter_name} is not None:\n"
            indent += 4

        content += " " * indent + f"request_args['{original_name}'] = query_class_arg_to_json({parameter_name})\n"

    content += " " * 8 + f"url_path, request_args = parse_url_for_query_classes(url_path, request_args)\n"
    imports_list.add("from util.query_classes_helper import *")

    if 'request_body' in parameters:
        pass

    return content, list(imports_list)


# Request body: No
# Response body: Yes
# Safe: Yes
def create_get_function(location, schema):
    class_py, imports_list = json_schema_to_python_function(location, schema)
    return class_py, imports_list


# Request body: Yes
# Response body: Yes
# Safe: Yes
def create_post_function(location, schema):
    class_py, imports_list = json_schema_to_python_function(location, schema)
    return class_py, imports_list


# Request body: May
# Response body: May
# Safe: Yes
def create_delete_function(location, schema):
    class_py, imports_list = json_schema_to_python_function(location, schema)
    return class_py, imports_list


# Request body: No
# Response body: No
# Safe: Yes
def create_head_function(location, schema):
    class_py, imports_list = json_schema_to_python_function(location, schema)
    return class_py, imports_list


def create_py_classes(query_tree):
    all_classes_dict = {}
    for section in query_tree:
        content = ""
        import_list = set()
        content += f"class {section}:\n"
        if section.startswith("%"):
            continue
        for path_name in query_tree[section]:
            path_body = query_tree[section][path_name]
            for http_request_method in path_body:
                if 'deprecated' in path_body[http_request_method]:
                    continue
                if http_request_method.lower() == "get":
                    add_content, add_imports = create_get_function(path_name, path_body[http_request_method])
                elif http_request_method.lower() == "post":
                    add_content, add_imports = create_post_function(path_name, path_body[http_request_method])
                elif http_request_method.lower() == "delete":
                    add_content, add_imports = create_delete_function(path_name, path_body[http_request_method])
                elif http_request_method.lower() == "head":
                    add_content, add_imports = create_head_function(path_name, path_body[http_request_method])
                else:
                    add_content = f"# NotImplemented: {path_body}"
                    print(add_content)
                    add_imports = []

                content += f"{add_content}\n"
                for i in add_imports:
                    import_list.add(i)

        all_classes_dict[section] = {
            'imports': import_list,
            'content': content,
        }
    return all_classes_dict


def parse_import_list(classes_dict, data_classes_path):
    class_content = {}
    connections = {}
    for filename in os.listdir(data_classes_path):
        if '.py' not in filename:
            continue
        if filename == "_all.py":
            continue
        with open(data_classes_path.joinpath(filename), "r") as file:
            for line in file.readlines():
                if line.startswith("class"):
                    class_name = line.replace("class", "").replace(":", "").strip()
                    if "(" in class_name:
                        class_name = class_name[:class_name.find("(")]
                    class_path = data_classes_path.parent.name + "." + data_classes_path.name + "." + filename.replace(
                        ".py", "")
                    connections[class_name] = f"from {class_path} import {class_name}"
                    break

    for name in classes_dict:
        if name in class_content:
            raise Exception("What?")
        class_content[name] = ""

        for i in classes_dict[name]["imports"]:
            if i.startswith("#"):
                class_name = i[1:]
                import_line = connections[class_name]
            else:
                import_line = i
            class_content[name] += f"{import_line}\n"

    # print(class_content)
    return class_content


def main(url, location, data_classes):
    path = Path(__file__)
    query_path = path.parent.joinpath(location)
    json_schema_path = query_path.joinpath("json")
    classes_path = query_path.joinpath("classes")
    data_classes_path = path.parent.joinpath(data_classes).joinpath("classes")
    openapi_json_path = json_schema_path.joinpath("_openapi.json")

    # if os.path.exists(query_path):
    #     shutil.rmtree(query_path)
    #
    # os.mkdir(query_path)
    # os.mkdir(json_schema_path)
    # os.mkdir(classes_path)

    # save_openapi_json(url, openapi_json_path)
    query_tree = create_tree(openapi_json_path)
    all_classes_dict = create_py_classes(query_tree)
    all_classes_content = parse_import_list(all_classes_dict, data_classes_path)

    open(query_path.joinpath("__init__.py"), "w").close()
    open(classes_path.joinpath("__init__.py"), "w").close()


if __name__ == '__main__':
    main("http://localhost:8096/api-docs/openapi.json", "query_classes", "data_classes")
