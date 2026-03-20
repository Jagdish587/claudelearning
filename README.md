# claudelearning

A simple Python learning project featuring a basic calculator module.

## About

This project is a hands-on Python learning exercise. It includes a `calculator` module with common arithmetic operations and a test suite to verify their correctness.

## Features

- **Add** two numbers
- **Subtract** one number from another
- **Multiply** two numbers
- **Divide** two numbers (with zero-division protection)

## Project Structure

```
claudelearning/
├── calculator.py       # Core arithmetic functions
├── test_calculator.py  # pytest test suite
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- [pytest](https://pytest.org)

```bash
pip install pytest
```

### Usage

```python
from calculator import add, subtract, multiply, divide

add(2, 3)        # 5
subtract(10, 4)  # 6
multiply(3, 4)   # 12
divide(10, 2)    # 5.0
```

You can also run the module directly:

```bash
python calculator.py
```

## Running Tests

```bash
python -m pytest          # run all tests
python -m pytest -v       # verbose output
```

## Notes

- `divide` raises a `ValueError` if you attempt to divide by zero.
