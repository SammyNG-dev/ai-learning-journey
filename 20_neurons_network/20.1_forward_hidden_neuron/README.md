# Projet 20.1 — Forward d’un neurone caché

## 🎯 Objectif

Comprendre comment un neurone caché peut transformer des données d’entrée en une nouvelle représentation exploitable par un autre neurone.

---

## 🧩 Description

Ce programme :

- prend un dataset contenant plusieurs exemples
- crée plusieurs neurones cachés
- fait passer les données dans ces neurones
- produit de nouvelles valeurs appelées :
  - sorties cachées
  - ou nouvelles features

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Neurone caché

Un neurone caché :

- reçoit des données en entrée
- calcule un score
- applique une sigmoid
- produit une nouvelle valeur

---

### 2. Combinaison linéaire

```python
score = np.dot(inputs, weights) + bias
```

Le neurone combine les features d’entrée avec ses poids.

---

### 3. Sigmoid

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

La sigmoid transforme le score en valeur comprise entre `0` et `1`.

---

### 4. Nouvelle feature

Chaque neurone caché produit :

```text
une nouvelle valeur par exemple
```

Exemple :

```python
[0.12, 0.34, 0.71, 0.91]
```

Cette sortie devient une nouvelle représentation des données.

---

### 5. Plusieurs neurones cachés

Deux neurones cachés produisent :

```python
feature_1 = [...]
feature_2 = [...]
```

Chaque neurone observe les données différemment grâce à ses propres poids.

---

### 6. Transformation des données

Avant :

```python
[0, 1]
[1, 0]
[0, 0]
[1, 1]
```

Après passage dans les neurones cachés :

```python
[0.41, 0.22]
[0.63, 0.81]
[0.52, 0.35]
[0.77, 0.90]
```

Les données ont été transformées.

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

w1 = np.random.rand(2) - 0.5
b1 = np.random.rand() - 0.5

w2 = np.random.rand(2) - 0.5
b2 = np.random.rand() - 0.5

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def neuron(inputs, weights, bias):
    score = np.dot(inputs, weights) + bias
    y_pred = sigmoid(score)
    return y_pred

output_neuron1 = neuron(dataset, w1, b1)
output_neuron2 = neuron(dataset, w2, b2)

print(output_neuron1)
print()
print(output_neuron2)
```

---

## 📚 Ce que j’ai retenu

- un neurone caché transforme les données
- chaque neurone crée une nouvelle feature
- plusieurs neurones produisent plusieurs représentations des données
- les sorties cachées peuvent servir d’entrées à un autre neurone
- un réseau de neurones est une chaîne de transformations successives