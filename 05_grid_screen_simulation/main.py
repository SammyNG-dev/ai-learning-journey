import numpy as np

matrix_numpy = np.random.randint(0, 2, size=(10, 10))

print("Matrice NumPy : ")
print(matrix_numpy)
print()
simulated_screen = []
for i in range(0, len(matrix_numpy)):
    simulated_screen.append([])
    for j in range(0, len(matrix_numpy[i])):
        if matrix_numpy[i][j] == 0:
            simulated_screen[i].append(".")
        else:
            simulated_screen[i].append(("#"))
    print(" ".join(simulated_screen[i]))