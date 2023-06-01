from collections import deque


def check_valid_index(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True


def print_matrix():
    [print(*row, sep=" ") for row in matrix]


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

explosion_directions = {
    "nw": (-1, -1),
    "n": (-1, 0),
    "ne": (-1, 1),
    "e": (0, 1),
    "se": (1, 1),
    "s": (1, 0),
    "sw": (1, -1),
    "w": (0, -1),
}

bomb_positions = []
bombs_coordinates = input().split()
for coordinate in bombs_coordinates:
    bombs_pos = coordinate.split(",")
    bomb_row = bombs_pos[0]
    bomb_col = bombs_pos[1]
    bomb_positions.append([bomb_row, bomb_col])

bomb_positions = deque(bomb_positions)

while bomb_positions:
    current_bomb_coordinates = bomb_positions.popleft()
    current_bomb_row = int(current_bomb_coordinates[0])
    current_bomb_col = int(current_bomb_coordinates[1])

    current_bomb_value = matrix[current_bomb_row][current_bomb_col]

    if current_bomb_value <= 0:
        continue

    for direction in explosion_directions:
        to_bomb_row, to_bomb_col = current_bomb_row + explosion_directions[direction][0], \
                                   current_bomb_col + explosion_directions[direction][1]
        if check_valid_index(to_bomb_row, to_bomb_col) and matrix[to_bomb_row][to_bomb_col] > 0:
            bomb_row = to_bomb_row
            bomb_col = to_bomb_col
            matrix[bomb_row][bomb_col] -= current_bomb_value
    matrix[current_bomb_row][current_bomb_col] = 0

alive_cells_count = 0
alive_cells_sum = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells_count += 1
            alive_cells_sum += matrix[row][col]

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
print_matrix()
