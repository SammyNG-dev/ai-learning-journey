import numpy as np

x = np.array([1, 2, 3, 4])
y_true = np.array([3, 5, 7, 9])

a = 0.0   # poids
b = 0.0   # biais
lr = 0.01 # learning rate

for i in range(1000):
    y_pred = a * x + b
    error = y_pred - y_true
    cost = np.mean(error ** 2)
    da = 2 * np.mean(error * x)
    db = 2 * np.mean(error)
    a = a - lr * da
    b = b - lr * db

print("a :", a)
print("b :", b)
print("cost :", cost)
