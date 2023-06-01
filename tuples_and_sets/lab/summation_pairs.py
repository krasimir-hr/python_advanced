numbers = [int(x) for x in input().split()]
target = int(input())

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")
