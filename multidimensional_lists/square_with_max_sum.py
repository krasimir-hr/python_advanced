from sys import maxsize

rows, columns = [int(x) for x in input().split(", ")]

biggest_sum = -maxsize
submatrix = []
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

for i in range(rows - 1):
    for j in range(columns - 1):
        current_number = matrix[i][j]
        right_number = matrix[i][j + 1]
        down_number = matrix[i + 1][j]
        diagonal_number = matrix[i + 1][j + 1]
        total = current_number + right_number + down_number + diagonal_number
        if biggest_sum < total:
            biggest_sum = total
            submatrix = [[current_number, right_number], [down_number, diagonal_number]]

for row in submatrix:
    print(*row)
print(biggest_sum)
