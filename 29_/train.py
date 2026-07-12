import numpy as np
import random
from datetime import datetime
import os

run_start = datetime.now()

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

def get_reward(old_agent_position, agent_pos, goal_pos):
    if agent_pos == goal_pos:
        return 20
    elif old_agent_position == agent_pos:
        return -8
    elif is_nearer(old_agent_position, agent_pos, goal_pos):
        return 5
    else:
        return -4

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
learning_rate = 0.0007

successes = 0
fails = 0
episodes = 200000
max_moves = 200
neurons_hidden = 8

file = open(f"sortie_agent_train_{neurons_hidden}_neurons_{episodes}_episodes.txt", "w")

successes_by_goal_position = {}
fails_by_goal_position = {}

total_moves = 0
epsilon = 1
np.random.seed(42)
random.seed(42)
successes = 0
fails = 0
epsilon_min = 0.05
epsilon_decay = (epsilon - epsilon_min) / (episodes * 0.5)


file.write(f"train.py | entrainement à {neurons_hidden} neurones - {episodes} épisodes\n\n")
print(f"train.py | entrainement à {neurons_hidden} neurones - {episodes} épisodes\n")

if os.path.exists(f"./29_/parameters_{neurons_hidden}_neurons_{episodes}_episodes.npz"):
    print("Chargement des paramètres...")
    file.write("Chargement des paramètres...\n\n")
    data = np.load(f"./29_/parameters_{neurons_hidden}_neurones_{episodes}_episodes.npz")
    weights_hidden = data["weights_hidden"]
    bias_hidden = data["bias_hidden"]
    weights_hidden2 = data["weights_hidden2"]
    bias_hidden2 = data["bias_hidden2"]
    weights_final = data["weights_final"]
    bias_final = data["bias_final"]
else:
    print("Inititialisation aléatoire des paramètres...")
    file.write("Inititialisation aléatoire des paramètres...\n\n")
    weights_hidden = np.random.rand(8, neurons_hidden) - 0.5
    bias_hidden = np.random.rand(1, neurons_hidden) - 0.5

    weights_hidden2 = np.random.rand(neurons_hidden, 4) - 0.5
    bias_hidden2 = np.random.rand(1, 4)

    weights_final = np.random.rand(4, 4) - 0.5
    bias_final = np.random.rand(1, 4) - 0.5

rewards_distribution = {}

world = create_world(start_position, start_position)
free_positions = get_free_positions(world)
successes_for_batch_episodes = 0
fails_for_batch_episodes = 0

for episode in range(episodes):
    current_position = start_position
    goal_position = random.choice(free_positions)
    grid = create_world(start_position, goal_position)
    nb_moves = 0
    episode_cost = 0
    nb_update = 0
    while current_position != goal_position and nb_moves < max_moves:
        old_position = current_position
        old_agent_environment = get_agent_environment(old_position, grid)
        old_input_network = create_network_input(old_position, goal_position, old_agent_environment)
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
        current_agent_environment = get_agent_environment(current_position, grid)
        nb_moves += 1
        input_network = create_network_input(current_position, goal_position, current_agent_environment)
        reward = get_reward(old_position, current_position, goal_position)
        rewards = rewards_distribution.get(reward, 0)
        rewards_distribution[reward] = rewards + 1
        total_moves += 1

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

    if current_position == goal_position:
        successes += 1
        successes_for_batch_episodes
    else:
        fails += 1
        fails_for_batch_episodes

    if episode % (episodes / 100) == 0 and episode > 1:
        successes_percent = round(successes / episode * 100, 2)
        fails_percent = round(fails / episode * 100, 2)
        successes_percent_batch = round(successes_for_batch_episodes / (episode / 100) * 100, 2)
        fails_percent_batch = round(fails_for_batch_episodes / (episode / 100) * 100)
        time_now = datetime.now()
        time_from_start = time_now - run_start
        print("\nepisode : ", episode)
        print(f"Temps d'éxécution du script : {calculate_time(time_from_start.seconds)}")
        print("max weights_hidden:", np.max(np.abs(weights_hidden)))
        print("max weights_final:", np.max(np.abs(weights_final)))
        print("max old_output_hidden:", np.max(np.abs(old_output_hidden)))
        print(f"Coût moyen de l'épisode {episode} : {mean_episode_cost}")
        print(f"Nombre de succès : {successes} ({successes_percent}%)")
        print(f"Nombre d'échecs : {fails} ({fails_percent}%)")
        print(f"Succès pour la tranche {episode - (episode / 100)} -> {episode} : {successes_for_batch_episodes} ({successes_percent_batch} %)")
        print(f"Echecs pour la tranche {episode - (episode / 100)} -> {episode} : {fails_for_batch_episodes} ({fails_for_batch_episodes} %)")
        

        file.write(f"\nEpisode : {episode}\n")
        file.write(f"max weights_hidden : {np.max(np.abs(weights_hidden))}\n")
        file.write(f"max weights_final : {np.max(np.abs(weights_final))}\n")
        file.write(f"max old_output_hidden : {np.max(np.abs(old_output_hidden))}\n")
        file.write(f"Moyenne de l'épisode {episode} : {mean_episode_cost}\n")
        file.write(f"Nombre de succès : {successes} ({successes_percent}%)\n")
        file.write(f"Nombre d'échecs : {fails} ({fails_percent}%)\n\n")
    epsilon = max(epsilon_min, epsilon - epsilon_decay)

    

np.savez(
    f"./29_/parameters_{neurons_hidden}_neurons_{episodes}_episodes.npz",
    weights_hidden=weights_hidden,
    bias_hidden=bias_hidden,
    weights_hidden2=weights_hidden2,
    bias_hidden2=bias_hidden2,
    weights_final=weights_final,
    bias_final=bias_final
)

end = datetime.now()
exec_time = end - start

hours = exec_time.seconds // 3600
minutes = (exec_time.seconds % 3600) // 60
seconds = exec_time.seconds % 60
print()
print(f"Temps d'exécution : {hours}h {minutes}min {seconds}s")
file.write(f"\nTemps d'exécution : {hours}h {minutes}min {seconds}\n\n")
for key, value in rewards_distribution.items():
    print(f"Reward : {key} : {value}\n")
    file.write(f"Reward : {key} : {value}")

print(total_moves)
file.close()