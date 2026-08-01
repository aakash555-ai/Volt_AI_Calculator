from calculator.engine import CalculatorEngine

engine = CalculatorEngine()

print("Addition:", engine.calculate(10, 5, "+"))
print("Subtraction:", engine.calculate(10, 5, "-"))
print("Multiplication:", engine.calculate(10, 5, "×"))
print("Division:", engine.calculate(10, 5, "÷"))
print("Percentage:", engine.calculate(200, 10, "%"))
print("Negate:", engine.calculate(5, 0, "±"))