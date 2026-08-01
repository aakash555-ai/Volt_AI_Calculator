from calculator.operations import add, subtract, multiply, divide


class CalculatorEngine:

    def calculate(self, a, b, operator):

        if operator == "+":
            return add(a, b)

        elif operator == "-":
            return subtract(a, b)

        elif operator == "×":
            return multiply(a, b)

        elif operator == "÷":
            return divide(a, b)

        return "Invalid"