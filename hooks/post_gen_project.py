#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import urllib.request
from pathlib import Path
from subprocess import check_output
import datetime


def request(
    url: str,
    raise_on_error: bool = True,
) -> str | dict | list:
    headers = {
        "Content-Type": "application/vnd.github+json",
    }

    req = urllib.request.Request(url, headers=headers, method="GET")

    page = None
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
    except urllib.error.HTTPError as e:
        if raise_on_error:
            raise

        print("WARNING: status code", e.status)
        print("...", e.url)
        print("...", str(e))
        return ""

    try:
        result = json.loads(page)
    except Exception:
        result = page

    return result


def mit_license():
    result = request("https://api.github.com/licenses/mit")
    body: str = result["body"]
    body = body.replace("[year]", str(datetime.datetime.now().year))
    body = body.replace("[fullname]", "{{ cookiecutter.full_name }}")

    Path("LICENSE").write_text(body)


venv_dir = f".direnv/python-{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
# Install the Python venv compatible with direnv
check_output(["direnv", "allow"])
check_output(["python", "-m", "venv", venv_dir])

license = "{{ cookiecutter.license }}"
if license == "MIT":
    mit_license()

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
