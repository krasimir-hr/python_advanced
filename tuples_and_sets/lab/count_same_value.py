numbers = tuple([float(x) for x in input().split()])

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

for number, occurrence in occurrences.items():
    print(f"{number} - {occurrence} times")