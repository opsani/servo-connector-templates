#!/usr/bin/env python
import os
import subprocess
import shlex
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def run_command(command: str):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf8")
    while True:
        output = process.stdout.readline()
        if output:
            print(output.strip())
        if process.poll() is not None:
            # Child process has exited, stop polling
            break

    if process.returncode != 0:
        raise RuntimeError(f"command failed with non-zero exit code {process.returncode}: {command}")

{%- if cookiecutter.dotenv|lower != "y" %}
remove_file(".env")
{%- endif %}

{%- if cookiecutter.kubernetes|lower != "y" %}
remove_file("kubernetes.yaml")
{%- endif %}

{%- if cookiecutter.docker_compose|lower != "y" %}
remove_file("docker-compose.yaml")
{%- endif %}

# Create a placeholder config file
# Docker will mkdir if we don't have a file in place on volume mount
Path("servo.yaml").touch()
