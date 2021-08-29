import copy
import json
import os
import re
import shutil
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

    return openapi["info"]["title"], dict_tree


def json_schema_to_python_function(location: str, schema: object, http_request_method: str):
    function_name = schema["operationId"]
    parameters = {}
    optional_parameters = []
    required_parameters = []
    default_parameters = []
    nullable_parameters = []
    non_required_parameters = []
    ref_parameter = []
    responses = "requests.Response"

    imports_list = set()

    if function_name.lower() in ["get", "post", "delete", "head"]:
        function_name += location.split("/")[-1]

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
            name = to_snake_case("requestBody")
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
            pass
        else:
            raise NotImplemented

    content = ""
    # content += " " * 4 + f"#          parameters={list(parameters.keys())}\n"
    # content += " " * 4 + f"# required_parameters={required_parameters}\n"
    # content += " " * 4 + f"# nullable_parameters={nullable_parameters}\n"
    args_type_dict = {}
    for parameter_name in required_parameters + non_required_parameters:
        parameter = parameters[parameter_name]
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
                args_type_dict[parameter_name] = python_type
            else:
                args_type_dict[parameter_name] = f"Optional[{python_type}] = None"
                imports_list.add("from typing import Optional")
        elif 'type' in parameter:
            python_type = json_type_to_python_str(parameter['type'])
            if python_type == "List" and 'items' in parameter and 'type' in parameter['items']:
                python_type += "[" + json_type_to_python_str(parameter['items']['type']) + "]"
                imports_list.add("from typing import List")

            if parameter_name in required_parameters:
                args_type_dict[parameter_name] = python_type
            else:
                args_type_dict[parameter_name] = f"Optional[{python_type}]"
                imports_list.add("from typing import Optional")
                if parameter_name in default_parameters:
                    args_type_dict[parameter_name] += f" = {parameter['default']}"
                else:
                    args_type_dict[parameter_name] += f" = None"
        else:
            raise NotImplemented

        # print(parameter)

    arg_text = "self"
    for parameter_name in required_parameters + non_required_parameters:
        arg_text += f", \n" + (" " * 12) + f"{parameter_name}: {args_type_dict[parameter_name]}"
    content += " " * 4 + f"def {to_snake_case(function_name)}(\n" + (" " * 12) + f"{arg_text}\n" + (" " * 4) + f") -> {responses}:\n"

    content += " " * 8 + "\"\"\""
    if "summary" in schema:
        content += schema["summary"] + "\n"
    content += "\n"
    content += " " * 8 + "Http:\n"
    content += " " * 12 + f"<{http_request_method}>: {location}\n"

    if len(parameters.keys()) > 0:
        content += "\n"
        content += " " * 8 + "Args:"
        for parameter_name in required_parameters + non_required_parameters:
            parameter = parameters[parameter_name]
            parameter_split = args_type_dict[parameter_name].split('=')
            content += "\n" + " " * 12 + f"{to_snake_case(parameter_name)} "
            if "Optional" in parameter_split[0].strip():
                content += f"({parameter_split[0].replace('Optional[', '').strip()[:-1]}"
            else:
                content += f"({parameter_split[0].strip()}"
            if len(parameter_split) > 1 and parameter_split[1].strip() != "None":
                content += f" = {parameter_split[1].strip()}"
            content += f")"

            if "description" in parameter:
                content += f": {parameter['description']}"
        content += "\n"

    if "responses" in schema:
        content += "\n"
        content += " " * 8 + "Returns:\n"
        for status_code in schema["responses"]:
            status = schema["responses"][status_code]
            content += " " * 12 + f"<{status_code}> "
            if status_code[0] == '2':
                content += f"{responses}"
            else:
                content += "requests.Response"

            if 'description' in status:
                content += f": {status['description']}"
            content += "\n"
    content += " " * 8 + "\"\"\"\n"

    if len(required_parameters + non_required_parameters) > 0:
        content += " " * 8 + "request_args = dict(\n"
        for parameter_name in required_parameters + non_required_parameters:
            original_name = parameters[parameter_name]['original_name']
            content += " " * 12 + f"{original_name}={parameter_name},\n"
        content += " " * 8 + ")\n"

    content += " " * 8 + f"return self._{http_request_method}(path='{location}'"
    if len(required_parameters + non_required_parameters) > 0:
        content += f", request_args=request_args"
    if responses != "requests.Response":
        content += f", response_type={responses}"

    if responses == "requests.Response":
        imports_list.add("import requests")

    content += ")\n"
    return content, list(imports_list)


def create_py_classes(query_tree):
    all_classes_dict = {}
    for section in query_tree:
        content = ""
        import_list = set()
        content += f"class {section}(BaseRequestClass):\n"
        import_list.add("from util.BaseRequestClass import BaseRequestClass")
        if section.startswith("%"):
            continue
        for path_name in query_tree[section]:
            path_body = query_tree[section][path_name]
            for http_request_method in path_body:
                if 'deprecated' in path_body[http_request_method]:
                    continue
                add_content, add_imports = json_schema_to_python_function(path_name, path_body[http_request_method],
                                                                          http_request_method)
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
    with open(data_classes_path, "r") as file:
        for line in file.readlines():
            connections[line.strip().split(" ")[-1]] = line.strip()

    for name in classes_dict:
        if name in class_content:
            raise Exception("What?")
        class_content[name] = ""

        for i in reversed(sorted(classes_dict[name]["imports"])):
            if i.startswith("#"):
                class_name = i[1:]
                import_line = connections[class_name]
            else:
                import_line = i
            class_content[name] += f"{import_line}\n"
        class_content[name] += "\n\n" + classes_dict[name]["content"]
    return class_content


def get_main_class_content(all_classes_content, class_name, path):
    padding = 0
    content = ""
    for i in all_classes_content:
        content += f"from {path}.{i} import {i}\n"
    content += "from util.BaseRequestClass import BaseRequestClass\n"
    content += "\n"
    content += "\n"
    content += f"class {class_name}(BaseRequestClass):\n"
    padding += 4
    content += " " * padding + "def __init__(self, *args, **kargs):\n"
    padding += 4
    content += " " * padding + f"super({class_name}, self).__init__(*args, **kargs)\n"
    for i in all_classes_content:
        content += " " * padding + f"self.{to_snake_case(i)} = {i}(*args, **kargs)\n"
    return content


def create_query_classes(url, location, data_classes):
    path = Path(__file__)
    query_path = path.parent.joinpath(location)

    temp_path = path.parent.joinpath("_temp")
    data_classes_path = path.parent.joinpath(data_classes).joinpath("__init__.py")
    openapi_json_path = temp_path.joinpath("query_openapi.json")

    if os.path.exists(query_path):
        shutil.rmtree(query_path)

    os.mkdir(query_path)
    # if not os.path.exists(temp_path):
    #     os.mkdir(temp_path)
    #
    # save_openapi_json(url, openapi_json_path)
    title, query_tree = create_tree(openapi_json_path)
    title = title.split(' ')[0]
    all_classes_dict = create_py_classes(query_tree)
    all_classes_content = parse_import_list(all_classes_dict, data_classes_path)
    main_class_content = get_main_class_content(all_classes_content, title, query_path.name)
    for new_class in all_classes_content:
        with open(query_path.joinpath(f"{new_class}.py"), "w") as file:
            file.write(all_classes_content[new_class])
    with open(query_path.joinpath(f"{title}.py"), "w") as file:
        file.write(main_class_content)

    with open(query_path.joinpath("__init__.py"), "w") as file:
        file.write(f"from {query_path.name}.{title} import {title}")


if __name__ == '__main__':
    create_query_classes("http://localhost:8096/api-docs/openapi.json", "query_classes", "data_classes")
