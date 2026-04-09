import numpy as np

array = np.random.randint(0, 2, size=(10, 10))

one = np.argwhere(array == 1)

print("Obstacles trouves aux positions :")
for positions in one:
    print(positions)