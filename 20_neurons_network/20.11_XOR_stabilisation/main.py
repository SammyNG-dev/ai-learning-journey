import numpy as np

x = np.array([[0, 0],
              [1, 0],
              [1, 1],
              [0, 1]])

y_true = np.array([0, 1, 0, 1])

w1 = np.random.rand(2) - 0.5
b1 = np.random.rand() - 0.5

w2 = np.random.rand(2) - 0.5
b2 = np.random.rand() - 0.5

w_final = np.random.rand(2) - 0.5
b_final = np.random.rand() - 0.5

lr = 0.1

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(s):
    return s * (1 - s)

def neuron(dataset, weights, bias):
    score = np.dot(dataset, weights) + bias
    y_pred = sigmoid(score)
    return y_pred

output_neuron1 = neuron(x, w1, b1)
output_neuron2 = neuron(x, w2, b2)
final_dataset = np.array([output_neuron1, output_neuron2]).T
final_output = neuron(final_dataset, w_final, b_final)
error = final_output - y_true
cost = np.mean(error ** 2)
dw_final = np.dot(final_dataset.T, error) / len(final_dataset)
db_final = np.mean(error)
w_final = w_final - lr * dw_final
b_final = b_final - lr * db_final
output_final_neuron = neuron(final_dataset, w_final, b_final)