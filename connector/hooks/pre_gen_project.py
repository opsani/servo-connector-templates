#!/usr/bin/env python
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.module_name }}'

print(f"Checking module {module_name}")
if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: The module_name "{module_name}" is not a valid Python module name.')
    sys.exit(1)

print("pre-hook completed successfully")
