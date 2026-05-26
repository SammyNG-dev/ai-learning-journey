import numpy as np

x = np.array([[0, 1],
              [1, 0],
              [0, 0],
              [1, 1]])

y_true = np.array([1, 1, 0, 0])

w1 = np.random.rand(2) - 0.5
b1 = np.random.rand() - 0.5

w2 = np.random.rand(2) - 0.5
b2 = np.random.rand() - 0.5

final_w = np.random.rand(2) - 0.5
final_b = np.random.rand() - 0.5

lr = 0.1

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(s):
    return s * (1 - s)

def neuron(dataset, weights, bias):
    score = np.dot(dataset, weights) + bias
    y_pred = sigmoid(score)
    return y_pred


for i in range(1000):
    output_neuron1 = neuron(x, w1, b1)
    output_neuron2 = neuron(x, w2, b2)
    final_dataset = np.array([output_neuron1, output_neuron2]).T
    final_output = neuron(final_dataset, final_w, final_b)
    error = final_output - y_true
    final_derivative = sigmoid_derivative(final_output)
    final_delta = error * final_derivative
    cost = np.mean(error ** 2)
    dw_final = np.dot(final_dataset.T, final_delta) / len(final_dataset)
    db_final = np.mean(final_delta)
    final_w = final_w - lr * dw_final
    final_b = final_b - lr * db_final

last_output_neuron1 = neuron(x, w1, b1)
last_output_neuron2 = neuron(x, w2, b2)
last_dataset = np.array([last_output_neuron1, last_output_neuron2]).T
last_output_final_neuron = neuron(last_dataset, final_w, final_b)
last_predictions = (last_output_final_neuron > 0.5).astype(int)
print("last_predictions :", last_predictions)