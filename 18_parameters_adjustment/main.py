import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, 0, 0, 1, 1, 1, 1])

x_train = x[0:5]
x_test = x[5:]

y_train = y[0:5]
y_test = y[5:]

learning_rates = [0.1, 0.01, 0.001]


def sigmoid(z):
    return 1/(1+np.exp(-z))

for lr in learning_rates:
    a = 0.0
    b = 0.0
    for i in range(1000):
        score = a * x_train + b
        y_pred = sigmoid(score)
        error = y_pred - y_train
        cost = np.mean(error ** 2)
        if i % 100 == 0:
            print(cost)
        da = np.mean(error * x_train)
        db = np.mean(error)
        a = a - lr * da
        b = b - lr * db
    print()
    print("lr =", lr, "cost final =", cost)
    print()
    score_test = a * x_test + b
    proba_test = sigmoid(score_test)
    predictions = (proba_test > 0.5).astype(int)
    print("Prédictions : ", predictions)
    print(np.array_equal(predictions, y_test))
