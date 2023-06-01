def func_executor(*kwargs):
    results = []
    for kwarg in kwargs:
        func, args = kwarg
        result = func(*args)
        result_string = f"{func.__name__} - {result}"
        results.append(result_string)

    return '\n'.join(results)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
(sum_numbers, (1, 2)),
(multiply_numbers, (2, 4))
))