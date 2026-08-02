from calculator.operations import (
    add,
    subtract,
    multiply,
    divide,
    percentage,
    negate,
    square,
    cube,
    square_root,
    pi,
)


class CalculatorEngine:

    def __init__(self):

        self.operations = {
            "+": add,
            "-": subtract,
            "×": multiply,
            "÷": divide,
            "%": percentage,
        }

    def calculate(self, a, b, operator):

        if operator == "±":
            return negate(a)

        if operator == "x²":
            return square(a)

        if operator == "x³":
            return cube(a)

        if operator == "√":
            return square_root(a)

        if operator == "π":
            return pi()

        if operator not in self.operations:
            return "Invalid"

        return self.operations[operator](a, b)