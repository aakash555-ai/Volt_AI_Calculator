from calculator.operations import (
    add,
    subtract,
    multiply,
    divide,
    percentage,
    negate,
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

        if operator not in self.operations:
            return "Invalid"

        return self.operations[operator](a, b)