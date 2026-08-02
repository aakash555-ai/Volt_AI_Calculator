import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error"
    return a / b


def percentage(a, b):
    return (a * b) / 100


def negate(a):
    return -a


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def square_root(a):
    if a < 0:
        return "Error"
    return math.sqrt(a)


def pi():
    return math.pi