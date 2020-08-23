# Servo Assembly Template
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/{{ cookiecutter.image_name }})](https://hub.docker.com/r/{{ cookiecutter.image_name }})
[![Docker Image Size (latest semver)](https://img.shields.io/docker/image-size/{{ cookiecutter.image_name }})](https://hub.docker.com/r/{{ cookiecutter.image_name }})

This directory contains a [cookiecutter](https://github.com/audreyr/cookiecutter) template 
for generating new [Opsani Servo](https://github.com/opsani/servox) assemblies.

The template generates a `Dockerfile` for building the assembly image and assets supporting rapid deployment
including a Docker Compose manifest and a set of Kubernetes manifests that will run the servo in a Deployment.

The connectors that are available within the assembly is configured via Python package management. The `Dockerfile`
generated uses [Poetry](https://python-poetry.org/) for package management and by default inherits from the latest
version of the Opsani servo base image.

Dotenv files are optionally generated to provide credentials to Docker, Compose, and local execution for development.

Several GitHub Actions are auto-configured for project automation. Docker container images will be automatically
published to Docker Hub upon push and release provided that the `DOCKER_USERNAME` and `DOCKER_PASSWORD` secrets are
configured on the repository. Docker tags are automatically provisioned for branches and release tags. Release tags
are built in production mode and will exclude the development packages to slim down the image.

The Docker build setup has been optimized for rapid builds by avoiding cache misses during day to day development
activities and by using the BuildKit backend.

## Generated Project Layout

The templates generates a handful of artifacts in a flat directory hierarchy.

Given a connector name of `new-assembly`, the following directory structure is generated:

```
new-assembly
├── CHANGELOG.md
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── docker-compose.yaml
├── kubernetes.yaml
├── pyproject.toml
└── servo.yaml
```

The `pyproject.toml` manifest is configured with essential project metadata,
a dependency on the [servox](https://github.com/opsani/servox) library, Pytest, 
and support libraries for testing asynchronous code.

## Usage

See documentation in the [repository README.md](../README.md) for details on running templates.
