#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from subprocess import check_output
from pathlib import Path

ENVRC = """layout python3
PATH_add bin

[[ -f .secrets/env.sh ]] && source .secrets/env.sh

export PYTHONBREAKPOINT=ipdb.set_trace
"""

Path(".envrc").write_text(ENVRC)

env_sh = Path(".secrets/env.sh")
env_sh.parent.mkdir(parents=True, exist_ok=True)
env_sh.write_text(
    """#!/usr/bin/env bash
# Use this file to store any sensitive data in the form of env vars.
# This file will be source automatically by direnv.

export DJANGO_SECRET_KEY='super-secret-key'"""
)

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
