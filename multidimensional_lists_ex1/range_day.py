def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if matrix[r][c] == "x":
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return[r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5
matrix = []

targets = 0
targets_hit = 0
targets_hit_pos = []

directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

for row in range(SIZE):
    matrix.append(input().split())

    if "A" in matrix[row]:
        my_position = [row, matrix[row].index("A")]

    targets += matrix[row].count("x")

for _ in range(int(input())):
    command_line = input().split()

    if command_line[0] == "move":
        my_position = move(command_line[1], int(command_line[2]))

    elif command_line[0] == "shoot":
        target_down_pos = shoot(command_line[1])

        if target_down_pos:
            targets_hit_pos.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_pos, sep="\n")
