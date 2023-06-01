from math import floor
odd_sums = set()
even_sums = set()

for idx in range(int(input())):
    name = input()
    total = 0
    for letter in name:
        total += ord(letter) / (idx + 1)
    total = floor(total)
    if total % 2 != 0:
        odd_sums.add(total)
    else:
        even_sums.add(total)

odd_total = sum(odd_sums)
even_total = sum(even_sums)

if odd_total == even_total:
    print(f"{odd_total}, {even_total}")

elif odd_total > even_total:
    print(*(odd_sums.difference(even_sums)), sep=", ")

elif odd_total < even_total:
    print(*(odd_sums.symmetric_difference(even_sums)), sep=", ")