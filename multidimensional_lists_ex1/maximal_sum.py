from sys import maxsize

rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for y in range(rows)]

max_sum = -maxsize
max_submatrix = []

for i in range(rows - 2):
    for j in range(columns - 2):
        row_1_col_1 = matrix[i][j]
        row_1_col_2 = matrix[i][j + 1]
        row_1_col_3 = matrix[i][j + 2]
        row_2_col_1 = matrix[i + 1][j]
        row_2_col_2 = matrix[i + 1][j + 1]
        row_2_col_3 = matrix[i + 1][j + 2]
        row_3_col_1 = matrix[i + 2][j]
        row_3_col_2 = matrix[i + 2][j + 1]
        row_3_col_3 = matrix[i + 2][j + 2]
        total_sum = row_1_col_1 + \
                    row_1_col_2 + \
                    row_1_col_3 + \
                    row_2_col_1 + \
                    row_2_col_2 + \
                    row_2_col_3 + \
                    row_3_col_1 + \
                    row_3_col_2 + \
                    row_3_col_3
        if max_sum < total_sum:
            max_sum = total_sum
            max_submatrix = [[row_1_col_1, row_1_col_2, row_1_col_3],
                             [row_2_col_1, row_2_col_2, row_2_col_3],
                             [row_3_col_1, row_3_col_2, row_3_col_3]]

print(f"Sum = {max_sum}")
for row in max_submatrix:
    print(*row)