import numpy as np
import random
from datetime import datetime
import os
import time
import matplotlib.pyplot as plt

run_start = datetime.now()
date_time = run_start.strftime("%d-%m-%Y_%Hh%Mm%Ss")
start = datetime.now()

def create_world(agent_start_pos, goal_pos):
    world = np.array([
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
    
    world[agent_start_pos] = 2
    world[goal_pos] = 3
    return world

def display(world):
    print(world)

def get_random_action(moves_possibilities):
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

def is_goal_reached(agent_pos, goal_pos):
    return agent_pos == goal_pos

def get_reward(old_agent_position, agent_pos, goal_pos, two_moves_ago):
    if agent_pos == goal_pos:
        return 25
    elif old_agent_position == agent_pos:
        return -8.2
    elif two_moves_ago == agent_pos:
        return - 10.2
    elif is_nearer(old_agent_position, agent_pos, goal_pos):
        return 5.8
    else:
        return -4.2

def is_nearer(old_pos, new_pos, goal_pos):
    old_vector = normalize(old_pos) - normalize(goal_pos)
    new_vector = normalize(new_pos) - normalize(goal_pos)
    old_distance = np.linalg.norm(old_vector)
    new_distance = np.linalg.norm(new_vector)
    return new_distance < old_distance

def normalize(agent_pos):
    row, col = agent_pos
    return np.array([row/9, col/9]).reshape(-1, 2)

def wall_or_outsite(row, col, world):
    if row == -1 or col == -1 or row >= len(world) or col >= len(world[0]):
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

def create_network_input(agent_pos, goal_pos, agent_enviro, entire_grid, two_moves_ago):
    agent_row, agent_col = agent_pos
    goal_row, goal_col = goal_pos
    up, down, left, right = agent_enviro
    two_moves_ago_row, two_moves_ago_col = two_moves_ago
    locale_information = np.array([
        agent_row/9,
        agent_col/9,
        goal_row/9,
        goal_col/9,
        up,
        down,
        left,
        right,
        two_moves_ago_row /9,
        two_moves_ago_col /9
    ])

    concatenated = np.concatenate([locale_information, entire_grid])

    return concatenated.reshape(1, 110)

def get_free_positions(world):
    free_positions = []
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] == 0:
                free_positions.append((i, j))
    return free_positions

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(s):
    return s * (1 - s)

def calculate_time(secs):
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    return f"{hours}h {minutes}mn {seconds}s"

agent_row_start = 0
agent_col_start = 0

start_position = (agent_row_start, agent_col_start)

moves = ["haut", "bas", "droite", "gauche"]

gamma = 0.8
learning_rate = 0.00001

successes = 0
fails = 0
episodes = 500000
max_moves = 200
neurons_hidden = 16

file = open(f"./29_sortie_entrainement_{date_time}.txt", "w")

successes_by_goal_position = {}
fails_by_goal_position = {}

total_moves = 0
moves_by_batch = 0
np.random.seed(42)
random.seed(42)
successes = 0
fails = 0
epsilon = 0.05
epsilon_min = 0.05
epsilon_decay = (epsilon - epsilon_min) / (episodes * 0.5)
evaluation_interval = 10

path_best_model_file = "./29_grid_agent/best_optimal_model.npz"


file.write(f"train.py | entrainement du {date_time}\n")
print(f"train.py | entrainement du {date_time}\n")

if os.path.exists(path_best_model_file):
    print("Chargement des paramètres...")
    file.write("Chargement des paramètres...\n\n")
    data = np.load(path_best_model_file)
    weights_hidden = data["weights_hidden"]
    bias_hidden = data["bias_hidden"]
    weights_hidden2 = data["weights_hidden2"]
    bias_hidden2 = data["bias_hidden2"]
    weights_final = data["weights_final"]
    bias_final = data["bias_final"]
    last_best_score = data["last_best_score"]
    last_min_mean_test_moves = data["min_mean_test_moves"]
    if last_best_score != 58:
        print(f"\nScore à battre : {last_best_score} !")
    print(f"Moyenne de mouvements dans les tests déterministes à battre : {last_min_mean_test_moves:.2f}\n")
    time.sleep(2)
else:
    print("Inititialisation aléatoire des paramètres...")
    file.write("Inititialisation aléatoire des paramètres...\n\n")
    time.sleep(2)
    weights_hidden = np.random.rand(110, neurons_hidden) - 0.5
    bias_hidden = np.random.rand(1, neurons_hidden) - 0.5

    weights_hidden2 = np.random.rand(neurons_hidden, 8) - 0.5
    bias_hidden2 = np.random.rand(1, 8)

    weights_final = np.random.rand(8, 4) - 0.5
    bias_final = np.random.rand(1, 4) - 0.5

    last_best_score = 0

    last_min_mean_test_moves = float("inf")



rewards_distribution = {}

cost_history = []
episode_history = []

plt.ion()

figure, axis = plt.subplots()

cost_line, = axis.plot([], [])

axis.set_title("Évolution du coût pendant l'entraînement")
axis.set_xlabel("Épisodes")
axis.set_ylabel("Coût moyen")
axis.grid()

cost_for_batch = 0

graph_interval = 100

world = create_world(start_position, start_position)
free_positions = get_free_positions(world)
successes_for_batch_episodes = 0
fails_for_batch_episodes = 0
best_score = last_best_score
best_train_score = 0
min_mean_test_moves = last_min_mean_test_moves

for episode in range(episodes):
    current_position = start_position
    goal_position = random.choice(free_positions)
    grid = create_world(start_position, goal_position)
    nb_moves = 0
    episode_cost = 0
    nb_update = 0
    previous_position = start_position
    while current_position != goal_position and nb_moves < max_moves:
        position_tow_moves_ago = previous_position
        old_position = current_position
        old_agent_environment = get_agent_environment(old_position, grid)
        old_input_network = create_network_input(old_position, goal_position, old_agent_environment, grid.flatten(), position_tow_moves_ago)
        random_choice = np.random.random()
        if random_choice < epsilon:
            action = get_random_action(moves)
        else:
            z_hidden = np.dot(old_input_network, weights_hidden) + bias_hidden
            output_hidden = sigmoid(z_hidden)
            z_hidden2 = np.dot(output_hidden, weights_hidden2) + bias_hidden2
            output_hidden2 = sigmoid(z_hidden2)
            q_values = np.dot(output_hidden2, weights_final) + bias_final
            index_action = np.argmax(q_values)
            action = moves[index_action]
        
        current_position, grid = move_agent(current_position, action, grid)
        previous_position = old_position
        current_agent_environment = get_agent_environment(current_position, grid)
        nb_moves += 1
        input_network = create_network_input(current_position, goal_position, current_agent_environment, grid.flatten(), old_position)
        reward = get_reward(old_position, current_position, goal_position, position_tow_moves_ago)
        rewards = rewards_distribution.get(reward, 0)
        rewards_distribution[reward] = rewards + 1
        total_moves += 1
        moves_by_batch += 1

        current_z_hidden = np.dot(input_network, weights_hidden) + bias_hidden
        current_output_hidden = sigmoid(current_z_hidden)
        current_z_hidden2 = np.dot(current_output_hidden, weights_hidden2) + bias_hidden2
        current_output_hidden2 = sigmoid(current_z_hidden2)
        next_q_values = np.dot(current_output_hidden2, weights_final) + bias_final
        old_z_hidden = np.dot(old_input_network, weights_hidden) + bias_hidden
        old_output_hidden = sigmoid(old_z_hidden)
        old_z_hidden2 = np.dot(old_output_hidden, weights_hidden2) + bias_hidden2
        old_output_hidden2 = sigmoid(old_z_hidden2)
        old_q_values = np.dot(old_output_hidden2, weights_final) + bias_final
        next_q_value = np.max(next_q_values)
        target_vector = old_q_values.copy()
        target = reward
        episode_finished = (
            is_goal_reached(current_position, goal_position)
            or nb_moves >= max_moves
        )
        if not episode_finished:
            target += gamma * next_q_value
        action_index = moves.index(action)
        target_vector[0][action_index] = target
        error = old_q_values - target_vector
        delta_hidden2 = np.dot(error, weights_final.T) * sigmoid_derivative(old_output_hidden2)
        delta_hidden = np.dot(delta_hidden2, weights_hidden2.T) * sigmoid_derivative(old_output_hidden)
        cost = np.mean(error ** 2)
        episode_cost += cost
        nb_update += 1
        dw_hidden = 2 * np.dot(old_input_network.T, delta_hidden)  / len(old_input_network)
        db_hidden = 2 * np.mean(delta_hidden, axis=0, keepdims=True)
        dw_hidden2 = 2 * np.dot(old_output_hidden.T, delta_hidden2) / len(old_output_hidden)
        db_hidden2 = 2 * np.mean(delta_hidden2, axis=0, keepdims=True)
        dw_final = 2 * np.dot(old_output_hidden2.T, error) / len(old_output_hidden2)
        db_final = 2 * np.mean(error, axis=0, keepdims=True)
        weights_hidden = weights_hidden - learning_rate * dw_hidden
        bias_hidden = bias_hidden - learning_rate * db_hidden
        weights_hidden2 = weights_hidden2 - learning_rate * dw_hidden2
        bias_hidden2 = bias_hidden2 - learning_rate * db_hidden2
        weights_final = weights_final - learning_rate * dw_final
        bias_final = bias_final - learning_rate * db_final
        percent = (episode + 1) / episodes * 100
        print(f"Episode {episode}/{episodes} ({round(percent, 2)}%). epsilon : {epsilon}", end="\r")
    mean_episode_cost = episode_cost / nb_update
    cost_for_batch += mean_episode_cost

    if (episode + 1) % graph_interval == 0:
        mean_batch_cost = cost_for_batch / graph_interval

        episode_history.append(episode + 1)
        cost_history.append(mean_batch_cost)

        cost_line.set_data(episode_history, cost_history)

        axis.relim()
        axis.autoscale_view()

        figure.canvas.draw()
        figure.canvas.flush_events()

        cost_for_batch = 0


    if current_position == goal_position:
        successes += 1
        successes_for_batch_episodes += 1
    else:
        fails += 1
        fails_for_batch_episodes += 1

    if episode % (episodes / 100) == 0 and episode > 1:
        successes_percent = round(successes / episode * 100, 2)
        fails_percent = round(fails / episode * 100, 2)
        successes_percent_batch = round(successes_for_batch_episodes / (episodes / 100) * 100, 2)
        fails_percent_batch = round(fails_for_batch_episodes / (episodes / 100) * 100, 2)
        time_now = datetime.now()
        time_from_start = time_now - run_start
        mean_moves_by_batch = moves_by_batch / (episodes / 100)
        print(f"\nepisode : {episode} - epsilon : {epsilon} - learning rate : {learning_rate}")
        print("max weights_hidden:", np.max(np.abs(weights_hidden)))
        print("max weights_final:", np.max(np.abs(weights_final)))
        print("max old_output_hidden:", np.max(np.abs(old_output_hidden)))
        print(f"Coût moyen de l'épisode {episode} : {mean_episode_cost}")
        print(f"Moyenne de mouvements pour la tranche {int(episode - (episodes / 100))} -> {episode} : {mean_moves_by_batch:.2f}")
        print(f"Nombre de succès : {successes} ({successes_percent}%)")
        print(f"Nombre d'échecs : {fails} ({fails_percent}%)")
        print(f"Succès pour la tranche {int(episode - (episodes / 100))} -> {episode} : {successes_for_batch_episodes} ({successes_percent_batch} %)")
        print(f"Echecs pour la tranche {int(episode - (episodes / 100))} -> {episode} : {fails_for_batch_episodes} ({fails_percent_batch} %)")
        print(f"Temps écoulé depuis le début : {calculate_time(time_from_start.seconds)}\n")
        

        file.write(f"\nepisode : {episode} - epsilon : {epsilon} - learning rate : {learning_rate}")
        file.write(f"max weights_hidden : {np.max(np.abs(weights_hidden))}\n")
        file.write(f"max weights_final : {np.max(np.abs(weights_final))}\n")
        file.write(f"max old_output_hidden : {np.max(np.abs(old_output_hidden))}\n")
        file.write(f"Coût moyen de l'épisode {episode} : {mean_episode_cost}\n")
        file.write(f"Moyenne de mouvements pour la tranche {int(episode - (episode / 100))} -> {episode} : {mean_moves_by_batch:.2f}\n\n")
        file.write(f"Nombre de succès : {successes} ({successes_percent}%)\n")
        file.write(f"Nombre d'échecs : {fails} ({fails_percent}%)\n")
        file.write(f"Succès pour la tranche {int(episode - (episodes / 100))} -> {episode} : {successes_for_batch_episodes} ({successes_percent_batch} %)\n")
        file.write(f"Echecs pour la tranche {int(episode - (episodes / 100))} -> {episode} : {fails_for_batch_episodes} ({fails_for_batch_episodes} %)\n")
        file.write(f"Temps écoulé depuis le début : {calculate_time(time_from_start.seconds)}\n")

        fails_for_batch_episodes = 0
        successes_for_batch_episodes = 0
        moves_by_batch = 0
    epsilon = max(epsilon_min, epsilon - epsilon_decay)

    if (episode + 1) % evaluation_interval == 0:
        score = 0
        total_test_moves = 0
        for test_goal_position in free_positions:
            max_test_moves = 100
            test_grid = create_world(start_position, test_goal_position)
            test_current_position = start_position
            test_moves = 0
            test_previous_position = start_position
            while test_current_position != test_goal_position and test_moves < max_test_moves:
                test_position_two_moves_ago = test_previous_position
                test_old_position = test_current_position
                test_agent_enviro = get_agent_environment(test_current_position, test_grid)
                test_input_network = create_network_input(test_current_position, test_goal_position, test_agent_enviro, test_grid.flatten(), test_position_two_moves_ago)
                test_output_hidden = sigmoid(np.dot(test_input_network, weights_hidden) + bias_hidden)
                test_output_hidden2 = sigmoid(np.dot(test_output_hidden, weights_hidden2) + bias_hidden2)
                test_q_values= np.dot(test_output_hidden2, weights_final) + bias_final
                action_index = np.argmax(test_q_values)
                action = moves[action_index]
                test_current_position, test_grid = move_agent(test_current_position, action, test_grid)
                test_previous_position = test_old_position
                test_moves += 1
            if test_current_position == test_goal_position:
                score +=1
                total_test_moves += test_moves
        
        mean_test_moves = total_test_moves / len(free_positions)

        if score > best_score:
            best_score = score
            print(f"\nNouveau meilleur modèle : {best_score}/{len(free_positions)} obtenu à l'épisode {episode}\n")
            file.write(f"\nNouveau meilleur modèle : {best_score}/{len(free_positions)} obtenu à l'épisode {episode}\n\n")
            np.savez(
                f"./29_grid_agent/best_score_model.npz",
                weights_hidden=weights_hidden,
                bias_hidden=bias_hidden,
                weights_hidden2=weights_hidden2,
                bias_hidden2=bias_hidden2,
                weights_final=weights_final,
                bias_final=bias_final,
                last_best_score=best_score
            )
        if score > best_train_score:
            best_train_score = score

        if score == len(free_positions) and mean_test_moves < min_mean_test_moves:
            min_mean_test_moves = mean_test_moves
            file.write(f"\nModèle le plus optimal obtenu à l'épisode {episode} avec un moyenne de {min_mean_test_moves:.2f} mouvements\n")
            print(f"\nModèle le plus optimal obtenu à l'épisode {episode} avec un moyenne de {min_mean_test_moves:.2f} mouvements\n")
            np.savez(
                f"./29_grid_agent/best_optimal_model.npz",
                weights_hidden=weights_hidden,
                bias_hidden=bias_hidden,
                weights_hidden2=weights_hidden2,
                bias_hidden2=bias_hidden2,
                weights_final=weights_final,
                bias_final=bias_final,
                last_best_score=score,
                min_mean_test_moves=min_mean_test_moves
            )

            
        

end = datetime.now()
exec_time = end - start

hours = exec_time.seconds // 3600
minutes = (exec_time.seconds % 3600) // 60
seconds = exec_time.seconds % 60
print()
print(f"Temps d'exécution : {hours}h {minutes}min {seconds}s")
print(f"Meilleur score de l'entrainement : {best_train_score}")
print(f"Nombre total de mouvements : {total_moves} | Moyenne : {total_moves / episodes}")
file.write(f"\nTemps d'exécution : {hours}h {minutes}min {seconds}\n")
file.write(f"Meilleur score de l'entrainement : {best_train_score}\n")
file.write(f"Nombre total de mouvements : {total_moves} | Moyenne : {total_moves / episodes}\n\n")
for key, value in rewards_distribution.items():
    print(f"Reward : {key} : {value}")
    file.write(f"Reward : {key} : {value}\n")

print(total_moves)
plt.ioff()
plt.show()
file.close()