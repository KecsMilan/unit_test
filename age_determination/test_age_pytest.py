import pytest
from age import categorizeByAge

def test_child():
    assert categorizeByAge(6) == "child"

def test_teenager():
    assert categorizeByAge(14) == "teenager"

def test_adult():
    assert categorizeByAge(20) == "adult"

def test_goldenAge():
    assert categorizeByAge(66) == "golden age"

def test_invalid():
    assert categorizeByAge(2025) == "invalid age: 2025"