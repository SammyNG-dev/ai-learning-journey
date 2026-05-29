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

def sigmoid_derivative(s):
    return s * (1 - s)

for value in z_values:
    sigmoid_value = sigmoid(value)
    derivative = sigmoid_derivative(sigmoid_value)
    print(value, "- Sigmoid :", sigmoid_value, "; Derivée :", derivative)