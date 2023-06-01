def even_odd(*args):
    numbers = args[:-1]
    command = args[-1]
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if command == "even":
        return even
    elif command == "odd":
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

