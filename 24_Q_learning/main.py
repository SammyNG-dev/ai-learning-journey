"""q_table = {
    (2, "avancer"): 8
}

position = 1
action = "avancer"
reward = 0
next_position = 2

learning_rate = 0.1
gamma = 0.9

q_avancer_next = q_table.get((next_position, "avancer"), 0)
q_reculer_next = q_table.get((next_position, "reculer"), 0)

next_q_value = max(q_avancer_next, q_reculer_next)

q_value = q_table.get((position, action), 0)

q_value = q_value + learning_rate * (reward + gamma * next_q_value - q_value)

q_table[(position, action)] = q_value

print(q_table)
"""

import numpy as np
import random

q_table = {}
start_position = 0
actions = ["avancer", "reculer"]
compteur = 0
gamma = 0.8
learning_rate = 0.1

# fonction de calcul de la q_value à mettre à jour

def compute_q_value(q, lr, rwd, gma, nxt_q):
    return q + lr * (rwd + gma * nxt_q - q)

for episode in range(1000):
    world = np.zeros(6, dtype=int)
    current_position = start_position
    goal_position = len(world) - 1
    world[start_position] = 1
    world[goal_position] = 2
    while True:
        old_position = current_position
        random_mode_choice = np.random.random()
        if random_mode_choice < 1:
        # l'agent va explorer 100% du temps
            action = random.choice(actions)
            if action == "avancer" and current_position < len(world) - 1:
                current_position += 1
                world[current_position] = 1
                world[current_position - 1] = 0
            elif action == "reculer" and current_position > 0:
                current_position -= 1
                world[current_position] = 1
                world[current_position + 1] = 0
        compteur += 1

        if current_position == goal_position:
            reward = 10
        elif old_position < current_position:
            reward = 1
        elif old_position > current_position:
            reward = 0
        else:
            reward = 0

        old_q_value = q_table.get((old_position, action), 0)
        next_avancer = q_table.get((current_position, "avancer"), 0)
        next_reculer = q_table.get((current_position, "reculer"), 0)
        next_q_value = max(next_avancer, next_reculer)
        q_value = compute_q_value(old_q_value, learning_rate, reward, gamma, next_q_value)
        q_table[(old_position, action)] = q_value

        if current_position == goal_position:
            break

for key, value in q_table.items():
    print(key, ":", value)
print("Nombre de tours:", compteur)