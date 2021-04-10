import numbers
import sys

class CalculatorError(Exception):
    """An exception class for calculator"""
    
class Calculator:
    """A terrible calculator"""
    
    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise CalculatorError("Division by zero is invalid")
    
    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number')

if __name__ == '__main__':
    c = Calculator()
    operations = [
        c.add,
        c.subtract,
        c.multiply,
        c.divide,
    ]
    while True:
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        
        operation = input("Pick an operation: ")
        if operation == "q":
            sys.exit()
        op = int(operation)
        
        a = float(input("a: "))
        b = float(input("b: "))
        
        try:
            print(f"Result: {operations[op - 1](a, b)}")
        except CalculatorError as err:
            print(err)
            
            