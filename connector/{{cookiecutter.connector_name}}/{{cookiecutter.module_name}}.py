from __future__ import annotations
from importlib.metadata import PackageNotFoundError, version

import servo
from servo import metadata, License, Maturity

try:
    __version__ = version("{{ cookiecutter.connector_name }}")
except PackageNotFoundError:
    __version__ = "0.0.0"

{%- set class_prefix = cookiecutter.module_name|replace('_', ' ')|title|replace(' ', '') %}
{%- set config_class_name = class_prefix + 'Configuration' %}
{%- set connector_class_name = class_prefix + 'Connector' %}
{%- set cli_class_name = class_prefix + 'CLI' %}
class {{ config_class_name }}(servo.BaseConfiguration):

    @classmethod
    def generate(cls, **kwargs) -> {{ config_class_name }}:
        return cls(
            **kwargs,
        )

@metadata(
    name="{{ cookiecutter.connector_name }}",
    description="{{ cookiecutter.description }}",
    version=__version__,
    homepage="{{ cookiecutter.homepage }}",
    license=License.APACHE2,
    maturity=Maturity.EXPERIMENTAL,
)
class {{ connector_class_name }}(servo.BaseConnector):
    config: {{ config_class_name }}

{%- if cookiecutter.generate_cli|lower == "y" %}
class {{ cli_class_name }}(servo.cli.ConnectorCLI):
    ...
{%- endif %}
