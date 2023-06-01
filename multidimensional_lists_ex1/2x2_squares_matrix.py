rows, columns = [int(x) for x in input().split()]

matrix = [list(input().split()) for row in range(rows)]
unique_symbols = set()
two_by_twos = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current_ch = matrix[row][column]
        right_ch = matrix[row][column + 1]
        below_ch = matrix[row + 1][column]
        diag_ch = matrix[row + 1][column + 1]
        if current_ch == right_ch == below_ch == diag_ch:
            two_by_twos += 1

print(two_by_twos)

