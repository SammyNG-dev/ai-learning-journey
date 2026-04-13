import numpy as np

grid = np.random.randint(0, 2, size=(10, 10))

player_row = 2
player_column = 4

grid[player_row][player_column] = 2

print(grid)

if grid[player_row][player_column+1] == 0:
    player_column += 1
    grid[player_row][player_column] = 2
    grid[player_row][player_column-1] = 0

print()
print(grid)
