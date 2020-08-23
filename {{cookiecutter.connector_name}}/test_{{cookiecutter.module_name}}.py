from __future__ import annotations
import asyncio
import pytest
{%- set class_prefix = cookiecutter.module_name|replace('_', ' ')|title|replace(' ', '') %}
{%- set config_class_name = class_prefix + 'Configuration' %}
{%- set connector_class_name = class_prefix + 'Connector' %}
{%- set cli_class_name = class_prefix + 'CLI' %}
import servo
from {{ cookiecutter.module_name }} import {{ config_class_name }}, {{ connector_class_name }}, {% if cookiecutter.generate_cli|lower == "y" %} {{ cli_class_name }},{% endif %} __version__


pytestmark = pytest.mark.asyncio


def test_version():
    assert __version__ == "{{ cookiecutter.version }}"

class Test{{ config_class_name }}:
    ...

class Test{{ connector_class_name }}:
    ...

{%- if cookiecutter.generate_cli|lower == "y" %}
class Test{{ cli_class_name }}:
    ...
{%- endif %}
