def sort_and_sum(*args):
    positive_numbers = []
    negative_numbers = []
    result = ""
    for num in args:
        if num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negative_numbers.append(num)
    sum_positive = sum(positive_numbers)
    sum_negative = sum(negative_numbers)
    if abs(sum_negative) > abs(sum_positive):
        result = "The negatives are stronger than the positives"
    else:
        result = "The positives are stronger than the negatives"

    return print(f"{sum_negative}\n{sum_positive}\n{result}")


numbers = [int(x) for x in input().split()]
sort_and_sum(*numbers)
