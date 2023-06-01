size = int(input())
matrix = [input().split() for _ in range(size)]

collected_tea = 0
alice_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "A":
            alice_pos = [row, col]
            matrix[alice_pos[0]][alice_pos[1]] = "*"

while True:
    if collected_tea >= 10:
        break

    direction = input()
    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break

    if matrix[row][col].isdigit():
        collected_tea += int(matrix[row][col])

    alice_pos = [row, col]
    matrix[row][col] = "*"

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

print(*[' '.join(row) for row in matrix], sep='\n')

