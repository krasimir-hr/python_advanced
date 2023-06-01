def even_odd_filter(**kwargs):
    filtered_numbers = {}
    for key, numbers in kwargs.items():
        if key == "odd":
            filtered_numbers[key] = [num for num in numbers if num % 2 != 0]
        elif key == "even":
            filtered_numbers[key] = [num for num in numbers if num % 2 == 0]

    sorted_numbers = dict(sorted(filtered_numbers.items(), key=lambda x: -len(x[1])))
    return sorted_numbers


print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))