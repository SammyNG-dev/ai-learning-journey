import numpy as np

x = np.array([0, 1, 2, 3, 4])
y_true = np.array([0, 0, 0, 1, 1])

a = 0.0
b = 0.0
lr = 0.1

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for i in range(1000):
    score = a * x + b
    y_pred = sigmoid(score)
    error = y_pred - y_true
    cost = np.mean(error ** 2)
    da = np.mean(error * x)
    db = np.mean(error)
    a = a - lr * da
    b = b - lr * db

z = a * x + b
proba = sigmoid(z)
predictions = (proba > 0.5).astype(int)

print("a :", a)
print("b :", b)
print("proba :", proba)
print("predictions :", predictions)