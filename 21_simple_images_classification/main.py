import numpy as np

np.random.seed(42)

vertical_1 = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]).flatten()

vertical_2 = np.array([
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
]).flatten()

vertical_3 = np.array([
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1]
]).flatten()

horizontal_1 = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]).flatten()

horizontal_2 = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]
]).flatten()

horizontal_3 = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1]
]).flatten()

x_train = np.array([vertical_1, vertical_2, vertical_3, horizontal_1, horizontal_2, horizontal_3])

y_train = np.array([0, 0, 0, 1, 1, 1]).reshape(-1, 1)

lr = 5

weights1 = np.random.rand(9, 2) - 0.5
bias1 = np.random.rand(2) - 0.5

weights_final = np.random.rand(2, 1) - 0.5
bias_final = np.random.rand(1) - 0.5

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def neuron(dataset, weights, bias):
    score = np.dot(dataset, weights) + bias
    y_pred = sigmoid(score)
    return y_pred

def sigmoid_derivative(s):
    return s * (1 - s)

y_train = y_train.reshape(-1, 1)

for i in range(1000):
    # forward
    output_hidden_neurons_layer = neuron(x_train, weights1, bias1)
    output_final_neuron = neuron(output_hidden_neurons_layer, weights_final, bias_final)

    # calcul de l'erreur, du coût et des deltas
    error = output_final_neuron - y_train
    cost = np.mean(error ** 2)
    if i % 100 == 0:
        print(cost)
    delta_final = error * sigmoid_derivative(output_final_neuron)
    delta_hidden_neurons_layer = np.dot(delta_final, weights_final.T) * sigmoid_derivative(output_hidden_neurons_layer)

    # calcul des gradients et correction des neurones cachés (9 entrées - 2 neurones)
    dw1 = np.dot(x_train.T, delta_hidden_neurons_layer) / len(x_train)
    db1 = np.mean(delta_hidden_neurons_layer)
    weights1 = weights1 - lr * dw1
    bias1 = bias1 - lr * db1

    # calcul des gradients et correction du neurone final (2 entrées - 1 neurone)
    dw_final = np.dot(output_hidden_neurons_layer.T, delta_final) / len(x_train)
    db_final = np.mean(delta_final, axis=0)
    weights_final = weights_final - lr * dw_final
    bias_final = bias_final - lr * db_final

last_output_hidden_neurons_layer = neuron(x_train, weights1, bias1)
last_output_final_neuron = neuron(last_output_hidden_neurons_layer, weights_final, bias_final)
predictions = (last_output_final_neuron > 0.5).astype(int)
print(predictions)
if(np.array_equal(y_train, predictions)):
    print("Bingo !!")