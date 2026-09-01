import numpy as np 
import os
import time
from datetime import datetime
import subprocess

def get_next_position(agent_pos, action):
    row, col = agent_pos
    if action == "haut":
        return (row - 1, col)
    elif action == "bas":
        return (row + 1, col)
    elif action == "droite":
        return (row, col + 1)
    elif action == "gauche":
        return (row, col - 1)
    
def is_position_valid(pos, world):
    row, col = pos
    if row < 0 or row >= len(world) or col < 0 or col >= len(world[0]) or world[pos] == 1:
        return False
    return True

def move_agent(agent_pos, move, grid):
    world = grid.copy()
    old_pos = agent_pos
    new_position = get_next_position(agent_pos, move)
    if is_position_valid(new_position, grid):
        world[new_position] = 2
        world[old_pos] = 0
        return new_position, world
    return agent_pos, world
    

def get_positions_reachables(agent_start, grid):
    positions = [agent_start]
    for coordinates in positions:
        row, col = coordinates
        neighborhood = ((row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col))
        for neighbor in neighborhood:
            if is_position_valid(neighbor, grid) and neighbor not in positions:
                positions.append(neighbor)
    positions.remove(agent_start)
    return tuple(positions)

def get_neighbor_environment(pos, world):
    row, col = pos
    neighbor_environement = []
    neighborhood = ((row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col))
    for neighbor in neighborhood:
        if is_position_valid(neighbor, world):
            neighbor_environement.append(0)
        else:
            neighbor_environement.append(1)
    return tuple(neighbor_environement)

def create_world(agent_start):
    while True:
        grid = np.random.choice([0, 1], size=(10, 10), p=[0.8, 0.2])
        grid[agent_start] = 2
        potentials_goal_positions = get_positions_reachables(agent_start, grid)
        if len(potentials_goal_positions) > 0:
            return grid, potentials_goal_positions

def create_network_inputs(agent_pos, goal_pos, grid, ancient_position, positions_counter, nb_moves, last_action=None,):
    agent_row, agent_col = agent_pos
    goal_row, goal_col = goal_pos
    enviro1, enviro2, enviro3, enviro4 = get_neighbor_environment(agent_pos, grid)
    ancient_position_row, ancient_position_col = ancient_position
    situation_between_agent_and_goal = get_situation_between_agent_and_goal(grid, agent_pos, goal_pos)
    position_counter = min(positions_counter[agent_pos], 10) / 10
    delta_row = (agent_row - goal_row)
    delta_col = (agent_col - goal_col)
    moves_input = min(nb_moves, 100) / 100
    local_inputs = np.array([
        agent_row / 9,
        agent_col / 9,
        goal_row / 9,
        goal_col / 9,
        enviro1,
        enviro2,
        enviro3,
        enviro4,
        ancient_position_row / 9,
        ancient_position_col / 9,
        position_counter,
        moves_input,
        delta_row / 9,
        delta_col / 9
        ])
    if last_action is None:
        encoded_last_action = np.array([0,0,0,0])
    else:
        encoded_last_action = encode_action(last_action)

    concatenated = np.concatenate([local_inputs, grid.flatten(), situation_between_agent_and_goal, encoded_last_action])

    return concatenated.reshape(-1, 124)

def normalize(pos):
    row, col = pos
    return np.array([row/9, col/9]).reshape(-1, 2)

def is_goal_reached(agent_pos, goal_pos):
    return agent_pos == goal_pos

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def encode_action(action):
    if action == "haut":
        return np.array([1,0,0,0])
    elif action == "bas":
        return np.array([0,1,0,0])
    elif action == "droite":
        return np.array([0,0,1,0])
    elif action == "gauche":
        return np.array([0,0,0,1])

def are_aligned(agent_pos, goal_pos):
    agent_row, agent_col = agent_pos
    goal_row, goal_col = goal_pos
    if agent_pos == goal_pos:
        return 0, 0
    return int(agent_row == goal_row), int(agent_col == goal_col)

def is_horizontally_blocked(grid, agent_pos, goal_pos):
    agent_row, agent_col = agent_pos
    goal_row, goal_col = goal_pos
    horizontal_obstacles_counter = 0

    if agent_pos == goal_pos:
        return 0, 0

    if agent_row != goal_row:
        return 0, 0

    start = min(agent_col, goal_col) +1
    end = max(agent_col, goal_col)

    for col in range(start, end):
        if grid[agent_row][col] == 1:
            horizontal_obstacles_counter += 1
    return int(horizontal_obstacles_counter > 0), horizontal_obstacles_counter

def is_vertically_blocked(grid, agent_pos, goal_pos):
    agent_row, agent_col = agent_pos
    goal_row, goal_col = goal_pos
    vertical_obstacles_counter = 0

    if agent_pos == goal_pos:
        return 0, 0

    if agent_col != goal_col:
        return 0, 0

    start = min(agent_row, goal_row) + 1
    end = max(agent_row, goal_row)

    for row in range(start, end):
        if grid[row][agent_col] == 1:
            vertical_obstacles_counter += 1
    return int(vertical_obstacles_counter > 0), vertical_obstacles_counter

def get_situation_between_agent_and_goal(grid, agent_pos, goal_pos):
    horizontally_aligned, vertically_aligned = are_aligned(agent_pos, goal_pos)
    horizontally_blocked, horizontal_obstacles = is_horizontally_blocked(grid, agent_pos, goal_pos)
    vertically_blocked, vertical_obstacles = is_vertically_blocked(grid, agent_pos, goal_pos)

    return np.array([horizontally_aligned, vertically_aligned, horizontally_blocked, horizontal_obstacles  / 9, vertically_blocked, vertical_obstacles / 9])



path_best_model = "./30_grid_generalization/best_model_sigmoid_target_network__02_123_32_16_8_4.npz"
moves_possibilities = ["haut", "bas", "droite", "gauche"]

if os.path.exists(path_best_model):
    path_logs_file = "./30_grid_generalization/sortie_play_sigmoid_target_network__02_123_32_16_8_4.txt"
    logs_file = open(path_logs_file, "w")
    data = np.load(path_best_model)
    weights_hidden1 = data["weights_hidden1"]
    bias_hidden1 = data["bias_hidden1"]
    weights_hidden2 = data["weights_hidden2"]
    bias_hidden2 = data["bias_hidden2"]
    weights_hidden3 = data["weights_hidden3"]
    bias_hidden3 = data["bias_hidden3"]
    weights_final = data["weights_final"]
    bias_final = data["bias_final"]

    np.random.seed(123)

    play_worlds = []

    row_start = 0
    col_start = 0
    start_position = (row_start, col_start)
    total_goal_positions = 0
    worlds_resolved = 0
    total_goals_reached = 0
    total_worlds = 20
    counter = 0

    max_moves = 100

    print(f"Génération de {total_worlds} mondes, Please Wait...")
    time.sleep(2)
    for _ in range(total_worlds):
        base_grid, potential_goal_positions = create_world(start_position)
        play_worlds.append((base_grid, potential_goal_positions))
        total_goal_positions += len(potential_goal_positions)
    for world in play_worlds:
        goals_reached_by_world = 0
        counter += 1
        base_grid, potential_goal_positions = world
        goal_positions_by_world = len(potential_goal_positions)
        logs_file.write(f"Monde numéro {counter}, {len(potential_goal_positions)} positions atteignables :\n\n")
        logs_file.write(f"{base_grid}\n\n")
        positions_reached_counter = {start_position: 1}
        for goal_position in potential_goal_positions:
            grid = base_grid.copy()
            grid[goal_position] = 3
            logs_file.write(f"Position de la cible : {goal_position}\n\n")
            current_position = start_position
            previous_position = start_position
            moves = 0
            last_action = None
            while current_position != goal_position and moves < max_moves:
                old_position = current_position
                inputs_network = create_network_inputs(current_position, goal_position, grid, previous_position, positions_reached_counter, moves, last_action)
                output_hidden1 = sigmoid(np.dot(inputs_network, weights_hidden1) + bias_hidden1)
                output_hidden2 = sigmoid(np.dot(output_hidden1, weights_hidden2) + bias_hidden2)
                output_hidden3 = sigmoid(np.dot(output_hidden2, weights_hidden3) + bias_hidden3)
                q_values = np.dot(output_hidden3, weights_final) + bias_final
                previous_position = old_position
                action_index = np.argmax(q_values)
                action = moves_possibilities[action_index]
                current_position, grid = move_agent(current_position, action, grid)
                position_reached_counter = positions_reached_counter.get(current_position, 0)
                positions_reached_counter[current_position] = position_reached_counter + 1
                moves += 1
                logs_file.write(f"{action} : {old_position} -> {current_position}\n")
                last_action = action
            logs_file.write("\n")
            print(f"Monde {counter} sur {total_worlds}", end="\r")
            if current_position == goal_position:
                goals_reached_by_world += 1
                total_goals_reached += 1
                logs_file.write(f"Cible atteinte en {moves} mouvements.\n\n")
            else:
                logs_file.write("Cible non atteinte\n\n")
        if goals_reached_by_world == goal_positions_by_world:
            worlds_resolved += 1
            logs_file.write(f"Monde {counter} résolu !\n\n")
        else:
            logs_file.write(f"{goals_reached_by_world} positions atteintes sur {goal_positions_by_world}\n\n")

    goals_reached_percent = ((total_goals_reached / total_goal_positions) * 100)

    logs_file.write(f"{goals_reached_percent:.2f}% des cibles atteintes : {total_goals_reached} sur {total_goal_positions}\n")
    logs_file.write(f"{worlds_resolved} mondes résolus\n\n")
    if total_goals_reached == total_goal_positions:
        logs_file.write(f"L'intégralité des {total_worlds} mondes ont été résolus\n\n")

    logs_file.close()
    subprocess.run([
        "paplay",
        "/usr/share/sounds/freedesktop/stereo/complete.oga"
    ])

else:
    print("Impossible de charger les paramètres.")