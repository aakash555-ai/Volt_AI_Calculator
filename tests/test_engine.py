from calculator.engine import CalculatorEngine

engine = CalculatorEngine()

print(engine.calculate(10, 5, "+"))
print(engine.calculate(10, 5, "-"))
print(engine.calculate(10, 5, "×"))
print(engine.calculate(10, 5, "÷"))