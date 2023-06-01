rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

flattened = [num for row in matrix for num in row]
print(flattened)