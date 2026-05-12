import numpy as np

dataset = np.array([[0, 1],
              [1, 0],
              [0, 0],
              [1, 1]])

y_true = np.array([1, 1, 0, 0])

w1 = np.random.rand(2) - 0.5
b1 = np.random.rand() - 0.5

w2 = np.random.rand(2) - 0.5
b2 = np.random.rand() - 0.5

w_final = np.random.rand(2) - 0.5
b_final = np.random.rand() - 0.5

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def neuron(inputs, weights, bias):
    score = np.dot(inputs, weights) + bias
    y_pred = sigmoid(score)
    return y_pred

output_neuron1 = neuron(dataset, w1, b1)
output_neuron2 = neuron(dataset, w2, b2)
final_dataset = np.array([output_neuron1, output_neuron2]).T
final_output = neuron(final_dataset, w_final, b_final)
print(final_output.shape)
predictions = (final_output > 0.5).astype(int)
print(predictions)