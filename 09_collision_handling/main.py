import numpy as np

grid = np.random.randint(0, 2, size=(10, 10))

rows = len(grid)
cols = len(grid[0])

player_way = []

# cherche une case vide pour placer le joueur

while True:
    player_row = np.random.randint(0, rows)
    player_column = np.random.randint(0, cols)

    if grid[player_row][player_column] == 0:
        grid[player_row][player_column] = 2
        initial_position = (player_row, player_column)
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
        player_way.append((player_row, player_column))
        grid[player_row][player_column] = 2
        grid[player_row][player_column - 1] = 0

    print(grid)
    print()
print()

if len(player_way) > 0:
    print("Trajet :")
    print("Position initiale :", initial_position)
    print("Mouvements :", player_way)
else:
    print("Le joueur a spawn à côté d'un obstacle, il n'a donc pas bougé.")