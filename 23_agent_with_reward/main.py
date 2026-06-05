world_size = 4
goal_position = 3
reward = 0
agent_position = 0
action = "RECULER"
old_position = agent_position
old_distance = goal_position - old_position

# action

if action == "AVANCER" and agent_position < world_size - 1:
    agent_position += 1

if action == "RECULER" and agent_position > 0:
    agent_position -= 1

# nouvelle position

new_position = agent_position
new_distance = goal_position - new_position

if new_position == goal_position:
    reward = 10
elif new_distance < old_distance:
    reward = 1
else:
    reward = 0

if agent_position == goal_position:
    print("Objectif atteint")
else:
    print("Objectif non atteint")

print("Reward:", reward)