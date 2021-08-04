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
        "$schema": "http://json-schema.org/schema#"

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


def add_imports(core_py, new_class_list):
    for new_class in new_class_list:
        imports_str = f"from schema.classes.{core_py.filename} import *\n"

        if new_class == core_py:
            continue

        for new_class_j in new_class_list:
            if new_class_j == core_py or new_class_j == new_class:
                continue

            not_variable = "[^a-zA-Z0-9]"
            matches = re.findall(not_variable + new_class_j.class_name + not_variable, new_class.content)
            if len(matches) > 0:
                imports_str += f"from schema.classes.{new_class_j.filename} import {new_class_j.class_name}\n"

        new_class.content = imports_str + "\n\n" + new_class.content


def main(url):
    path = Path(__file__)
    schema_path = path.parent.joinpath("schema")
    json_schema_path = schema_path.joinpath("json")
    classes_path = schema_path.joinpath("classes")
    combine_json_schema_path = json_schema_path.joinpath("_all.json")
    combine_classes_py_path = classes_path.joinpath("_all.py")

    if os.path.exists(schema_path):
        shutil.rmtree(schema_path)

    os.mkdir(schema_path)
    os.mkdir(json_schema_path)
    os.mkdir(classes_path)

    open(schema_path.joinpath("__init__.py"), "w").close()
    open(classes_path.joinpath("__init__.py"), "w").close()

    create_json_schema(url, json_schema_path, combine_json_schema_path)
    create_py(combine_json_schema_path, combine_classes_py_path)
    core_py, new_class_list = to_class_dict(combine_classes_py_path)
    add_imports(core_py, new_class_list)

    for new_class in new_class_list:
        with open(classes_path.joinpath(f"{new_class.filename}.py"), "w") as file:
            file.write(new_class.content)
    exit()

if __name__ == '__main__':
    main("http://localhost:8096/api-docs/openapi.json")
