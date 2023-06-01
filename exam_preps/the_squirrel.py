from collections import deque


def check_valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


collected_hazelnuts = 0
size = int(input())

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, 0),
}

commands = deque(input().split(", "))
matrix = [list(input()) for _ in range(size)]
squirrel_pos = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            squirrel_pos = [row, col]

matrix[squirrel_pos[0]][squirrel_pos[1]] = "*"
died = False

while commands:
    current_command = commands.popleft()
    row = squirrel_pos[0] + directions[current_command][0]
    col = squirrel_pos[1] + directions[current_command][1]
    if not check_valid_index(row, col):
        print("The squirrel is out of the field.")
        died = True
        break

    elif matrix[row][col] == "h":
        collected_hazelnuts += 1
        matrix[row][col] = "*"
        if collected_hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    elif matrix[row][col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        died = True
        break

    squirrel_pos[0] = row
    squirrel_pos[1] = col

if not died and collected_hazelnuts < 3:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazelnuts}")