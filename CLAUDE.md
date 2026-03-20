# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Python learning/experimentation repository. Currently it contains a single module, [calculator.py](calculator.py), with basic arithmetic functions (`add`, `subtract`, `multiply`, `divide`).

## Running Code

```bash
python calculator.py
python -c "from calculator import add; print(add(2, 3))"
```

## Running Tests

Tests are written using [pytest](https://pytest.org) and located in `test_calculator.py`.

```bash
python -m pytest                  # run all tests
python -m pytest -v               # verbose output
python -m pytest test_calculator.py  # run specific test file
```

Install pytest if needed:

```bash
pip install pytest
```
