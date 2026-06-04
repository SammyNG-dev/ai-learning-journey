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

x_test = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1],

    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1],

    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 1],

    [0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],

    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],

    [1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],

    [1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1]
])

lr = 1

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

y_train = y_train.reshape(-1, 1)

# boucle d'apprentissage

for i in range(1000):

    # forward

    output_hidden_neurons_layer1 = neuron(x_train, weights1, bias1)
    output_hidden_neurons_layer2 = neuron(output_hidden_neurons_layer1, weights2, bias2)
    output_final_neuron = neuron(output_hidden_neurons_layer2, weights_final, bias_final)

    # calcul de l'erreur, du coût et des deltas

    error = output_final_neuron - y_train
    cost = np.mean(error ** 2)
    if i % 100 == 0:
        print(f"iteration {i}:")
        print(f"cost: {cost}")
    final_delta = error * sigmoid_derivative(output_final_neuron)
    delta_hidden_neurons_layer2 = np.dot(final_delta, weights_final.T) * sigmoid_derivative(output_hidden_neurons_layer2)
    delta_hidden_neurons_layer1 = np.dot(delta_hidden_neurons_layer2, weights2.T) * sigmoid_derivative(output_hidden_neurons_layer1)

    # calcul des gradients et retropropagation de la 1ere couche de neurones (6 entrées - 4 neurones)

    dw1 = np.dot(x_train.T, delta_hidden_neurons_layer1) / len(x_train)
    db1 = np.mean(delta_hidden_neurons_layer1, axis=0)
    weights1 = weights1 - lr * dw1
    bias1 = bias1 - lr * db1

    # calcul des gradients et retropropagation de la 2e couche de neurones (4 entrées - 2 neurones)

    dw2 = np.dot(output_hidden_neurons_layer1.T, delta_hidden_neurons_layer2) / len(output_hidden_neurons_layer1)
    db2 = np.mean(delta_hidden_neurons_layer2, axis=0)
    weights2 = weights2 - lr * dw2
    bias2 = bias2 - lr * db2

    # calcul des gradients retropropagation du neurone final

    dw_final = np.dot(output_hidden_neurons_layer2.T, final_delta) / len(x_train)
    db_final = np.mean(final_delta, axis=0)
    weights_final = weights_final - lr * dw_final
    bias_final = bias_final - lr * db_final

# test de l'IA

test_output1 = neuron(x_test, weights1, bias1)
test_output2 = neuron(test_output1, weights2, bias2)
test_final_output = neuron(test_output2, weights_final, bias_final)
test_predictions = (test_final_output > 0.5).astype(int)
for x, proba, pred in zip(x_test, test_final_output, test_predictions):
        print(x, "->", round(float(proba.item()), 3), "->", int(pred.item()))
