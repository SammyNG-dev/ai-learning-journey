import numpy as np

grid = np.random.randint(0, 2, size=(10, 10))

rows = len(grid)
cols = len(grid[0])

# cherche une case vide pour placer le joueur

while True:
    player_row = np.random.randint(0, rows)
    player_column = np.random.randint(0, cols)

    if grid[player_row][player_column] == 0:
        grid[player_row][player_column] = 2
        break

print(grid)
print()

while True:
    if player_column == cols - 1:
        print("BORD")
        break
    elif grid[player_row][player_column+1] == 1:
        print("OBSTACLE")
        break
    else:
        player_column += 1
        grid[player_row][player_column] = 2
        grid[player_row][player_column - 1] = 0

    print(grid)
    print()