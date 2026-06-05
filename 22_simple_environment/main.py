world_size = 4
agent_position = 2
goal_position = 3
action = "AVANCER"

print("Agent :", agent_position)
print("Goal :", goal_position)

if action == "AVANCER" and agent_position < world_size - 1:
    agent_position += 1

if action == "RECULER" and agent_position > 0:
    agent_position -= 1

if agent_position == goal_position:
    print("Objectif atteint")
else:
    print("Objectif non atteint")

print("Position :", agent_position)