import numpy as np

y_true = np.array([3, -1, 2])
y_pred = np.array([2.5, 0, 2])

error = y_pred - y_true

cost = np.mean(error ** 2)

print("y_true :", y_true)
print()
print("y_pred :", y_pred)
print()
print("error :", error)
print()
print("cost :", cost)