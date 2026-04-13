import numpy as np

grid = np.random.randint(0, 2, size=(10, 10))

rows = len(grid)
cols = len(grid[0])
final_position = None

# cherche une position valide pour le joueur

while True:
    player_row = np.random.randint(0, rows)
    player_col = np.random.randint(0, cols)

    if grid[player_row][player_col] == 0:
        grid[player_row][player_col] = 2
        initial_position = (player_row, player_col)
        break

print("Grille initiale :")
print(grid)
print()
random_move = np.random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
print("Input :", random_move)

if random_move == "UP":
    if player_row == 0:
        print("Mouvement impossible : BORD HAUT ATTEINT")
    elif grid[player_row - 1][player_col] == 1:
        print("Mouvement impossible : OBSTACLE")
    else:
        player_row -= 1
        final_position = (player_row, player_col)
        grid[player_row][player_col] = 2
        grid[player_row + 1][player_col] = 0
elif random_move == "DOWN":
    if player_row == rows - 1:
        print("Mouvement impossible : BORD BAS ATTEINT")
    elif grid[player_row + 1][player_col] == 1:
        print("Mouvement impossible : OBSTACLE")
    else:
        player_row += 1
        final_position = (player_row, player_col)
        grid[player_row][player_col] = 2
        grid[player_row - 1][player_col] = 0
elif random_move == "LEFT":
    if player_col == 0:
        print("Mouvement impossible : BORD GAUCHE ATTEINT")
    elif grid[player_row][player_col - 1] == 1:
        print("Mouvement impossible : OBSTACLE")
    else:
        player_col -= 1
        final_position = (player_row, player_col)
        grid[player_row][player_col] = 2
        grid[player_row][player_col + 1] = 0
elif random_move == "RIGHT":
    if player_col == cols -1:
        print("Mouvement impossible : BORD DROIT ATTEINT")
    elif grid[player_row][player_col + 1] == 1:
        print("Mouvement impossible : OBSTACLE")
    else:
        player_col += 1
        final_position = (player_row, player_col)
        grid[player_row][player_col] = 2
        grid[player_row][player_col - 1] = 0


print()
print("Position initiale :", initial_position)
print()
if final_position:
    print("Position atteinte :", final_position)
    print()
    print("Grille après mouvement :")
    print()
    print(grid)