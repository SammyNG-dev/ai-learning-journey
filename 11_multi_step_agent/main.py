import numpy as np

grid = np.random.randint(0, 2, size=(10, 10))

len_rows = len(grid)
len_cols = len(grid[0])

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
player_way = []

def has_free_neighboor(np_array, row, col, rows, cols):
    for dr, dc in directions:
        new_r = row + dr
        new_c = col + dc

        if 0 <= new_r < rows and 0 <= new_c < cols:
            if np_array[new_r][new_c] == 0:
                return True
    return False

while True:
    player_row = np.random.randint(0, len_rows)
    player_col = np.random.randint(0, len_cols)

    if grid[player_row][player_col] == 0 and has_free_neighboor(grid, player_row, player_col, len_rows, len_cols):
        grid[player_row][player_col] = 2
        initial_position = (player_row, player_col)
        break

print(grid)
print()

for _ in range(10):
    move = np.random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    if move == "UP":
        if player_row == 0:
            continue
        elif grid[player_row-1][player_col] == 1:
            continue
        else:
            player_row -= 1
            player_way.append((player_row, player_col))
            grid[player_row][player_col] = 2
            grid[player_row + 1][player_col] = 0

    elif move == "DOWN":
        if player_row == len_rows - 1 :
            continue
        elif grid[player_row + 1][player_col] == 1:
            continue
        else:
            player_row += 1
            player_way.append((player_row, player_col))
            grid[player_row][player_col] = 2
            grid[player_row - 1][player_col] = 0

    elif move == "LEFT":
        if player_col == 0:
            continue
        elif grid[player_row][player_col - 1] == 1:
            continue
        else:
            player_col -= 1
            player_way.append((player_row, player_col))
            grid[player_row][player_col] = 2
            grid[player_row][player_col + 1] = 0
    
    elif move == "RIGHT":
        if player_col == len_cols - 1:
            continue
        elif grid[player_row][player_col + 1] == 1:
            continue
        else:
            player_col += 1
            player_way.append((player_row, player_col))
            grid[player_row][player_col] = 2
            grid[player_row][player_col - 1] = 0

    print("Mouvement choisi :", move)
    print("Grille après action :")
    print(grid)
    print()
    
print("Position initiale :", initial_position)
print(player_way)
print(f"Le joueur a fait {len(player_way)} mouvements.")