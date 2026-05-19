import numpy as np

z_values = np.array([
    -10,
    -5,
    -2,
    -1,
    0,
    1,
    2,
    5,
    10
])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for value in z_values:
    print(value, ":", sigmoid(value))