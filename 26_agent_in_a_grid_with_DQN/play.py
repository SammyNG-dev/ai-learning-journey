import numpy as np

def create_world(agent_start_pos, goal_pos):
    world = np.zeros((10, 10), dtype=int)
    world[agent_start_pos] = 2
    world[goal_pos] = 3
    return world

def display(world):
    print(world)

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

def normalize_inputs_network(agent_pos):
    row, col = agent_pos
    return np.array([row/9, col/9]).reshape(-1, 2)

agent_row_start = 0
agent_col_start = 0

goal_row = 4
goal_col = 6

start_position = (agent_row_start, agent_col_start)
# goal_position = (goal_row, goal_col)

moves = ["haut", "bas", "droite", "gauche"]

weights = np.array([
    [1.64140779, 0.81376411, 2.0994109,  0.71116192],
    [0.85874397, 2.79184109, 0.64546162, 0.70169316]
    ])

bias = np.array([
    [3.92468714, 4.48380604, 5.32044344, 4.30910285]
    ])

total_moves = 0
goal_positions = ((4, 6), (2, 8))
file = open("sortie_agent_play.txt", "w")

for goal_position in goal_positions:
    file.write(f"Goal position : {goal_position}\n\n")
    grid = create_world(start_position, goal_position)
    current_position = start_position

    while current_position != goal_position:
        inputs_network = normalize_inputs_network(current_position)
        q_values = np.dot(inputs_network, weights) + bias
        q_action_index = np.argmax(q_values)
        action = moves[q_action_index]
        current_position, grid = move_agent(current_position, action, grid)
        total_moves += 1
        file.write(f"Action : {action}\nPosition : {current_position}\n\n")
        print(current_position)

    current_position = start_position
    file.write(f"\nGrille : ({total_moves} mouvement)\n\n{grid}\n\n")

file.close()