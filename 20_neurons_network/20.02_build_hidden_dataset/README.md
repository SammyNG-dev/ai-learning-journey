# Projet 20.2 — Build Hidden Dataset

## 🎯 Objectif

Construire un nouveau dataset à partir des sorties de plusieurs neurones cachés.

---

## 🧩 Description

Ce programme :

- prend un dataset en entrée
- fait passer les données dans plusieurs neurones cachés
- récupère les sorties de chaque neurone
- regroupe ces sorties dans une nouvelle matrice :
  - `final_dataset`

Cette nouvelle matrice devient une nouvelle représentation des données.

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Sortie d’un neurone caché

Chaque neurone produit :

```text
une valeur par exemple
```

Exemple :

```python
[0.41, 0.63, 0.52, 0.77]
```

---

### 2. Plusieurs neurones cachés

Deux neurones produisent :

```python
output_neuron1
output_neuron2
```

Chaque neurone crée sa propre feature cachée.

---

### 3. Construction d’un nouveau dataset

Les sorties des neurones sont regroupées :

```python
np.array([
    output_neuron1,
    output_neuron2
])
```

Avant transposition :

```text
(2, 4)
=
2 neurones
4 exemples
```

---

### 4. Réorganisation avec `.T`

```python
final_dataset = np.array([
    output_neuron1,
    output_neuron2
]).T
```

Après transposition :

```text
(4, 2)
=
4 exemples
2 features cachées
```

---

### 5. Organisation des données

Dans le dataset final :

- chaque ligne représente un exemple
- chaque colonne représente une feature cachée

Exemple :

```python
[
 [0.41, 0.22],
 [0.63, 0.81],
 [0.52, 0.35],
 [0.77, 0.90]
]
```

---

### 6. Couche cachée

Une couche cachée :

- transforme les données
- produit une nouvelle représentation des exemples
- transmet cette représentation à la couche suivante

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

final_dataset = np.array([
    output_neuron1,
    output_neuron2
]).T

print(final_dataset.shape)
print(final_dataset)
```

---

## 📚 Ce que j’ai retenu

- plusieurs neurones cachés produisent plusieurs features cachées
- une couche cachée crée une nouvelle représentation des données
- les données doivent être organisées correctement :
  - lignes = exemples
  - colonnes = features
- `.T` permet de réorganiser les dimensions
- un réseau de neurones transmet des transformations successives des données