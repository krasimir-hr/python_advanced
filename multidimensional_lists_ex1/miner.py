def find_miner_pos():
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "s":
                return row, col


def check_valid_index(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True


n = int(input())
commands = input().split()

matrix = [input().split() for _ in range(n)]

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

miner_row, miner_col = find_miner_pos()
matrix[miner_row][miner_col] = "*"

total_coal = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "c":
            total_coal += 1

player_dead = False
collected_coal = 0

for command in commands:
    miner_movement_row, miner_movement_col = miner_row + directions[command][0], miner_col + directions[command][1]

    if check_valid_index(miner_movement_row, miner_movement_col):
        miner_row, miner_col = miner_movement_row, miner_movement_col

    if matrix[miner_row][miner_col] == "c":
        collected_coal += 1
        total_coal -= 1
        matrix[miner_row][miner_col] = "*"

    if total_coal == 0:
        print(f"You collected all coal! ({miner_row}, {miner_col})")
        break

    if matrix[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        player_dead = True
        break

if total_coal > 0 and not player_dead:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")
