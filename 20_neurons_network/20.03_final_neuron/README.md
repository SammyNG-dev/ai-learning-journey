# Projet 20.3 — Final Neuron

## 🎯 Objectif

Utiliser les features produites par les neurones cachés comme entrées d’un neurone final.

---

## 🧩 Description

Ce programme :

- prend un dataset en entrée
- fait passer les données dans plusieurs neurones cachés
- construit un dataset caché (`final_dataset`)
- transmet ce dataset à un neurone final
- produit une prédiction finale

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Couche cachée

Les neurones cachés produisent de nouvelles features :

```python
output_neuron1
output_neuron2
```

Ces features représentent une transformation des données originales.

---

### 2. Dataset caché

Les sorties des neurones cachés sont regroupées :

```python
final_dataset = np.array([
    output_neuron1,
    output_neuron2
]).T
```

Le dataset caché possède :

```text
(nb_exemples, nb_features_cachees)
```

---

### 3. Neurone final

Le neurone final ne reçoit plus les données originales :

```python
[x1, x2]
```

Il reçoit les features cachées :

```python
[feature_cachee_1, feature_cachee_2]
```

---

### 4. Propagation avant (forward)

Les données circulent dans plusieurs étapes :

```text
dataset original
→ neurones cachés
→ dataset caché
→ neurone final
→ prédiction finale
```

Cette circulation des données est appelée :

```text
forward propagation
```

---

### 5. Réseau multicouche

Le système contient maintenant :

- une couche d’entrée
- une couche cachée
- une couche de sortie

C’est un premier réseau de neurones dense simple.

---

### 6. Importance des dimensions

Les shapes deviennent importantes :

```python
print(final_dataset.shape)
print(final_output.shape)
```

Une mauvaise organisation des dimensions peut casser le réseau.

---

## 📌 Exemple de code

```python
import numpy as np

dataset = np.array([
    [0, 1],
    [1, 0],
    [0, 0],
    [1, 1]
])

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

final_dataset = np.array([
    output_neuron1,
    output_neuron2
]).T

final_output = neuron(final_dataset, w_final, b_final)

print(final_output.shape)
print(final_output)

predictions = (final_output > 0.5).astype(int)

print(predictions)
```

---

## 📚 Ce que j’ai retenu

- une couche cachée transforme les données
- les sorties cachées deviennent les entrées du neurone final
- un réseau de neurones est une chaîne de transformations
- les données circulent couche par couche
- la propagation avant correspond au passage des données dans le réseau
- les dimensions des matrices deviennent essentielles dans un réseau multicouche