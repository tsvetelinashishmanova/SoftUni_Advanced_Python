from functools import reduce


def operate(operator, *args):

    def calculate(a, b):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b

    result = reduce(calculate, args)
    return result


print(operate("+", 1, 2, 3))
