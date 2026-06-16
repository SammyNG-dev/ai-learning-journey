import numpy as np

np.random.seed(42)

x_train = np.array([0, 1, 2, 3, 4]).reshape(-1, 1)

y_train = np.array([
    [7.05, 5.64],
    [7.56, 5.64],
    [8.20, 6.05],
    [9.00, 6.56],
    [10.00, 7.20]
])

x_test = np.array([[2]])

learning_rate = 0.1

weights = np.random.rand(1, 2) - 0.5
bias = np.random.rand(1, 2) - 0.5

for i in range(200):
    y_pred = np.dot(x_train, weights) + bias
    error = y_pred - y_train
    cost = np.mean(error ** 2)
    if i % 100 == 0:
        print(f"Iteration {i} : {cost}")
    dw1 = 2 * np.dot(x_train.T, error) / len(x_train)
    db1 = 2 * np.mean(error, axis=0, keepdims=True)
    weights = weights - learning_rate * dw1
    bias = bias - learning_rate * db1

prediction = np.dot(x_test, weights) + bias
print(prediction)