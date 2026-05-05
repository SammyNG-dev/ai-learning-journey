import numpy as np

x = np.array([[0, 0],
             [0, 1],
             [1, 0],
             [1, 1]])

y = np.array([0, 0, 0, 1])

w = np.array([0.0, 0.0])
b = 0.0
lr = 0.1

def sigmoid(z):
    return 1/(1+np.exp(-z))

for i in range(1000):
    z = np.dot(x, w) + b
    y_pred = sigmoid(z)
    error = y_pred - y
    cost = np.mean(error ** 2)
    dw = np.dot(x.T, error) / len(x)
    db = np.mean(error)
    w = w - lr * dw
    b = b - lr * db


predictions = (y_pred > 0.5).astype(int)
print("w:", w)
print("b:", b)
print("cost:", cost)
print("y_pred:", y_pred)
print("predictions:", predictions)
print("error:", error)

print(x.T)

