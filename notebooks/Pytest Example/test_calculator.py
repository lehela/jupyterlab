"""Test the terrible calculator"""

import pytest
from calculator import Calculator, CalculatorError

def test_add():
    """test"""
    calc = Calculator()
    assert calc.add(2,3) == 5

def test_add_weird_stuff():
    """test"""
    calc = Calculator()
    with pytest.raises(CalculatorError):
        calc.add("two",3)

def test_add_weirder_stuff():
    """test"""
    calc = Calculator()
    with pytest.raises(CalculatorError):
        calc.add("two","three")

def test_subtract():
    """test"""
    calc = Calculator()
    assert calc.subtract(2,3) == -1

def test_multiply():
    """test"""
    calc = Calculator()
    assert calc.multiply(2,3) == 6

def test_divide():
    """test"""
    calc = Calculator()
    assert calc.divide(5,2) == 2.5

def test_divide_by_zero():
    """test"""
    calc = Calculator()
    with pytest.raises(CalculatorError) as context:
        calc.divide(5,0)
    assert str(context.value) == "Division by zero is invalid"
