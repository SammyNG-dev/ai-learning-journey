# Projet 20.7 — Dérivée de la sigmoid

## 🎯 Objectif

Comprendre ce que mesure la dérivée de la sigmoid et pourquoi elle est importante pour l’apprentissage d’un neurone.

---

## 🧩 Description

Ce programme :

- crée plusieurs valeurs de `z`
- calcule la sigmoid pour chaque valeur
- calcule la dérivée de la sigmoid
- affiche les résultats
- permet d’observer les zones où un neurone apprend facilement
- permet d’observer les zones où un neurone apprend difficilement

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Score brut `z`

`z` est la valeur calculée avant la sigmoid.

Exemple :

```python
z = x * w + b
```

---

### 2. Fonction sigmoid

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

La sigmoid transforme `z` en valeur comprise entre `0` et `1`.

---

### 3. Dérivée de la sigmoid

```python
def sigmoid_derivative(s):
    return s * (1 - s)
```

La dérivée mesure :

```text
à quel point la sortie peut encore changer
```

---

### 4. Zone d’apprentissage optimale

Quand :

```text
z ≈ 0
```

alors :

```text
sigmoid ≈ 0.5
```

et la dérivée est maximale :

```text
0.25
```

Dans cette zone :

```text
le neurone apprend facilement
```

---

### 5. Zones de saturation

Quand :

```text
z très positif
```

ou :

```text
z très négatif
```

la sigmoid devient presque plate.

Exemple :

```text
z = -10 → sigmoid ≈ 0
z = 10  → sigmoid ≈ 1
```

La dérivée devient alors très faible :

```text
≈ 0
```

---

### 6. Neurone saturé

Quand la dérivée devient très faible :

```text
le neurone réagit presque plus
```

Même si les poids changent un peu :

```text
la sortie change très peu
```

Le neurone apprend donc difficilement.

---

### 7. Sensibilité locale

La dérivée représente la sensibilité locale de la sigmoid :

- grande dérivée → forte réaction
- petite dérivée → faible réaction

---

### 8. Symétrie

La dérivée est symétrique autour de `0`.

Exemple :

```text
z = -1 → dérivée ≈ 0.196
z =  1 → dérivée ≈ 0.196
```

---

## 📌 Exemple de code

```python
import numpy as np

z_values = np.array([
    -10,
    -5,
    -2,
    -1,
    0,
    1,
    2,
    5,
    10
])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(s):
    return s * (1 - s)

for value in z_values:

    sigmoid_value = sigmoid(value)

    derivative = sigmoid_derivative(sigmoid_value)

    print(
        value,
        "- Sigmoid :",
        sigmoid_value,
        "; Derivée :",
        derivative
    )
```

---

## 📌 Exemple de sortie

```text
-10 - Sigmoid : 0.000045 ; Derivée : 0.000045
-5  - Sigmoid : 0.0067   ; Derivée : 0.0066
-2  - Sigmoid : 0.1192   ; Derivée : 0.1049
-1  - Sigmoid : 0.2689   ; Derivée : 0.1966
0   - Sigmoid : 0.5      ; Derivée : 0.25
1   - Sigmoid : 0.7310   ; Derivée : 0.1966
2   - Sigmoid : 0.8807   ; Derivée : 0.1049
5   - Sigmoid : 0.9933   ; Derivée : 0.0066
10  - Sigmoid : 0.99995  ; Derivée : 0.000045
```

---

## 📚 Ce que j’ai retenu

- la dérivée mesure la sensibilité locale de la sigmoid
- près de `z = 0`, la sigmoid réagit fortement
- aux extrêmes, la sigmoid devient presque plate
- un neurone saturé apprend difficilement
- la dérivée est maximale autour de `z = 0`
- cette idée est essentielle pour comprendre le gradient et la rétropropagation