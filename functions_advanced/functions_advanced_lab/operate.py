def operate(operator, *args):
    def sum_nums():
        return sum(args)

    def subtract():
        res = 0
        for arg in args:
            res -= arg
        return res

    def multiply():
        res = 1
        for arg in args:
            res *= arg
        return res

    def divide():
        res = 1
        for arg in args:
            res /= args
        return res

    if operator == "+":
        return sum_nums()

    elif operator == "-":
        return subtract()

    elif operator == "*":
        return multiply()

    else:
        return divide()

print(operate("+", 1, 2, 3))