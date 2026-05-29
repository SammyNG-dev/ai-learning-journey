# Projet 20.10 — Clean Backpropagation

## 🎯 Objectif

Implémenter une première rétropropagation complète sur un petit réseau de neurones.

L'objectif est que :

- le neurone final apprenne
- les neurones cachés apprennent également
- l'erreur finale soit propagée vers les couches précédentes

---

## 🧩 Description

Le réseau est composé de :

- 2 neurones cachés
- 1 neurone final

Le réseau est entraîné sur le dataset XOR :

```python
x = np.array([
    [0, 1],
    [1, 0],
    [0, 0],
    [1, 1]
])

y_true = np.array([
    1,
    1,
    0,
    0
])
```

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Limite de la rétropropagation naïve

Dans les projets précédents :

```text
seul le neurone final apprenait
```

Les neurones cachés restaient figés.

Le réseau ne pouvait donc pas améliorer les features qu'il produisait.

---

### 2. Delta du neurone final

Le neurone final calcule :

```text
erreur
×
dérivée locale
```

```python
final_delta = error * final_derivative
```

Le delta représente :

```text
le signal local de correction
```

---

### 3. Delta des neurones cachés

Les neurones cachés ne connaissent jamais :

```python
y_true
```

Ils ne peuvent donc pas calculer directement leur erreur.

Ils reçoivent une partie du signal provenant du neurone suivant.

---

### 4. Construction d'un delta caché

Le delta caché dépend :

- du delta de la couche suivante
- du poids de connexion
- de la dérivée locale

Exemple :

```python
hidden_delta_neuron1 = (
    final_delta
    * final_w[0]
    * derivative_neuron1
)
```

---

### 5. Poids de connexion

Dans ce réseau :

```text
neurone caché 1 ---- final_w[0] ----\
                                      > neurone final
neurone caché 2 ---- final_w[1] ----/
```

Les poids :

```python
final_w[0]
final_w[1]
```

mesurent l'influence des neurones cachés sur le neurone final.

---

### 6. Gradient des neurones cachés

Une fois les deltas cachés calculés :

```python
dw1 = np.dot(x.T, hidden_delta_neuron1)
dw2 = np.dot(x.T, hidden_delta_neuron2)
```

Les gradients permettent de corriger les poids.

---

### 7. Mise à jour des poids

```python
w1 = w1 - lr * dw1
w2 = w2 - lr * dw2

final_w = final_w - lr * dw_final
```

Chaque neurone corrige ses propres poids.

---

### 8. Chaîne complète d'apprentissage

```text
forward

→ erreur finale

→ delta final

→ deltas cachés

→ gradients

→ mise à jour des poids
```

---

### 9. Première vraie rétropropagation multicouche

Pour la première fois :

```text
les neurones cachés apprennent eux aussi
```

L'erreur finale est propagée à travers le réseau.

---

## 📌 Ce que j'ai retenu

- le neurone final est le seul à connaître `y_true`
- les neurones cachés reçoivent l'information d'erreur depuis la couche suivante
- un delta caché dépend du delta suivant
- le poids de connexion mesure l'influence d'un neurone sur le suivant
- chaque neurone possède sa propre dérivée locale
- chaque neurone calcule ses propres gradients
- chaque neurone corrige ses propres poids
- la rétropropagation distribue l'erreur finale à tous les neurones ayant participé au résultat

---

## ✅ Résultat obtenu

Le réseau est capable d'apprendre XOR :

```text
[1, 1, 0, 0]
```

Cependant :

- certaines initialisations apprennent correctement
- d'autres restent bloquées

L'apprentissage n'est donc pas encore totalement stable.

La stabilisation sera étudiée dans le projet suivant.