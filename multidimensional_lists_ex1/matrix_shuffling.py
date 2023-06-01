def print_matrix(curr_matrix):
    for nested_lst in curr_matrix:
        print(*nested_lst, sep=" ")


def check_valid_indices(position, length):
    if position >= length or position < 0:
        return False
    return True


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for y in range(rows)]


while True:
    command = input()
    if command == "END":
        break
    tokens = command.split()

    if "swap" in tokens and len(tokens) == 5:
        x1 = int(tokens[1])
        y1 = int(tokens[2])
        x2 = int(tokens[3])
        y2 = int(tokens[4])

        if check_valid_indices(x1, rows) and check_valid_indices(y1, cols)\
                and check_valid_indices(x2, rows) and check_valid_indices(y2, cols):
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            print_matrix(matrix)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

