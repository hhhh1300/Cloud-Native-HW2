import pytest
from src.arithmetics import add, subtract, multiply, intergerDivide, factorial

def test_add():
    assert add(1, 2) == 3
    
def test_subtract():
    assert subtract(5, 3) == 2
    
def test_multiply():
    assert multiply(4, 2) == 8

def test_integer_divide():
    assert intergerDivide(10, 2) == 5
    try:
        intergerDivide(10, 0)
    except ValueError:
        assert True
    else:
        assert False
        
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        factorial(-1)
    except ValueError:
        assert True
    else:
        assert False