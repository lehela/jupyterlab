from calculator import Calculator, CalculatorError
import pytest

def test_add():
    c = Calculator()
    assert c.add(2,3) == 5

def test_add_weird_stuff():
    c = Calculator()
    with pytest.raises(CalculatorError):
        result = c.add("two",3)

def test_add_weirder_stuff():
    c = Calculator()
    with pytest.raises(CalculatorError) as context:
        result = c.add("two","three")
    
def test_subtract():
    c = Calculator()
    assert c.subtract(2,3) == -1

def test_multiply():
    c = Calculator()
    assert c.multiply(2,3) == 6

def test_divide():
    c = Calculator()
    assert c.divide(5,2) == 2.5

def test_divide_by_zero():
    c = Calculator()
    with pytest.raises(CalculatorError) as context:
        result = c.divide(5,0)
    assert str(context.value) = "Division by zero is invalid"
