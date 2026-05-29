# ce réseau de neurones apprend XOR. 

# ce projet est un recodage du début à la fin du projet 20.10 en y ajoutant np.random.seed(42) et des données de test

import numpy as np

np.random.seed(42)

x = np.array([[0, 0],
              [1, 0],
              [1, 1],
              [0, 1]])

y_true = np.array([0, 1, 0, 1])

x_test = np.array([[0, 0],
                   [1, 1],
                   [0, 1],
                   [1, 0]])

y_test = np.array([0, 0, 1, 1])

w1 = np.random.rand(2) - 0.5
b1 = np.random.rand() - 0.5

w2 = np.random.rand(2) - 0.5
b2 = np.random.rand() - 0.5

w_final = np.random.rand(2) - 0.5
b_final = np.random.rand() - 0.5

lr = 1.0

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(s):
    return s * (1 - s)

def neuron(dataset, weights, bias):
    score = np.dot(dataset, weights) + bias
    y_pred = sigmoid(score)
    return y_pred

for i in range(10000):
    output_neuron1 = neuron(x, w1, b1)
    output_neuron2 = neuron(x, w2, b2)
    final_dataset = np.array([output_neuron1, output_neuron2]).T
    final_output = neuron(final_dataset, w_final, b_final)
    error = final_output - y_true
    final_delta = error * sigmoid_derivative(final_output)
    hidden_delta_neuron1 = sigmoid_derivative(output_neuron1) * w_final[0] * final_delta
    hidden_delta_neuron2 = sigmoid_derivative(output_neuron2) * w_final[1] * final_delta
    cost = np.mean(error ** 2)
    if i % 100 == 0:
        print("iteration:", i)
        print("cost: ",cost)
    dw1 = np.dot(x.T, hidden_delta_neuron1) / len(x)
    db1 = np.mean(hidden_delta_neuron1)
    dw2 = np.dot(x.T, hidden_delta_neuron2) / len(x)
    db2 = np.mean(hidden_delta_neuron2)
    dw_final = np.dot(final_dataset.T, final_delta) / len(final_dataset)
    db_final = np.mean(final_delta)
    w1 = w1 - lr * dw1
    b1 = b1 - lr * db1
    w2 = w2 - lr * dw2
    b2 = b2 - lr * db2
    w_final = w_final - lr * dw_final
    b_final = b_final - lr * db_final

print()
last_output_neuron1 = neuron(x_test, w1, b1)
last_output_neuron2 = neuron(x_test, w2, b2)
last_dataset = np.array([last_output_neuron1, last_output_neuron2]).T
last_output_final_neuron = neuron(last_dataset, w_final, b_final)
last_error = last_output_final_neuron - y_test
last_cost = np.mean(last_error ** 2)
predictions = (last_output_final_neuron > 0.5).astype(int)
print("last_cost: ", last_cost)
print("predictions: ", predictions)
print("last_output_final_neuron:", last_output_final_neuron)
print("y_test:", y_test)