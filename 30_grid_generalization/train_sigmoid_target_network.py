import numpy as np 
import random
import os
import time
from datetime import datetime

start_time = datetime.now()
date_time = start_time.strftime("%d-%m-%Y_%Hh%Mm%Ss")

debug = True

if debug:
    np.random.seed(42)
    random.seed(42)

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

"""def create_world(agent_start):
    while True:
        grid = np.random.choice([0, 1]goku vs hit db super vf, size=(10, 10), p=[0.8, 0.2])
        grid[agent_start] = 2
        potentials_goal_positions = get_positions_reachables(agent_start, grid)
        if len(potentials_goal_positions) > 0:
            goal_position = random.choice(potentials_goal_positions)
            grid[goal_position] = 3
            return grid, goal_position"""

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
    input_moves = min(nb_moves, 100) / 100
    delta_row = (agent_row - goal_row)
    delta_col = (agent_col - goal_col)
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
        input_moves,
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

def is_closer(old_pos, new_pos, goal_pos):
    old_vector = normalize(old_pos) - normalize(goal_pos)
    new_vector = normalize(new_pos) - normalize(goal_pos)
    old_distance = np.linalg.norm(old_vector)
    new_distance = np.linalg.norm(new_vector)
    return new_distance < old_distance

def get_reward(old_agent_position, agent_pos, goal_pos, two_moves_ago, positions_counter):
    if agent_pos == goal_pos:
        reward = 60
    elif old_agent_position == agent_pos:
        reward = -10
    elif two_moves_ago == agent_pos:
        reward = -6.5
    elif is_closer(old_agent_position, agent_pos, goal_pos):
        reward = 3.5
    else:
        reward = 0
    if positions_counter[agent_pos] > 1 and agent_pos != goal_pos:
        reward -= 0.1
    return reward
    
def is_goal_reached(agent_pos, goal_pos):
    return agent_pos == goal_pos

def calculate_time(secs):
    days = secs // 3600 // 24
    hours = (secs // 3600) % 24
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    return f"{days}jours {hours}heures {minutes}minutes {seconds}secondes"

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(s):
    return s * (1 - s)

def relu(z):
    return np.maximum(0, z)

def relu_derivative(r):
    return (r > 0).astype(int)

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

moves_possibilities = ["haut", "bas", "droite", "gauche"]

model_file_name = "best_model_sigmoid_target_network__02_123_32_16_8_4.npz"

parameters_file_path = f"./30_grid_generalization/{model_file_name}"
outputs_logs_file_path = f"./30_grid_generalization/sortie_entrainement_sigmoid_target_network_02_123_32_16_8_4_{date_time}"
file = open(outputs_logs_file_path, "w")



if os.path.exists(parameters_file_path):
    print("Chargements des paramètres...")
    file.write("Chargement des paramètres...\n")
    print(f"Nom du fichier : {model_file_name}\n")
    file.write(f"Nom du fichier : {model_file_name}\n\n")
    data = np.load(parameters_file_path)
    weights_hidden1 = data["weights_hidden1"]
    bias_hidden1 = data["bias_hidden1"]
    weights_hidden2 = data["weights_hidden2"]
    bias_hidden2 = data["bias_hidden2"]
    weights_hidden3 = data["weights_hidden3"]
    bias_hidden3 = data["bias_hidden3"]
    weights_final = data["weights_final"]
    bias_final = data["bias_final"]
    last_best_score = data["best_score"]
    run_number = data["run_number"]
    print(f"Meilleur score à battre : {last_best_score}")
    file.write(f"Meilleur score à battre : {last_best_score}\n")
    best_model_mean_moves = data["best_model_mean_moves"]
    time.sleep(1)


    # pour le target network

    target_weights_hidden1 = weights_hidden1.copy()
    target_bias_hidden1 = bias_hidden1.copy()
    target_weights_hidden2 = weights_hidden2.copy()
    target_bias_hidden2 = bias_hidden2.copy()
    target_weights_hidden3 = weights_hidden3.copy()
    target_bias_hidden3 = bias_hidden3.copy()
    target_weights_final = weights_final.copy()
    target_bias_final = bias_final.copy()
else:
    print("Initialisation aléatoire des paramètres...\n")
    file.write("Initialisation aléatoire des paramètres...\n")
    print(f"Nom du fichier : {parameters_file_path}")
    file.write(f"Nom du fichier : {parameters_file_path}\n\n")
    time.sleep(1)
    weights_hidden1 = np.random.rand(124, 32) - 0.5
    bias_hidden1 = np.random.rand(1, 32) - 0.5
    weights_hidden2 = np.random.rand(32, 16) - 0.5
    bias_hidden2 = np.random.rand(1, 16) - 0.5
    weights_hidden3 = np.random.rand(16, 8) - 0.5
    bias_hidden3 = np.random.rand(1, 8) - 0.5
    weights_final = np.random.rand(8, 4) - 0.5
    bias_final = np.random.rand(1, 4) - 0.5
    last_best_score = 0
    best_model_mean_moves = float("inf")
    run_number = 0

    # pour le target network

    target_weights_hidden1 = weights_hidden1.copy()
    target_bias_hidden1 = bias_hidden1.copy()
    target_weights_hidden2 = weights_hidden2.copy()
    target_bias_hidden2 = bias_hidden2.copy()
    target_weights_hidden3 = weights_hidden3.copy()
    target_bias_hidden3 = bias_hidden3.copy()
    target_weights_final = weights_final.copy()
    target_bias_final = bias_final.copy()

row_start = 0
col_start = 0
start_position = (row_start, col_start)
episodes = 100000
lr = 1e-4
gamma = 0.8
epsilon = 1
epsilon_min = 0.15
epsilon_decay = (epsilon - epsilon_min) / (episodes * 0.75)
max_steps = 200
successes = 0
successes_by_batch = 0
fails = 0
fails_by_batch = 0
best_score = last_best_score
total_cost = 0
total_steps = 0
total_q_min = 0
total_q_max = 0
total_q_abs_mean = 0
q_count = 0
delta_q = 0
rewards_distribution = {}
best_mean_moves = best_model_mean_moves
target_by_reward = {}
target_count_by_reward = {}
training_worlds = []
test_worlds = []
total_test_goals_positions = 0
number_of_run = run_number
number_of_run += 1
old_q_delta_mean = 0
np.random.seed(123)
random.seed(123)

print("Génération de 20 mondes de test.")
for _ in range(20):
    test_base_grid, test_potential_goal_positions = create_world(start_position)
    total_test_goals_positions += len(test_potential_goal_positions)
    test_worlds.append((test_base_grid, test_potential_goal_positions))

file.write(f"Entrainement du {date_time}\n")
file.write(f"Architecture : 122 -> 32 -> 16 -> 8 -> 4\n")
file.write(f"Learning rate : {lr}\n")
file.write(f"Gamma : {gamma}\n")
file.write(f"{episodes} épisodes.\n")
file.write(f"Epsilon initial : {epsilon}\n")
file.write(f"Epsilon decay : {epsilon_decay}\n")
file.write(f"Epsilon min : {epsilon_min}\n\n")
file.write(f"Run numéro : {number_of_run}\n\n")

for episode in range(episodes):
        positions_reached_counter = {start_position:1}
        base_grid, potential_goal_positions = create_world(start_position)
        grid = base_grid.copy()
        goal_position = random.choice(potential_goal_positions)
        grid[goal_position] = 3
        current_position = start_position
        previous_position = start_position
        last_action = None
        steps = 0
        while current_position != goal_position and steps < max_steps:
            position_two_moves_ago = previous_position
            old_position = current_position
            old_inputs_network = create_network_inputs(old_position, goal_position, grid, previous_position, positions_reached_counter, steps, last_action)
            if np.random.random() < epsilon:
                action = random.choice(moves_possibilities)
            else:
                output_exploit_hidden1 = sigmoid(np.dot(old_inputs_network, weights_hidden1) + bias_hidden1)
                output_exploit_hidden2 = sigmoid(np.dot(output_exploit_hidden1, weights_hidden2) + bias_hidden2)
                output_exploit_hidden3 = sigmoid(np.dot(output_exploit_hidden2, weights_hidden3) + bias_hidden3)
                output_exploit_final = np.dot(output_exploit_hidden3, weights_final) + bias_final
                action_index = np.argmax(output_exploit_final)
                action = moves_possibilities[action_index]

            last_action = action
            current_position, grid = move_agent(current_position, action, grid)
            previous_position = old_position

            position_reached_counter = positions_reached_counter.get(current_position, 0)
            positions_reached_counter[current_position] = position_reached_counter + 1

            steps += 1
            current_inputs_network = create_network_inputs(current_position, goal_position, grid, previous_position, positions_reached_counter, steps, last_action)
            reward = get_reward(old_position, current_position, goal_position, position_two_moves_ago, positions_reached_counter)
            episode_finished = (is_goal_reached(current_position, goal_position))
            action_index = moves_possibilities.index(action)

            # forward next

            next_output_hidden1 = sigmoid(np.dot(current_inputs_network, target_weights_hidden1) + target_bias_hidden1)
            next_output_hidden2 = sigmoid(np.dot(next_output_hidden1, target_weights_hidden2) + target_bias_hidden2)
            next_output_hidden3 = sigmoid(np.dot(next_output_hidden2, target_weights_hidden3) + target_bias_hidden3)
            next_q_values = np.dot(next_output_hidden3, target_weights_final) + target_bias_final
            next_q_value = np.max(next_q_values)

            # forward old

            z_old_output_hidden1 = np.dot(old_inputs_network, weights_hidden1) + bias_hidden1
            old_output_hidden1 = sigmoid(z_old_output_hidden1)
            z_old_output_hidden2 = np.dot(old_output_hidden1, weights_hidden2) + bias_hidden2
            old_output_hidden2 = sigmoid(z_old_output_hidden2)
            z_old_output_hidden3 = np.dot(old_output_hidden2, weights_hidden3) + bias_hidden3
            old_output_hidden3 = sigmoid(z_old_output_hidden3)
            old_q_values = np.dot(old_output_hidden3, weights_final) + bias_final

            total_q_min += np.min(old_q_values)
            total_q_max += np.max(old_q_values)
            total_q_abs_mean += np.mean(np.abs(old_q_values))
            q_count += 1
            delta_q += np.max(old_q_values) - np.min(old_q_values)

            target_vector = old_q_values.copy()
            target = reward
            if not episode_finished:
                target += gamma * next_q_value
            target_by_reward[reward] = target_by_reward.get(reward, 0) + target
            target_count_by_reward[reward] = target_count_by_reward.get(reward, 0) + 1
            target_vector[0][action_index] = target
            error = old_q_values - target_vector
                
            cost = np.mean(error ** 2)
            total_cost += cost
            delta_hidden3 = np.dot(error, weights_final.T) * sigmoid_derivative(old_output_hidden3)
            delta_hidden2 = np.dot(delta_hidden3, weights_hidden3.T) * sigmoid_derivative(old_output_hidden2)
            delta_hidden1 = np.dot(delta_hidden2, weights_hidden2.T) * sigmoid_derivative(old_output_hidden1)
            dw_hidden1 = np.dot(old_inputs_network.T, delta_hidden1) / len(old_inputs_network)
            db_hidden1 = np.mean(delta_hidden1, axis=0, keepdims=True)
            dw_hidden2 = np.dot(old_output_hidden1.T, delta_hidden2) / len(old_output_hidden2)
            db_hidden2 = np.mean(delta_hidden2, axis=0, keepdims=True)
            dw_hidden3 = np.dot(old_output_hidden2.T, delta_hidden3) / len(old_output_hidden2)
            db_hidden3 = np.mean(delta_hidden3, axis=0, keepdims=True)
            dw_final = np.dot(old_output_hidden3.T, error) / len(old_output_hidden3)
            db_final = np.mean(error, axis=0, keepdims=True)
            weights_hidden1 = weights_hidden1 - lr * dw_hidden1
            bias_hidden1 = bias_hidden1 - lr * db_hidden1
            weights_hidden2 = weights_hidden2 - lr * dw_hidden2
            bias_hidden2 = bias_hidden2 - lr * db_hidden2
            weights_hidden3 = weights_hidden3 - lr * dw_hidden3
            bias_hidden3 = bias_hidden3 - lr * db_hidden3
            weights_final = weights_final - lr * dw_final
            bias_final = bias_final - lr * db_final

            reward_stat = rewards_distribution.get(reward, 0)
            rewards_distribution[reward] = reward_stat + 1
            total_steps += 1
            if total_steps % 1000 == 0:
                target_weights_hidden1 = weights_hidden1.copy()
                target_bias_hidden1 = bias_hidden1.copy()
                target_weights_hidden2 = weights_hidden2.copy()
                target_bias_hidden2 = bias_hidden2.copy()
                target_weights_hidden3 = weights_hidden3.copy()
                target_bias_hidden3 = bias_hidden3.copy()
                target_weights_final = weights_final.copy()
                target_bias_final = bias_final.copy()
        epsilon = max(epsilon_min, epsilon - epsilon_decay)
        episodes_percent = (episode + 1) / episodes * 100
        instant_time = datetime.now()
        timedelta = instant_time - start_time
        print(f"Episode {episode+1}/{episodes} ({episodes_percent:.2f}%). epsilon : {epsilon:.4f}. Temps écoulé : {calculate_time(int(timedelta.total_seconds()))}", end="\r")
        if current_position == goal_position:
            successes += 1
            successes_by_batch += 1
        else:
            fails += 1
            fails_by_batch += 1
        if episode % (episodes // 100) == 0 and episode > 1:
            general_successes_percent = successes / (episode + 1) * 100
            successes_percent_by_batch = successes_by_batch / (episodes // 100) * 100
            general_fails_percent = fails / (episode + 1) * 100
            fails_percent_by_batch = fails_by_batch / (episodes // 100) * 100
            cost_mean = total_cost / episode
            steps_mean = total_steps / episode
            q_delta_mean = delta_q / q_count
            print(f"\nNombre de succès : {successes}. ({general_successes_percent:.2f}%)")
            print(f"Nombre d'échecs : {fails}. ({general_fails_percent:.2f}%)")
            print(f"Succès pour la tranche {int(episode - episodes // 100)} -> {episode} : {successes_by_batch}. ({successes_percent_by_batch:.2f}%)")
            print(f"Echecs pour la tranche {int(episode - episodes // 100)} -> {episode} : {fails_by_batch}. ({fails_percent_by_batch:.2f}%)")
            print(f"Nombre moyen de mouvements par épisode : {steps_mean}")
            print(f"Coût moyen par épisode : {cost_mean:.4f}")
            print(f"Q min moyen : {total_q_min / q_count:.4f}")
            print(f"Q max moyen : {total_q_max / q_count:.4f}")
            print(f"Moyenne de l'écart entre Q min et Q max : {q_delta_mean} (Diff : {q_delta_mean - old_q_delta_mean})")
            old_q_delta_mean = q_delta_mean
            print(f"|Q| moyen : {total_q_abs_mean / q_count:.4f}")
            print(f"Meilleur score déterministe : {best_score}/{total_test_goals_positions}")
            print("Target moyen par récompense :")
            for reward, target_sum in target_by_reward.items():
                target_mean = target_sum / target_count_by_reward[reward]
                print(f"Reward : {reward} -> target moyen : {target_mean:.4f}")
            print()
            print("Distribution des récompenses : ")
            for reward, count in rewards_distribution.items():
                print(f"{reward} : {count}.")
            print("\n")

            file.write(f"Nombre de succès : {successes}. ({general_successes_percent}%)\n")
            file.write(f"Nombre d'échecs : {fails}. ({general_fails_percent}%)\n")
            file.write(f"Succès pour la tranche {int(episode - episodes // 100)} -> {episode} : {successes_by_batch}. ({successes_percent_by_batch:.2f}%)\n")
            file.write(f"Echecs pour la tranche {int(episode - episodes // 100)} -> {episode} : {fails_by_batch}. ({fails_percent_by_batch:.2f}%)\n")
            file.write(f"Nombre moyen de mouvements par épisode : {steps_mean:.4f}\n")
            file.write(f"Coût moyen par épisode : {cost_mean:.4f}\n")
            file.write(f"Q min moyen : {total_q_min / q_count:.4f}\n")
            file.write(f"Q max moyen : {total_q_max / q_count:.4f}\n")
            file.write(f"|Q| moyen : {total_q_abs_mean / q_count:.4f}\n")
            file.write(f"Moyenne de l'écart entre Q min et Q max : {delta_q / q_count:.4f}\n")
            file.write("Target moyen par récompense :\n")
            file.write(f"Meilleur score déterministe : {best_score}/{total_test_goals_positions}\n")
            for reward, target_sum in target_by_reward.items():
                target_mean = target_sum / target_count_by_reward[reward]
                file.write(f"Reward {reward} -> target moyen : {target_mean:.4f}\n")
            file.write("Distribution des récompenses : \n")
            for reward, count in rewards_distribution.items():
                file.write(f"{reward} : {count}\n")
            file.write("\n")
            successes_by_batch = 0
            fails_by_batch = 0

        if episode % (episodes // 100) == 0 and episode > 0:
            score = 0
            max_test_moves = 100
            total_test_moves = 0
            for test_base_grid, test_potential_goal_positions in test_worlds:
                test_positions_reached_counter = {start_position: 1}
                for test_goal_position in test_potential_goal_positions:
                    test_moves = 0
                    test_grid = test_base_grid.copy()
                    test_previous_position = start_position
                    test_current_position = start_position
                    test_last_action = None
                    test_grid[test_goal_position] = 3
                    mean_moves = 0
                    while test_current_position != test_goal_position and test_moves < max_test_moves:
                        test_old_position = test_current_position
                        test_position_two_moves_ago = test_previous_position
                        test_network_input = create_network_inputs(test_current_position, test_goal_position, test_grid, test_position_two_moves_ago, test_positions_reached_counter, test_moves, test_last_action)
                        test_output_hidden_1 = sigmoid(np.dot(test_network_input, weights_hidden1) + bias_hidden1)
                        test_output_hidden_2 = sigmoid(np.dot(test_output_hidden_1, weights_hidden2) + bias_hidden2)
                        test_output_hidden_3 = sigmoid(np.dot(test_output_hidden_2, weights_hidden3) + bias_hidden3)
                        test_q_values = np.dot(test_output_hidden_3, weights_final) + bias_final
                        test_move_index = np.argmax(test_q_values)
                        test_move = moves_possibilities[test_move_index]
                        test_last_action = test_move
                        test_current_position, test_grid = move_agent(test_current_position, test_move, test_grid)
                        test_position_reached_counter = test_positions_reached_counter.get(test_current_position, 0)
                        test_positions_reached_counter[test_current_position] = test_position_reached_counter + 1
                        test_previous_position = test_old_position
                        test_moves += 1
                        total_test_moves += 1
                    if test_current_position == test_goal_position:
                        score += 1
            mean_moves = total_test_moves / total_test_goals_positions
            if score > best_score:
                best_score = score
                best_mean_moves = mean_moves
                print(f"\nNouveau score à battre : {best_score}/{total_test_goals_positions}. Sauvegarde des paramètres...")
                file.write(f"\nNouveau score à battre : {best_score}/{total_test_goals_positions}. Sauvegarde des paramètres...\n\n")
                np.savez(
                    parameters_file_path,
                    weights_hidden1=weights_hidden1,
                    bias_hidden1=bias_hidden1,
                    weights_hidden2=weights_hidden2,
                    bias_hidden2=bias_hidden2,
                    weights_final=weights_final,
                    weights_hidden3=weights_hidden3,
                    bias_hidden3=bias_hidden3,
                    bias_final=bias_final,
                    best_score=best_score,
                    best_model_mean_moves=best_mean_moves,
                    run_number=number_of_run
                    )
            elif score == best_score and mean_moves < best_mean_moves:
                best_mean_moves = mean_moves
                print(f"Nouveau meilleur modèle : {best_mean_moves}")
                file.write(f"Nouveau meilleur modèle : {best_mean_moves}\n\n")
                np.savez(
                    parameters_file_path,
                    weights_hidden1=weights_hidden1,
                    bias_hidden1=bias_hidden1,
                    weights_hidden2=weights_hidden2,
                    bias_hidden2=bias_hidden2,
                    weights_final=weights_final,
                    weights_hidden3=weights_hidden3,
                    bias_hidden3=bias_hidden3,
                    bias_final=bias_final,
                    best_score=best_score,
                    best_model_mean_moves=best_mean_moves,
                    run_number=number_of_run
                )

script_end_time = datetime.now()
script_execution_time = script_end_time - start_time
print(f"\n\nFin de l'entraînement. Meilleur score déterministe : {best_score}/{total_test_goals_positions}. Temps d'execution : {calculate_time(int(script_execution_time.total_seconds()))}")
print(f"Coût moyen par épisode : {total_cost / episodes}")
file.write(f"Fin de l'entraînement.\nMeilleur score déterministe : {best_score}/{total_test_goals_positions}. Temps d'execution : {calculate_time(int(script_execution_time.total_seconds()))}\n")
file.write(f"Coût moyen par épisode : {total_cost / episodes}")
file.close()