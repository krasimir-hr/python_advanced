def searching_for_sym_coordinates(matrix, element):
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == searched_symbol:
                return row, col


n = int(input())
matrix = [list(input()) for row in range(n)]

searched_symbol = input()
location = searching_for_sym_coordinates(matrix, searched_symbol)

if location:
    print(location)
else:
    print(f"{searched_symbol} does not occur in the matrix")
