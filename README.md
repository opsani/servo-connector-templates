# servo-connector-templates
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/opsani/servo-connector-templates)](https://hub.docker.com/r/opsani/servo-connector-templates)
[![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/opsani/servo-connector-templates)](https://hub.docker.com/r/opsani/servo-connector-templates)

This repository contains a set of [cookiecutter](https://github.com/audreyr/cookiecutter) templates 
for generating new connectors for use in [Opsani Servo](https://github.com/opsani/servox) assemblies. 
The same core set of tools used in the servo are installed and configured in the generated project 
including [Poetry](https://python-poetry.org/), [Pytest](https://docs.pytest.org/en/stable/), 
and [asyncio](https://asyncio.readthedocs.io/en/latest/).

It will generate a configuration class, a connector class, and optionally a
CLI class and scaffold tests for the classes. A basic README.md is generated
and the LICENSE file is populated.

Python packaging is set up via pyproject.toml and an entry point
is configured to allow the Servo to auto-discover the new connector.

Several GitHub Actions are auto-configured for project automation including continuous
integration and automatic publication to PyPi upon publishing a new release.

In order for automatic package publication to succeed a `PYPI_TOKEN` secret must be configured
on the GitHub repository before publishing a release.

## Usage

### Running locally

```console
$ pip install cookiecutter
```

Alternatively, you can install cookiecutter with Homebrew (macOS only):

```console
$ brew install cookiecutter
```

Finally, to run it based on this template, execute:

```console
$ cookiecutter https://github.com/opsani/servo-connector-templates.git
```

You will be asked about your basic info (name, email, connector name, options, etc). This info will be used to customize your new project.

If you are customizing the template, you can build and run from a local working copy:

```console
$ git clone https://github.com/opsani/servo-connector-templates.git
$ cd servo-connector-templates
$ poetry install
$ poetry run cookiecutter .
```

### Running under Docker

Container images and a Dockerfile are provided if you would prefer to generate the project within Docker. 
The container will write the generated project to `/connector`. You can use a bind mount to let the 
container write out the generated files to the host:

```console
$ docker run --rm -it -v $(pwd):/connector opsani/servo-connector-templates:latest
```

If you are customizing the template, you can build and run from a local working copy:

```console
$ git clone https://github.com/opsani/servo-connector-templates.git
$ docker build -t opsani/servo-connector-templates:latest servo-connector-templates
$ docker run --rm -it -v $(pwd):/connector opsani/servo-connector-templates:latest
```

There are also Makefile shortcuts for building and running the image:

```console
$ make build
$ make run
```

## License

servo-connector-templates is distributed under the terms of the Apache 2.0 Open Source license.

A copy of the license is provided in the [LICENSE](LICENSE) file at the root of the repository.
