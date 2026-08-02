from calculator.engine import CalculatorEngine

engine = CalculatorEngine()

print("Add:", engine.calculate(10, 5, "+"))
print("Subtract:", engine.calculate(10, 5, "-"))
print("Multiply:", engine.calculate(10, 5, "×"))
print("Divide:", engine.calculate(10, 5, "÷"))

print("Square:", engine.calculate(5, 0, "x²"))
print("Cube:", engine.calculate(3, 0, "x³"))
print("Square Root:", engine.calculate(81, 0, "√"))
print("Pi:", engine.calculate(0, 0, "π"))