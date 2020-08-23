# Servo Connector Template

This directory contains a [cookiecutter](https://github.com/audreyr/cookiecutter) template 
for generating new connectors for use in [Opsani Servo](https://github.com/opsani/servox) assemblies. 
The same core set of tools used in the servo are installed and configured in the generated project 
including [Poetry](https://python-poetry.org/), [Pytest](https://docs.pytest.org/en/stable/), 
and [asyncio](https://asyncio.readthedocs.io/en/latest/).

It will generate a configuration class, a connector class, and optionally a
CLI class and scaffold tests for the classes. A basic README.md is generated
and the LICENSE file is populated.

Python packaging is set up via pyproject.toml and an entry point
is configured to allow the Servo to auto-discover the new connector. This means that
installing the connector library via package management is all that is required to
make it available for use in the assembly.

Several GitHub Actions are auto-configured for project automation including continuous
integration and automatic publication to PyPi upon publishing a new release.

In order for automatic package publication to succeed a `PYPI_TOKEN` secret must be configured
on the GitHub repository before publishing a release.

## Generated Project Layout

The template will generate and configure a standard Python library with a module in a single
`.py` source file, a supporting Pytest file, and supporting documentation and artifacts.

Given a connector name of `awesome-connector`, the following directory structure is generated:

```
awesome-connector
├── CHANGELOG.md
├── LICENSE
├── README.md
├── awesome_connector.py
├── poetry.lock
├── pyproject.toml
└── test_awesome_connector.py
```

The `pyproject.toml` manifest is configured with essential project metadata,
a dependency on the [servox](https://github.com/opsani/servox) library, Pytest, 
and support libraries for testing asynchronous code.

## Usage

See documentation in the [repository README.md](../README.md) for details on running templates.
