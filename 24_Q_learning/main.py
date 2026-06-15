import numpy as np
import random

q_table = {}
start_position = 0
actions = ["avancer", "reculer"]
compteur = 0
gamma = 0.8
learning_rate = 0.1
epsilon = 0.3

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
        if random_mode_choice < epsilon:
        # l'agent va explorer 30% du temps
            action = random.choice(actions)
            if action == "avancer" and current_position < len(world) - 1:
                current_position += 1
                world[current_position] = 1
                world[current_position - 1] = 0
            elif action == "reculer" and current_position > 0:
                current_position -= 1
                world[current_position] = 1
                world[current_position + 1] = 0
        else:
            q_avancer = q_table.get((current_position, "avancer"), 0)
            q_reculer = q_table.get((current_position, "reculer"), 0)
            q_max = max(q_avancer, q_reculer)
            if q_avancer == q_max and current_position < len(world) - 1:
                action = "avancer"
                current_position += 1
                world[current_position] = 1
                world[current_position - 1] = 0
            elif q_reculer == q_max and current_position > 0:
                action = "reculer"
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

print("Q_table:")
for key, value in sorted(q_table.items()):
    print(key, ":", value)
print("Nombre de tours:", compteur)
