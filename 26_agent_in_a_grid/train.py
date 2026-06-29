import numpy as np
import random

# 0 = case libre
# 1 = obstacle
# 2 = agent
# 3 = goal

agent_col_start = 0
agent_row_start = 0

goal_row = 8
goal_col = 9

agent_col = agent_col_start
agent_row = agent_row_start

position = (agent_row, agent_col)
goal_position = (goal_row, goal_col)

moves = ["haut", "bas", "droite", "gauche"]

file = open("sortie_agent.txt", "w")

def create_world(agent_start_pos, goal_pos):
    world = np.zeros((10, 10), dtype=int)
    world[agent_start_pos] = 2
    world[goal_pos] = 3
    return world

def display(world):
    print(world)

def random_action(moves_possibilities):
    move = random.choice(moves_possibilities)
    return move

def get_next_position(agent_position, action):
    row, col = agent_position
    if action == "haut":
        return (row - 1, col)
    elif action == "bas":
        return (row + 1, col)
    elif action == "droite":
        return (row, col + 1)
    elif action == "gauche":
        return (row, col - 1)
    return agent_position

def is_next_position_valid(nxt_pos, world):
    row, col = nxt_pos
    if row < 0 or row > len(world) - 1 or col < 0 or col > len(world[0]) - 1:
        return False
    elif world[nxt_pos] == 1:
        return False
    return True

def move_agent(agent_pos, action, world):
    old_position = agent_pos
    next_position = get_next_position(agent_pos, action)
    if is_next_position_valid(next_position, world):
        world[next_position] = 2
        world[old_position] = 0
        return next_position, world
    return agent_pos, world

def is_goal_reached(agent_pos, goal_pos):
    return agent_pos == goal_pos

grid = create_world(position, goal_position)

moves_counter = 0
max_moves = 100

print(f"Grille de départ : {grid}\n")
file.write(f"Grille de départ :\n {grid}\n\n")
print()

while moves_counter < max_moves:
    file.write(f"Position : {position}\n")
    action = random_action(moves)
    print(moves_counter + 1)
    print(action)
    position, grid = move_agent(position, action, grid)
    print(position)
    print(grid)
    moves_counter += 1
    file.write(f"Mouvement {moves_counter} : {action}\n")
    file.write(f"Nouvelle position : {position}\n")
    file.write(f"Nouvelle grille :\n{grid}\n\n")
    if is_goal_reached(position, goal_position):
        print(f"Gagné ! Le tout en moins de {max_moves} mouvements, chapeau bas ! {moves_counter} mouvements.")
        file.write(f"Gagné ! Le tout en moins de {max_moves} mouvements, chapeau bas ! {moves_counter} mouvements.")
        break

if not is_goal_reached(position, goal_position):
    print("Perdu ! Vous (ou plutôt votre agent) avez atteint le nombre maximal de mouvements autorisés !")
    file.write("Perdu ! Vous (ou plutôt votre agent) avez atteint le nombre maximal de mouvements autorisés !")

file.close()

