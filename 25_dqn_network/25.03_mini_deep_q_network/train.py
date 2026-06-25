import numpy as np
import random

np.random.seed(42)

weights = np.random.rand(1, 2) - 0.5
bias = np.random.rand(1, 2) - 0.5

gamma = 0.5
learning_rate = 0.001
epsilon = 1
start_position = 0
moves_distribution = {}

actions = ["avancer", "reculer"]

file = open("dqn_learning_output.txt", "w")

for episode in range(1000):
    world = np.zeros(6, dtype=int)
    goal_position = len(world) - 1
    world[goal_position] = 2
    current_position = start_position
    world[current_position] = 1
    moves_per_episode = 0

    while True:
        old_position = current_position
        action = random.choice(actions)
        random_float = np.random.random()

        if random_float < epsilon:
            if action == "avancer" and current_position < len(world) - 1:
                current_position += 1
                world[old_position] = 0
                world[current_position] = 1

            elif action == "reculer" and current_position > 0:
                current_position -= 1
                world[old_position] = 0
                world[current_position] = 1
        else:
            q_values = np.dot(np.array([[current_position]]), weights) + bias
            action_index = np.argmax(q_values[0])
            action = actions[action_index]
            if action == "avancer" and current_position < len(world) - 1:
                current_position += 1
                world[old_position] = 0
                world[current_position] = 1

            elif action == "reculer" and current_position > 0:
                current_position -= 1
                world[old_position] = 0
                world[current_position] = 1
            
        old_distance = (old_position - goal_position) * -1
        new_distance = (current_position - goal_position) * -1

        if current_position == goal_position:
            reward = 10
        elif new_distance < old_distance:
            reward = 1
        elif new_distance > old_distance:
            reward = 0
        else:
            reward = 0

        x_train_current_position = np.array([[current_position]])
        x_train_old_position = np.array([[old_position]])

        next_q_values = np.dot(x_train_current_position, weights) + bias
        old_q_values = np.dot(x_train_old_position, weights) + bias
        next_q_value = np.max(next_q_values)
        target = reward + gamma * next_q_value
        target_vector = old_q_values.copy()
        action_index = actions.index(action)
        target_vector[0][action_index] = target
        error = old_q_values - target_vector
        cost = np.mean(error ** 2)
        dw = 2 * x_train_old_position * error / len(x_train_old_position)
        db = 2 * np.mean(error, axis=0, keepdims=True)
        weights = weights - learning_rate * dw
        bias = bias - learning_rate * db
        moves_per_episode += 1

        if current_position == goal_position:
            break
    if episode % 100 == 0:
        print(f"Episode {episode} ! Coût : {cost}. Nombre de mouvements : {moves_per_episode}")
    file.write(f"Episode {episode} ! Coût : {cost}. Nombre de mouvements : {moves_per_episode}\n")

    number_moves = moves_distribution.get(moves_per_episode, 0)
    moves_distribution[moves_per_episode] = number_moves + 1
file.write("\n")
for key, value in sorted(moves_distribution.items(), reverse=True):
    print(f"{key} : {value}")
    file.write(f"{key} : {value}\n")


file.close()
print()
print(weights)
print(bias)