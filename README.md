# cookie-cutter-python

This is my default cookiecutter template for python things.

Use it with:
```shell
cookiecutter https://github.com/mtik00/cookiecutter-python.git
```

## Requirements

- Python 3.x
- Cookiecutter
- Poetry
- [Poetry "up" plugin](https://github.com/MousaZeidBaker/poetry-plugin-up#installation)

## Features

- [Pre-commit](https://pre-commit.com/) + [commitizen](https://commitizen-tools.github.io/commitizen/)
    - Commit messages are checked for [Conventional Commits](https://www.conventionalcommits.org/en/)
    - Commits are checked using flake8, black, and more (see .pre-commit-config.yaml)
- Commitizen
    - `cz` used for bumping versions and maintaining `CHANGELOG.md`
