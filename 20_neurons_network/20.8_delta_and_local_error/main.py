import numpy as np

y_true = 0

y_pred = np.array([0.5, 0.9, 0.999])

def sigmoid_derivative(s):
    return s * (1 -s)

i = 0

for pred in y_pred:
    i += 1
    error = pred - y_true
    derivative = sigmoid_derivative(pred)
    delta = error * derivative
    print(i, "------------------")
    print("error:", error)
    print("derivative:", derivative)
    print("delta :", delta)
    print()

print(np.exp(1))