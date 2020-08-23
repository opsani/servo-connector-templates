# servo-templates
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/opsani/servo-templates)](https://hub.docker.com/r/opsani/servo-templates)
[![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/opsani/servo-templates)](https://hub.docker.com/r/opsani/servo-templates)

This repository contains a set of [cookiecutter](https://github.com/audreyr/cookiecutter) templates 
for generating new projects for use with [Opsani Servo](https://github.com/opsani/servox). 

## Available templates

Each template lives within a subdirectory of this repository. Each template is documented independently in the 
README.md within the template subdirectory.

### Assembly

The [assembly](assembly) template provides support for generating new servo assemblies. An assembly is a versioned, 
distributable container that includes the base servo and a chosen set of connectors. Opsani maintains and distributes
a canonical set of assembly container images but from time to time it may become necessary to create a new assembly
to meet specific needs (e.g. integrating with a proprietary system or handling specific requirements such as version
mandates). The assembly template configures Python package management, a Dockerfile for building the assembly image,
and supporting automation.

### Connector

The [connector](connector) template enables generation of new servo connectors. Connectors are plugins for the servo
that provide functionality and connectivity to resources and systems for optimization. They are developed and distributed 
as standard Python libraries. The template generates a connector scaffold configured according to best practices and 
standard tooling recommended by Opsani.

## Usage

### Running locally

```console
$ pip install cookiecutter
```

Alternatively, you can install cookiecutter with Homebrew (macOS only):

```console
$ brew install cookiecutter
```

To run a template, identify the name of its subdirectory (e.g. `assembly` or `connector`) and invoke cookiecutter:

```console
$ cookiecutter https://github.com/opsani/servo-templates.git --directory=[TEMPLATE_SUBDIR_NAME]
```

You will be prompted to provide necessary input to configure your new project.

If you are customizing the templates, you can build and run from a local working copy:

```console
$ git clone https://github.com/opsani/servo-templates.git
$ cd servo-templates
$ poetry install
$ poetry run cookiecutter . --directory=[TEMPLATE_SUBDIR]
```

### Running under Docker

Container images and a Dockerfile are provided if you would prefer to generate your projects within Docker. 
The container will write the generated project to the `/build` path. You can use a bind mount a directory
to let the container write out the generated files to the host filesystem:

```console
$ docker run --rm -it -v $(pwd):/build opsani/servo-templates:latest --directory=[TEMPLATE_SUBDIR]
```

If you are customizing the templates, you can build and run from a local working copy:

```console
$ git clone https://github.com/opsani/servo-templates.git
$ docker build -t opsani/servo-templates:latest servo-templates
$ docker run --rm -it -v $(pwd):/build opsani/servo-templates:latest --directory=[TEMPLATE_SUBDIR]
```

There are also Makefile shortcuts for building and running the image:

```console
# Build the container image
$ make build

# Run a specific template
$ make -e TEMPLATE_SUBDIR=[TEMPLATE_SUBDIR] run

# Convenience aliases for running templates
$ make assembly
$ make connector
```

## Template Customization

Templates are vanilla cookiecutter implementations. Each template subdirectory has 
a `cookiecutter.json` file that defines the context and configuration options.

Filenames, directory names, and file content are templated via [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/).

Refer to the [cookiecutter](https://cookiecutter.readthedocs.io/) documentation site
for specifics about the templating environment, examples, and reference projects.

## License

servo-templates is distributed under the terms of the Apache 2.0 Open Source license.

A copy of the license is provided in the [LICENSE](LICENSE) file at the root of the repository.
