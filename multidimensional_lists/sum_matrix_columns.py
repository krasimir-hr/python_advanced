rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

for column in range(columns):
    column_sum = 0
    for row in range(rows):
        column_sum += matrix[row][column]
    print(column_sum)