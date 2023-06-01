def move(row, col, direction):
    r = row + directions[direction][0]
    c = col + directions[direction][1]

    if 0 <= r < rows and 0 <= c < cols:
        if matrix[r][c] == "O":
            return False
        else:
            return r, c
    else:
        return False



rows, cols = [int(x) for x in input().split()]

matrix = []
player_pos = []

moves = 0
touched_opps = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "B":
            player_pos = [row, col]
            matrix[row][col] = "-"
row, col = player_pos[0], player_pos[1]

while True:
    direction = input()
    if direction == "Finish":
        break

    if not move(row, col, direction):
        continue
    else:
        row, col = move(row, col, direction)

    if matrix[row][col] == "P":
        touched_opps += 1
        matrix[row][col] = "-"
    moves += 1
    if touched_opps == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched_opps} Moves made: {moves}")
