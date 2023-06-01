rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for _ in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)
    total_sum += sum(current_row)

print(total_sum)
print(matrix)
