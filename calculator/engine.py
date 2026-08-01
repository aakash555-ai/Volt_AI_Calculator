from calculator.operations import add, subtract, multiply, divide


class CalculatorEngine:

    def __init__(self):
        self.operations = {
            "+": add,
            "-": subtract,
            "×": multiply,
            "÷": divide,
        }

    def calculate(self, a, b, operator):

        if operator not in self.operations:
            return "Invalid"

        return self.operations[operator](a, b)