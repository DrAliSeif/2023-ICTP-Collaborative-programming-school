from factorial import factorial
import pytest


def test_factorial_1():
    assert(factorial(1)==1)

def test_factorial_2():
    assert(factorial(2)==2)

def test_factorial_3():
    assert(factorial(3)==6)

def test_factorial_4():
    assert(factorial(4)==24)

def test_factorial_0():
    assert(factorial(0)==1)

def test_factorial_negative_number():
    with pytest.raises(ValueError):
        factorial(-1)
