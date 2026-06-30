import numpy as np
import random

np.random.seed(42)

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

def get_reward(old_agent_position, agent_pos, goal_pos):
    if agent_pos == goal_pos:
        reward = 10
    elif is_nearer(old_agent_position, agent_pos, goal_pos):
        reward = 1
    elif not is_nearer(old_agent_position, agent_pos, goal_pos):
        reward = 0
    return reward

def is_nearer(old_pos, new_pos, goal_pos):
    old_vector = normalize_inputs_network(old_pos) - normalize_inputs_network(goal_pos)
    new_vector = normalize_inputs_network(new_pos) - normalize_inputs_network(goal_pos)
    old_distance = np.linalg.norm(old_vector)
    new_distance = np.linalg.norm(new_vector)
    return new_distance < old_distance

def normalize_inputs_network(agent_pos):
    row, col = agent_pos
    return np.array([row/9, col/9]).reshape(-1, 2)

agent_row_start = 0
agent_col_start = 0

goal_row = 8
goal_col = 9

start_position = (agent_row_start, agent_col_start)
goal_position = (goal_row, goal_col)

moves = ["haut", "bas", "droite", "gauche"]
weights = np.random.rand(2, 4) - 0.5
bias = np.random.rand(1, 4) - 0.5

gamma = 0.8
epsilon = 1
learning_rate = 0.01
total_moves = 0

file = open("sortie_agent.txt", "w")

for episode in range(1000):
    current_position = start_position
    grid = create_world(start_position, goal_position)
    moves_by_episode = 0

    while current_position != goal_position:
        old_position = current_position
        old_input_network = normalize_inputs_network(current_position)
        random_choice = np.random.random()
        if random_choice < epsilon:
            action = random_action(moves)
        else:
            q_values = np.dot(old_input_network, weights) + bias
            index_action = np.argmax(q_values)
            action = moves[index_action]
        
        current_position, grid = move_agent(current_position, action, grid)
        input_network = normalize_inputs_network(current_position)
        reward = get_reward(old_position, current_position, goal_position)

        next_q_values = np.dot(input_network, weights) + bias
        old_q_values = np.dot(np.array(old_input_network), weights) + bias
        next_q_value = np.max(next_q_values)
        target_vector = old_q_values.copy()
        target = reward
        if not is_goal_reached(current_position, goal_position):
            target += gamma * next_q_value
        action_index = moves.index(action)
        target_vector[0][action_index] = target
        error = old_q_values - target_vector
        cost = np.mean(error ** 2)
        dw = 2 * np.dot(old_input_network.T, error) / len(old_input_network)
        db = 2 * np.mean(error, axis=0, keepdims=True)
        weights = weights - learning_rate * dw
        bias = bias - learning_rate * db
        moves_by_episode += 1
    total_moves += moves_by_episode
    print(f"Episode {episode +1} : coût = {cost}\nMouvements = {moves_by_episode}\n")
    print(f"poids : {weights}\nBias : {bias}\n")
    file.write(f"Episode {episode + 1} : coût = {cost}\nMouvements = {moves_by_episode}\n")
    file.write(f"poids : {weights}\nBiais : {bias}\n")
    epsilon = max(0.05, epsilon - 0.0009)
    file.write(f"Epsilon = {epsilon}\n\n")
    
print()
print(f"Total des mouvements de tous les épisodes : {total_moves}.")
file.write(f"\nTotal des mouvements de tous les épisodes : {total_moves}\n.")
file.write(f"epsilon final = {epsilon}")
file.close()
print(epsilon)

print(weights)
print()
print(bias)