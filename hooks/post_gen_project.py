#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import check_call

# Install the Python venv compatible with direnv
check_call(["direnv", "allow"])
check_call(["python", "-m", "venv", ".direnv/python-3.11"])

# I'm too lazy to figure out how to do all of this here.  The main issue is
# kicking off direnv.ascii
print(
    """
>>>>>>>>>> PROJECT SETUP <<<<<<<<<<

You must run the following commands to complete setup:

cd {{ cookiecutter.project_slug }}
git init .
poetry install
pre-commit autoupdate
pre-commit install
git add .
git commit -am"chore: initial files"
"""
)
