import sys
import os
import inspect
import argparse
import yaml
import importlib.util
from typing import Any


def main(argv):
    parser = argparse.ArgumentParser(description="Generates model for specific model checker from template\
 and settings using generator module")
    parser.add_argument("-t", "--template", metavar="", type=str, required=True, help="Path to the template file")
    parser.add_argument("-s", "--settings", metavar="", type=str, required=True, help="Path to the YAML settings file")
    parser.add_argument("-g", "--generator", metavar="", type=str, required=True,
                        help="Path to the file with generator class")
    parser.add_argument("-l", "--language", metavar="", type=str, required=False, default="prism",
                        help="Name of the model checker language that must be applied")
    parser.add_argument("-o", "--output", metavar="", type=str, required=False, help="Path to store result model file")

    result = parser.parse_args(argv)

    settings = load_settings(result.settings)
    generator = load_generator(result.generator, settings)
    compiler = load_compiler(result.language, result.template, generator)

    program = compiler.compile()

    if result.output is not None:
        output_path = result.output
    else:
        output_path = create_output_path(result.template)

    with open(output_path, "w") as result_file:
        result_file.write(str(program))


def load_settings(path: str):
    with open(path, 'r') as file:
        settings = yaml.load(file)
    return settings


def load_generator(path: str, settings: Any):
    filename = os.path.basename(path)
    module_name, ext = os.path.splitext(filename)
    module_spec = importlib.util.spec_from_file_location(module_name, path)
    module_obj = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module_obj)
    generator_class = getattr(module_obj, module_name)
    return generator_class(settings)


def load_compiler(name: str, template_path: str, generator: Any):
    path = os.path.abspath(inspect.getsourcefile(lambda: 0))
    path = os.path.dirname(path)
    path = os.path.join(path, "core/{}/compile.py".format(name))
    filename = os.path.basename(path)
    module_name, ext = os.path.splitext(filename)
    module_spec = importlib.util.spec_from_file_location(module_name, path)
    module_obj = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module_obj)
    generator_class = getattr(module_obj, 'Compiler')
    return generator_class(generator, template_path)


def create_output_path(template_path: str):
    filename = os.path.basename(template_path)
    dir_name = os.path.dirname(template_path)
    output_name = "out_{}".format(filename)
    return os.path.join(dir_name, output_name)

if __name__ == '__main__':
    main(sys.argv[1:])
