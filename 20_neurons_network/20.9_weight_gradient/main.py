import numpy as np

x_values = np.array([0.1, 1, 5])

delta_values = np.array([
    0.001,
    0.1,
    1
])

for x, delta in zip(x_values, delta_values):
    dw = x * delta
    print(dw)
    print()