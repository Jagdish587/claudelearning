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

No test framework is set up yet. To run tests if added:

```bash
python -m pytest          # if using pytest
python -m unittest        # if using unittest
```
