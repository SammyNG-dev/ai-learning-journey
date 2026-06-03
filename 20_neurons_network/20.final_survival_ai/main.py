import numpy as np

np.random.seed(42)

x_train = np.array([
    [1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1]
])

y_train = np.array([
    1,
    1,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0
])

lr = 0.1

weights1 = np.random.rand(6, 4) - 0.5
bias1 = np.random.rand(4) - 0.5

weights2 = np.random.rand(4, 2) - 0.5
bias2 = np.random.rand(2) - 0.5 

weights_final = np.random.rand(2, 1) - 0.5
bias_final = np.random.rand() - 0.5

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(s):
    return s * (1 - s)

def neuron(dataset, weights, bias):
    score = np.dot(dataset, weights) + bias
    y_pred = sigmoid(score)
    return y_pred

# forward, calcul de l'erreur et du coût

output_hidden_neurons_layer1 = neuron(x_train, weights1, bias1)
output_hidden_neurons_layer2 = neuron(output_hidden_neurons_layer1, weights2, bias2)
output_final_neuron = neuron(output_hidden_neurons_layer2, weights_final, bias_final)
y_train = y_train.reshape(-1, 1)
error = output_final_neuron - y_train
cost = np.mean(error ** 2)

# correction du neurone final

final_delta = error * sigmoid_derivative(output_final_neuron)
dw_final = np.dot(output_hidden_neurons_layer2.T, final_delta) / len(x_train)
db_final = np.mean(final_delta, axis=0)
weights_final = weights_final - lr * dw_final
bias_final = bias_final - lr * db_final
print(weights_final.shape)