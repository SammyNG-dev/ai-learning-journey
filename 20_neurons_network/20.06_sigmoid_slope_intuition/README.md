# Projet 20.6 — Intuition de la pente de la sigmoid

## 🎯 Objectif

Comprendre que la sigmoid ne réagit pas partout avec la même intensité.

---

## 🧩 Description

Ce programme :

- crée plusieurs valeurs de `z`
- applique la fonction sigmoid sur chaque valeur
- affiche le résultat
- permet d’observer les zones où la sigmoid change beaucoup
- permet d’observer les zones où la sigmoid change très peu

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Score brut `z`

`z` est une valeur brute calculée avant la sigmoid.

Exemples :

```python
-10
-5
0
5
10
```

---

### 2. Sigmoid

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

La sigmoid transforme `z` en valeur comprise entre `0` et `1`.

---

### 3. Zone sensible

Autour de `z = 0`, la sigmoid change beaucoup.

Exemple :

```text
-1 : 0.268
 0 : 0.5
 1 : 0.731
```

Une petite variation de `z` produit une variation visible de la sortie.

---

### 4. Zones plates

Quand `z` est très négatif ou très positif, la sigmoid change très peu.

Exemple :

```text
-10 : 0.000045
-5  : 0.0067

5   : 0.993
10  : 0.99995
```

La sortie est presque bloquée vers `0` ou vers `1`.

---

### 5. Intuition de la pente

La pente indique si une fonction change beaucoup ou peu à un endroit donné.

Pour la sigmoid :

```text
près de 0 → pente forte
aux extrêmes → pente faible
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

for value in z_values:
    print(value, ":", sigmoid(value))
```

---

## 📌 Exemple de sortie

```text
-10 : 4.5397868702434395e-05
-5 : 0.0066928509242848554
-2 : 0.11920292202211755
-1 : 0.2689414213699951
0 : 0.5
1 : 0.7310585786300049
2 : 0.8807970779778823
5 : 0.9933071490757153
10 : 0.9999546021312976
```

---

## 📚 Ce que j’ai retenu

- la sigmoid transforme un score brut en valeur entre `0` et `1`
- la sigmoid n’a pas la même sensibilité partout
- près de `0`, la sortie change beaucoup
- aux extrêmes, la sortie change très peu
- cette idée prépare la compréhension de la dérivée de la sigmoid
- pour corriger un neurone, il faut savoir si sa sortie peut encore changer facilement