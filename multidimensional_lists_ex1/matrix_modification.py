n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command_line = input().split()
    if command_line[0] == "END":
        break

    command, row, col, value = command_line[0], int(command_line[1]), int(command_line[2]), int(command_line[3])

    if not (0 <= row < n and 0 <= col < n):
        print("Invalid coordinates")
    elif command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")

