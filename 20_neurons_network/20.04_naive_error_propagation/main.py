import numpy as np

dataset = np.array([[0, 1],
              [1, 0],
              [0, 0],
              [1, 1]])

y_true = np.array([1, 1, 0, 0])

lr = 0.1

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

for i in range(1000):
    output_neuron1 = neuron(dataset, w1, b1)
    output_neuron2 = neuron(dataset, w2, b2)
    final_dataset = np.array([output_neuron1, output_neuron2]).T
    final_output = neuron(final_dataset, w_final, b_final)
    error = final_output - y_true
    cost = np.mean(error ** 2)
    if i % 100 == 0:
        print(cost)
    dw_final = np.dot(final_dataset.T, error) /len(final_dataset)
    db_final = np.mean(error)
    w_final = w_final - lr * dw_final
    b_final = b_final - lr * db_final

final_proba = neuron(final_dataset, w_final, b_final)
error_final = final_proba - y_true
cost_final = np.mean(error_final ** 2)
predictions = (final_proba > 0.5).astype(int)
print("cost_final:", cost_final)
print("predictions:", predictions)
print("y_true:", y_true)