import numpy as np

grid = np.random.randint(0, 2, size=(10, 10))

player_row = 5
player_column = 6

grid[player_row][player_column] = 2

print(grid)
print()
print("Action :")
if grid[player_row][player_column + 1] == 1:
    print("SAUTER")
else:
    print("AVANCER")