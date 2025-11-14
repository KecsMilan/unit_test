#python -m pytest test_calculator.py -v

import pytest
from calculator import sum, substract, multiply, divide

def test_sum():
    assert sum(3, 5) == 8
    assert sum(-1, 1) == 0
    assert sum(-3, -2) == -5
    assert sum(0, 0) == 0

def test_substract():
    assert substract(10, 3) == 7
    assert substract(-10, -10) == 0

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(0, 0) == "Error: Division by zero"
    assert divide(15, 3) == 5