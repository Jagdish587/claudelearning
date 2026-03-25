import pytest
from calculator import add, subtract, multiply, divide, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(3, 3) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(0, 5) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_power():
    # Testing report:
    # - positive base and exponent: 2^3 = 8
    # - base to the power of 0: any number^0 = 1
    # - exponent of 1: any number^1 = itself
    # - negative exponent: 2^-1 = 0.5
    # - zero base: 0^5 = 0
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(7, 1) == 7
    assert power(2, -1) == 0.5
    assert power(0, 5) == 0
