"""
    Terrible calculator
"""

import numbers
import sys

class CalculatorError(Exception):
    """An exception class for calculator"""

class Calculator:
    """A terrible calculator"""

    def add(self, op_a, op_b):
        """adds"""
        self._check_operand(op_a)
        self._check_operand(op_b)
        return op_a + op_b

    @classmethod
    def subtract(cls, op_a, op_b):
        """subtracts"""
        return op_a - op_b

    @classmethod
    def multiply(cls, op_a, op_b):
        """multiplies"""
        return op_a * op_b

    @classmethod
    def divide(cls, op_a, op_b):
        """divides"""
        try:
            return op_a / op_b
        except ZeroDivisionError as exc_zero:
            raise CalculatorError("Division by zero is invalid") from exc_zero

    @classmethod
    def _check_operand(cls, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not op_a number')

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

        my_a = float(input("a: "))
        my_b = float(input("b: "))

        try:
            print(f"Result: {operations[op - 1](my_a, my_b)}")
        except CalculatorError as err:
            print(err)
            