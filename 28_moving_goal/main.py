import numpy as np
import random
from datetime import datetime

start = datetime.now()

def create_world(agent_start_pos, goal_pos):
    world = np.zeros((10, 10), dtype=int)
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

def get_reward(old_agent_position, agent_pos, goal_pos, world):
    if agent_pos == goal_pos:
        reward = 15
    elif old_agent_position == agent_pos:
        reward = -2
    elif is_nearer(old_agent_position, agent_pos, goal_pos):
        reward = 1
    elif not is_nearer(old_agent_position, agent_pos, goal_pos):
        reward = 0
    return reward

def is_nearer(old_pos, new_pos, goal_pos):
    old_vector = normalize(old_pos) - normalize(goal_pos)
    new_vector = normalize(new_pos) - normalize(goal_pos)
    old_distance = np.linalg.norm(old_vector)
    new_distance = np.linalg.norm(new_vector)
    return new_distance < old_distance

def normalize(agent_pos):
    row, col = agent_pos
    return np.array([row/9, col/9]).reshape(-1, 2)

def create_network_input(agent_pos, goal_pos):
    agent_row, agent_col = agent_pos
    goal_row, goal_col = goal_pos
    return np.array([agent_row/9, agent_col/9, goal_row/9, goal_col/9]).reshape(-1, 4)

def move_goal(goal_current_pos, world):
    random_move = get_random_action(moves)
    goal_old_pos = goal_current_pos
    goal_next_pos = get_next_position(goal_current_pos, random_move)
    if is_next_position_valid(goal_next_pos, world):
        world[goal_next_pos] = 3
        world[goal_old_pos] = 0
        return goal_next_pos, world
    return goal_current_pos, world


agent_row_start = 0
agent_col_start = 0

goal_row = 8
goal_col = 9

start_position = (agent_row_start, agent_col_start)
# goal_position = (goal_row, goal_col)

moves = ["haut", "bas", "droite", "gauche"]

gamma = 0.8
learning_rate = 0.001

successes = 0
fails = 0
trains = 10
episodes = 1000000

file = open(f"sortie_agent", "w")

test_goal_positions = [
    (0, 1),  # juste à côté
    (1, 0),  # juste en dessous
    (1, 1),  # diagonale proche

    (2, 8),  # loin à droite
    (4, 6),  # milieu de la grille
    (5, 2),  # milieu à gauche
    (6, 6),  # diagonale

    (8, 0),  # tout en bas à gauche
    (8, 5),  # bas milieu
    (8, 9),  # position d'entraînement

    (9, 0),  # coin bas gauche
    (9, 4),  # bas
    (9, 9),  # coin opposé
]

successes_by_goal_position = {}
fails_by_goal_position = {}

for run in range(trains):
    run_start = datetime.now()
    epsilon = 1
    np.random.seed(run)
    random.seed(run)
    weights_hidden = np.random.rand(4, 2) - 0.5
    bias_hidden = np.random.rand(1, 2) - 0.5

    weights_final = np.random.rand(2, 4) - 0.5
    bias_final = np.random.rand(1, 4) - 0.5

    for episode in range(episodes):
        current_position = start_position
        while True:
            goal_position = (random.randint(0, 9), random.randint(0,9))
            if goal_position != start_position:
                break

        grid = create_world(start_position, goal_position)

        nb_moves = 0
        while current_position != goal_position:
            if nb_moves > 0 and nb_moves % 5 == 0:
                goal_position, grid = move_goal(goal_position, grid)
            old_position = current_position
            old_input_network = create_network_input(current_position, goal_position)
            random_choice = np.random.random()
            if random_choice < epsilon:
                action = get_random_action(moves)
            else:
                output_hidden = np.dot(old_input_network, weights_hidden) + bias_hidden
                q_values = np.dot(output_hidden, weights_final) + bias_final
                index_action = np.argmax(q_values)
                action = moves[index_action]
            
            current_position, grid = move_agent(current_position, action, grid)
            nb_moves += 1
            input_network = create_network_input(current_position, goal_position)
            reward = get_reward(old_position, current_position, goal_position, grid)

            next_output_hidden = np.dot(input_network, weights_hidden) + bias_hidden
            next_q_values = np.dot(next_output_hidden, weights_final) + bias_final
            old_output_hidden = np.dot(old_input_network, weights_hidden) + bias_hidden
            old_q_values = np.dot(old_output_hidden, weights_final) + bias_final
            next_q_value = np.max(next_q_values)
            target_vector = old_q_values.copy()
            target = reward
            if not is_goal_reached(current_position, goal_position):
                target += gamma * next_q_value
            action_index = moves.index(action)
            target_vector[0][action_index] = target
            error = old_q_values - target_vector
            delta_hidden = np.dot(error, weights_final.T)
            cost = np.mean(error ** 2)
            dw_hidden = 2 * np.dot(old_input_network.T, delta_hidden)  / len(old_input_network)
            db_hidden = 2 * np.mean(delta_hidden, axis=0, keepdims=True)
            dw_final = 2 * np.dot(old_output_hidden.T, error) / len(old_output_hidden)
            db_final = 2 * np.mean(error, axis=0, keepdims=True)
            weights_hidden = weights_hidden - learning_rate * dw_hidden
            bias_hidden = bias_hidden - learning_rate * db_hidden
            weights_final = weights_final - learning_rate * dw_final
            bias_final = bias_final - learning_rate * db_final
            percent = (episode + 1) / episodes * 100
            print(f"Entrainement {run + 1}/{trains} | Episode {episode}/{episodes} ({round(percent, 2)}%)", end="\r")
        epsilon = max(0.05, epsilon - 0.0009)

    # test après entrainement  
    for test_goal_position in test_goal_positions:
        current_position = start_position
        grid = create_world(start_position, test_goal_position)
        test_moves = 0
        max_test_moves = 100
        while current_position != test_goal_position and test_moves < max_test_moves:
            input_network = create_network_input(current_position, test_goal_position)
            output_hidden = np.dot(input_network, weights_hidden) + bias_hidden
            next_q_values = np.dot(output_hidden, weights_final) + bias_final
            action_index = np.argmax(next_q_values)
            action = moves[action_index]
            current_position, grid = move_agent(current_position, action, grid)
            test_moves += 1
        # print()
        if current_position == test_goal_position:
            successes += 1
            successes_for_one_position = successes_by_goal_position.get((test_goal_position, "Succès"), 0)
            successes_by_goal_position[(test_goal_position, "Succès")] = successes_for_one_position + 1
        else:
            fails += 1
            fails_for_one_position = fails_by_goal_position.get((test_goal_position, "Echecs"), 0)
            fails_by_goal_position[(test_goal_position, "Echecs")] = fails_for_one_position +1
    run_end = datetime.now()
    run_time = run_end - run_start
    run_hours = run_time.seconds // 3600
    run_minutes = (run_time.seconds % 3600) // 60
    run_seconds = run_time.seconds % 60
    print(f"\nEntrainement {run+1} terminé. Temps écoulé : {run_hours}h {run_minutes}mn {run_seconds}s")

percent_successes = round(successes / (trains * len(test_goal_positions)) *100, 2)
percent_fails = round(fails / (trains * len(test_goal_positions)) * 100, 2)
print(f"\n{trains} entraînements, {len(test_goal_positions)} positions de test ({episodes} episodes) : \n\nSuccès : {successes} ({percent_successes}%)\nEchecs : {fails} ({percent_fails}%)")
file.write(f"\n{trains} entraînements, {len(test_goal_positions)} positions de test : \n\nSuccès : {successes} ({percent_successes}%)\nEchecs : {fails} ({percent_fails}%)")

print()
print("Succès :")
file.write("Succès\n")
for key, value in successes_by_goal_position.items():
    percent = value / trains *100
    print(f"Pour la position {key[0]} : {value} {key[1]} ({round(percent, 2)}%)")
    file.write(f"Pour la position {key[0]} : {value} {key[1]} ({round(percent, 2)}%)\n")
print()
print("Echecs :")
file.write("\nEchecs\n\n")
for key, value in fails_by_goal_position.items():
    percent = value / trains *100
    print(f"Pour la position {key[0]} : {value} {key[1]} ({round(percent, 2)}%)")
    file.write(f"Pour la position {key[0]} : {value} {key[1]} ({round(percent, 2)}%)\n")

end = datetime.now()
exec_time = end - start

hours = exec_time.seconds // 3600
minutes = (exec_time.seconds % 3600) // 60
seconds = exec_time.seconds % 60
print()
print(f"Temps d'exécution : {hours}h {minutes}min {seconds}s")
file.write(f"\nTemps d'exécution : {hours}h {minutes}min {seconds}s")

file.close()