import numpy as np

# poids obtenus par l'entraînement avec 30% d'exploration

# weights = np.array([[3.44047412, 1.32404378]])
# bias = np.array([[2.00344968, 0.36810529]])

# poids obtenus par l'entraînement avec 100% d'exploration

weights = np.array([[2.35696178, 0.74986446]])
bias = np.array([[2.63628269, 1.01232505]])
start_position = 0

actions = ["avancer", "reculer"]
world = np.zeros(6, dtype=int)
goal_position = len(world) - 1
world[goal_position] = 2
current_position = start_position
world[current_position] = 1
moves = 0

while current_position != goal_position:
    old_position = current_position
    q_values = np.dot(np.array([[current_position]]), weights) + bias
    action_index = np.argmax(q_values[0])
    action = actions[action_index]
    if action == "avancer" and current_position < len(world) - 1:
        current_position += 1
    elif action == "reculer" and current_position > 0:
        current_position -= 1

    world[old_position] = 0
    world[current_position] = 1

    moves += 1
    message = f"Action : {action} | Position : {current_position}"
    if current_position == goal_position:
        print(f"{message} | Gagné !!!!!")
    else:
        print(message)
    print(world)
print(f"Nombre de mouvements : {moves}")