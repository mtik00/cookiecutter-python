#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from subprocess import check_output
from pathlib import Path

venv_dir = f".direnv/python-{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
# Install the Python venv compatible with direnv
check_output(["direnv", "allow"])
check_output(["python", "-m", "venv", venv_dir])


if "Not open source" == "{{ cookiecutter.open_source_license }}":
    Path("LICENSE").unlink()

# I'm too lazy to figure out how to do all of this here.  The main issue is
# kicking off direnv.
print(
    """
>>>>>>>>>> PROJECT SETUP <<<<<<<<<<

You must run the following commands to complete setup:

cd {{ cookiecutter.project_slug }}
./bin/init-repo.sh
"""
)
