#!/usr/bin/env python
import os
import subprocess
import shlex

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

def install_deps():
    """
    Install the dependencies via Poetry
    """
    run_command("poetry install")

install_deps()
