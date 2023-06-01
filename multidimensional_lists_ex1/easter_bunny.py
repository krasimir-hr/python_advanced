size = int(input())
matrix = [input().split() for _ in range(size)]

bunny_pos = []
best_path = []

best_direction = None
max_collected_eggs = 0


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_pos = [row, col]

for direction, position in directions.items():
    row, col = bunny_pos[0] + position[0], bunny_pos[1] + position[1]

    current_path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break
        collected_eggs += int(matrix[row][col])
        current_path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = current_path

print(best_direction)
print(*best_path, sep="\n")
print(max_collected_eggs)