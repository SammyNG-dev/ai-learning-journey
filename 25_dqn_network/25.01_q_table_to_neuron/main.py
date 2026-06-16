import numpy as np

np.random.seed(42)

x_train = np.array([0, 1, 2, 3, 4]).reshape(-1, 1)

y_train = np.array([7.05, 7.56, 8.20, 9.00, 10.00]).reshape(-1, 1)

weight = np.random.rand(1, 1) - 0.5
bias = 0
learning_rate = 0.01

for i in range(1000):
    y_pred = np.dot(x_train, weight) + bias
    error = y_pred - y_train
    cost = np.mean(error ** 2)
    if i % 100 == 0:
        print(cost)
    d_weight = 2 * np.mean(error * x_train)
    d_bias = 2 * np.mean(error)
    weight = weight - learning_rate * d_weight
    bias = bias - learning_rate * d_bias

x_test = np.array([[2]])
pred = np.dot(x_test, weight) + bias
print("prediction:", pred)
