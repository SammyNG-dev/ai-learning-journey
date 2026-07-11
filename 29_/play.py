import numpy as np
import os


def create_world(agent_start_pos, goal_pos, original_world):
    world = original_world.copy()
    world[agent_start_pos] = 2
    world[goal_pos] = 3
    return world

def display(world):
    print(world)

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
    if row < 0 or row >= len(world) or col < 0 or col >= len(world[0]) or world[nxt_pos] == 1:
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

def normalize(agent_pos):
    row, col = agent_pos
    return np.array([row/9, col/9]).reshape(-1, 2)

def wall_or_outsite(row, col, world):
    if row < 0  or col < 0 or row >= len(world) or col >= len(world[0]):
        return 1
    if world[row][col] == 1:
        return 1
    return 0

def get_agent_environment(agent_pos, world):
    row, col = agent_pos
    up = wall_or_outsite(row - 1, col, world)
    down = wall_or_outsite(row + 1, col, world)
    left = wall_or_outsite(row, col - 1, world)
    right = wall_or_outsite(row, col + 1, world)
    return (up, down, left, right) 

def create_network_input(agent_pos, goal_pos, agent_enviro):
    agent_row, agent_col = agent_pos
    goal_row, goal_col = goal_pos
    up, down, left, right = agent_enviro
    return np.array([agent_row/9, agent_col/9, goal_row/9, goal_col/9, up, down, left, right]).reshape(-1, 8)

def get_free_positions(world):
    free_positions = []
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] == 0:
                free_positions.append((i, j))
    return free_positions

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

moves = ["haut", "bas", "droite", "gauche"]

episodes = 75000

neurons = 8


if not os.path.exists(f"./29_/parameters_{neurons}_neurons_{episodes}_episodes.npz"):
    print("Impossible de charger les paramètres !")
else:
    file = open(f"./29_/sortie_play_{neurons}_neurons_{episodes}_episodes.txt", "w")
    print("Chargement des paramètres...")
    print()
    data = np.load(f"./29_/parameters_{neurons}_neurons_{episodes}_episodes.npz")
    weights_hidden = data["weights_hidden"]
    bias_hidden = data ["bias_hidden"]
    weights_final = data["weights_final"]
    bias_final = data["bias_final"]


    row_start = 0
    col_start = 0

    original_grid = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    ], dtype=int)

    start_position = (row_start, col_start)
    test_goal_positions = get_free_positions(original_grid)
    test_goal_positions.remove(start_position)

    file.write(f"play.py | {neurons} neurones {episodes} épisodes\n\n")
    successes = 0
    fails = 0

    runs = 0
    for goal_position in test_goal_positions:
        runs += 1
        path = []
        actions_by_test = []
        q_values = []
        grid = create_world(start_position, goal_position, original_grid)
        current_position = start_position
        nb_moves = 0
        print(f"\nRun {runs} :\n")
        file.write(f"Run {runs}\n\n")
        while current_position != goal_position and nb_moves < 100:
            agent_environement = get_agent_environment(current_position, grid)
            normalized_current_position = create_network_input(current_position, goal_position, agent_environement)
            z_hidden = np.dot(normalized_current_position, weights_hidden) + bias_hidden
            output_hidden = sigmoid(z_hidden)
            output_final = np.dot(output_hidden, weights_final) + bias_final
            action_index = np.argmax(output_final)
            action = moves[action_index]
            print(f"Position : {current_position}\nQ-Values : {output_final}\nAction : {action}\n")
            file.write(f"Position : {current_position}\nQ-Values : {output_final}\nAction : {action}\n\n")
            current_position, grid = move_agent(current_position, action, grid)
            nb_moves += 1
            actions_by_test.append(action)
        if current_position == goal_position:
            successes += 1
            file.write(f"Position de la cible atteinte : {goal_position} !\n")
            print(f"Position de la cible atteinte : {goal_position} !")
        else:
            fails += 1
            file.write(f"Position de la cible non atteinte : {goal_position} !\n")
            print(f"Position de la cible non atteinte : {goal_position}")
        file.write(f"Nombre total de mouvement : {nb_moves}\n\n")
        print(f"Nombre total de mouvement : {nb_moves}\n")
        file.write("-------------------------------------------\n\n")
    successes_percent = successes/len(test_goal_positions) * 100
    print(f"Succès : {successes} ({round(successes_percent, 2)}%)")
    file.write(f"Succès : {successes} ({successes_percent}%)\n")
    fails_percent = fails / len(test_goal_positions) * 100
    print(f"Echecs : {fails} ({round(fails_percent, 2)}%)")
    file.write(f"Echecs : {fails} ({fails_percent}%)")

    file.close()
    # os.remove(f"./29_/parameters_{neurons}_neurons_{episodes}_episodes.npz")