import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import List, Union


class NewClassFile:
    def __init__(self, filename: str, class_name: Union[None, str], content: str = ""):
        self.content = content
        self.class_name = class_name
        self.filename = filename


def create_json_schema(url, json_schema_path: Path, combine_json_schema: Path):
    subprocess.run(["openapi2jsonschema", url, "-o", json_schema_path])
    all_json_schema = {
        "type": "object",
        "properties": {},
        "additionalProperties": False,
        "$schema": "https://json-schema.org/schema#"
    }
    with open(json_schema_path.joinpath("all.json"), "r") as file:
        json_schema = json.loads(file.read())
        for i in json_schema["oneOf"]:
            all_json_schema["properties"][i["$ref"].replace(".json", "")] = {
                "allOf": [{"$ref": i["$ref"]}],
                "nullable": True
            }
    with open(combine_json_schema, "w") as file:
        file.write(json.dumps(all_json_schema, indent=4))


def create_py(combine_json_schema_path, combine_classes_py_path):
    subprocess.run([
        "cd", combine_json_schema_path.parent, "&&",
        "quicktype",
        "-o", combine_classes_py_path.absolute(),
        "--src-lang", "schema", combine_json_schema_path.name,
        "--python-version", "3.7"
    ], shell=True)

    with open(combine_classes_py_path, "r") as file:
        content = file.read()
    content = f"from util.CaseInsensitiveEnum import CaseInsensitiveEnum\n" + content
    content = content.replace("(Enum)", "(CaseInsensitiveEnum)")
    with open(combine_classes_py_path, "w") as file:
        file.write(content)


def to_class_dict(combine_classes_py_path) -> (NewClassFile, List[NewClassFile]):
    core_py = NewClassFile(filename="_core", class_name=None)
    new_class_list = [core_py]
    current = core_py
    with open(combine_classes_py_path, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "@dataclass" in line:
                continue

            if re.match("^class .*", line):
                class_name = line.strip()
                class_name = class_name[6:]
                if "(" in class_name:
                    class_name = class_name[:class_name.find("(")]
                else:
                    class_name = class_name[:class_name.find(":")]

                # To snake_case
                name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
                new_class_file = NewClassFile(filename=name, class_name=class_name)
                if "@dataclass" in lines[i - 1]:
                    new_class_file.content += lines[i - 1]
                new_class_list.append(new_class_file)
                current = new_class_file

            current.content += line
    core_py.content += ""
    return core_py, new_class_list


def add_imports(core_py, new_class_list, folder_name):
    for new_class in new_class_list:
        imports_str = f"from {folder_name}.{core_py.filename} import *\n"

        if new_class == core_py:
            continue

        for new_class_j in new_class_list:
            if new_class_j == core_py or new_class_j == new_class:
                continue

            not_variable = "[^a-zA-Z0-9]"
            matches = re.findall(not_variable + new_class_j.class_name + not_variable, new_class.content)
            if len(matches) > 0:
                imports_str += f"from {folder_name}.{new_class_j.filename} import {new_class_j.class_name}\n"

        new_class.content = imports_str + "\n\n" + new_class.content


def get_init_file_content(all_class_path, new_class_list, folder_name):
    class_content = []

    with open(all_class_path, "r") as file:
        for line in file.readlines():
            if line.startswith("class "):
                class_content = []
            class_content.append(line)

    main_content = []
    find_to_dict = False
    for line in class_content:
        if find_to_dict:
            if line.strip().startswith("return "):
                break
            main_content.append(line.strip())
        if "def to_dict" in line and not find_to_dict:
            find_to_dict = True
            continue

    main_content = main_content[1:]
    map_list = []
    for x in main_content:
        org_class_name, new_class_name = x.split("=")
        org_class_name = org_class_name.strip()
        new_class_name = new_class_name.strip()
        org_class_name = org_class_name[org_class_name.find('"') + 1:-2]
        new_class_name = new_class_name.split(",")[0].split("(")[-1]
        map_list.append((org_class_name, new_class_name))

    content = ""
    for org_class_name, new_class_name in map_list:
        c = True
        for class_obj in new_class_list:
            if class_obj.class_name == new_class_name:
                content += f"from {folder_name}.{class_obj.filename} import {class_obj.class_name} as {org_class_name}\n"
                c = False
                break
        if c:
            raise Exception("What?")

    return content


def main(url, location):
    path = Path(__file__)
    schema_path = path.parent.joinpath(location)

    temp_path = path.parent.joinpath("_temp")
    json_schema_path = temp_path.joinpath("data_json")
    combine_json_schema_path = json_schema_path.joinpath("_all.json")
    combine_classes_py_path = temp_path.joinpath("data_all.py")

    if os.path.exists(schema_path):
        shutil.rmtree(schema_path)

    os.mkdir(schema_path)
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)
    if os.path.exists(json_schema_path):
        shutil.rmtree(json_schema_path)

    os.mkdir(json_schema_path)

    create_json_schema(url, json_schema_path, combine_json_schema_path)
    create_py(combine_json_schema_path, combine_classes_py_path)
    core_py, new_class_list = to_class_dict(combine_classes_py_path)
    init_content = get_init_file_content(combine_classes_py_path, new_class_list, schema_path.name)
    add_imports(core_py, new_class_list, schema_path.name)

    for new_class in new_class_list:
        with open(schema_path.joinpath(f"{new_class.filename}.py"), "w") as file:
            file.write(new_class.content)

    with open(schema_path.joinpath("__init__.py"), "w") as file:
        file.write(init_content)

    # os.remove(combine_classes_py_path)
    # os.remove(combine_json_schema_path)


if __name__ == '__main__':
    main("http://localhost:8096/api-docs/openapi.json", "data_classes")
