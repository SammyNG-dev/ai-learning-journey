# Projet 20.4 — Naive Error Propagation

## 🎯 Objectif

Faire apprendre uniquement le neurone final d’un réseau multicouche.

Les neurones cachés restent figés et ne sont jamais corrigés.

---

## 🧩 Description

Ce programme :

- prend un dataset en entrée
- fait passer les données dans une couche cachée
- construit un dataset caché (`final_dataset`)
- transmet ce dataset à un neurone final
- calcule l’erreur et le coût
- corrige uniquement :
  - `w_final`
  - `b_final`

Les poids des neurones cachés ne changent jamais.

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Réseau multicouche

Le réseau contient :

```text
entrée
→ couche cachée
→ neurone final
→ prédiction
```

---

### 2. Couche cachée figée

Les neurones cachés produisent des features :

```python
output_neuron1
output_neuron2
```

Mais leurs poids ne sont jamais modifiés :

```python
w1
b1
w2
b2
```

restent constants.

---

### 3. Dataset caché

Les sorties cachées sont regroupées :

```python
final_dataset = np.array([
    output_neuron1,
    output_neuron2
]).T
```

Le neurone final apprend uniquement à partir de ce dataset caché.

---

### 4. Erreur finale

```python
error = final_output - y_true
```

L’erreur est calculée uniquement sur la sortie finale du réseau.

---

### 5. Fonction de coût

```python
cost = np.mean(error ** 2)
```

Le coût mesure la qualité des prédictions du réseau.

---

### 6. Gradient du neurone final

```python
dw_final = np.dot(final_dataset.T, error) / len(final_dataset)
db_final = np.mean(error)
```

Important :

Le gradient utilise :

```python
final_dataset.T
```

et non :

```python
dataset.T
```

car le neurone final apprend à partir des features cachées.

---

### 7. Mise à jour des paramètres

```python
w_final = w_final - lr * dw_final
b_final = b_final - lr * db_final
```

Seuls les paramètres du neurone final sont corrigés.

---

### 8. Boucle d’apprentissage

Le réseau répète :

```text
forward
→ erreur
→ coût
→ correction du neurone final
```

---

### 9. Limite du système

Le neurone final apprend :

```text
mais les neurones cachés restent aléatoires
```

Donc :

- les features cachées peuvent être mauvaises
- le neurone final est limité par ces features
- le réseau ne peut pas encore apprendre complètement

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

    final_dataset = np.array([
        output_neuron1,
        output_neuron2
    ]).T

    final_output = neuron(final_dataset, w_final, b_final)

    error = final_output - y_true

    cost = np.mean(error ** 2)

    if i % 100 == 0:
        print(cost)

    dw_final = np.dot(final_dataset.T, error) / len(final_dataset)
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
```

---

## 📚 Ce que j’ai retenu

- un réseau multicouche peut produire une prédiction finale
- le neurone final apprend à partir des features cachées
- les gradients doivent utiliser les bonnes entrées
- une boucle est nécessaire pour apprendre progressivement
- un neurone final seul est limité si les features cachées sont mauvaises
- les neurones cachés doivent probablement être corrigés eux aussi