![Platform: Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Language: Python](https://img.shields.io/badge/Language-Python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build](https://github.com/CSC510-Group18/hw1/actions/workflows/python-app.yml/badge.svg)](https://github.com/CSC510-Group18/hw1/actions/workflows/python-app.yml)
[![Linter: Ruff](https://img.shields.io/badge/Linter-Ruff-brightgreen?style=flat-square)](https://github.com/charliermarsh/ruff)
[![Formatter: Ruff](https://img.shields.io/badge/Formatter-Ruff-brightgreen?style=flat-square)](https://github.com/charliermarsh/ruff)

## Install

```bash
pip install -r requirements.txt
```

## Generate Documentation

```bash
cd docs && make html # Note that requirements.txt is required for this to work
```

After running the above command, the documentation will be generated in the `docs/build/html` directory.

## Run Tests

```bash
pytest tests.py
```

## Code Linting and Formatting

```bash
ruff check .
```

```bash
ruff format .
```
