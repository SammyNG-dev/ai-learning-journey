# Projet 20.9 — Rétropropagation propre

## 🎯 Objectif

Comprendre comment le delta permet de calculer le gradient d’un poids et comment les poids sont corrigés dans un réseau de neurones.

---

## 🧩 Description

Ce programme :

- définit plusieurs valeurs d’entrée `x`
- définit plusieurs valeurs de `delta`
- calcule le gradient `dw`
- affiche les résultats
- permet d’observer pourquoi certains poids changent beaucoup et d’autres très peu

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Delta

Le delta représente :

```text
la force locale réelle de correction
```

Le delta combine :

- l’erreur
- la dérivée de la sigmoid

---

### 2. Gradient d’un poids

```python
dw = x * delta
```

Le gradient mesure :

```text
de combien un poids doit être corrigé
```

---

### 3. Rôle de l’entrée `x`

L’entrée indique :

```text
à quel point ce poids a participé au calcul
```

---

### 4. Entrée faible

Exemple :

```text
x = 0.1
```

Même avec un delta important :

```text
le gradient reste limité
```

car cette entrée a peu influencé le neurone.

---

### 5. Entrée forte

Exemple :

```text
x = 5
```

Si le delta est fort :

```text
le gradient devient important
```

car cette entrée a fortement participé à l’erreur.

---

### 6. Relation complète

Le gradient dépend :

- de la participation de l’entrée
- de la force locale de correction

---

### 7. Chaîne complète de correction

```text
sigmoid
→ dérivée
→ delta
→ gradient
→ correction des poids
```

---

### 8. Importance locale des poids

Tous les poids ne sont pas corrigés de la même manière.

Un poids reçoit :

- une forte correction s’il a beaucoup contribué à l’erreur
- une faible correction s’il a peu participé

---

## 📌 Exemple de code

```python
import numpy as np

x_values = np.array([0.1, 1, 5])

delta_values = np.array([
    0.001,
    0.1,
    1
])

for x, delta in zip(x_values, delta_values):

    dw = x * delta

    print(dw)
    print()
```

---

## 📌 Exemple de sortie

```text
0.0001

0.1

5.0
```

---

## 📚 Ce que j’ai retenu

- le delta représente la force locale de correction
- le gradient dépend à la fois :
  - de l’entrée
  - du delta
- une entrée importante produit une correction plus forte
- un poids peu impliqué reçoit une faible correction
- tous les poids ne sont pas modifiés de la même manière
- le gradient sert à corriger les poids du réseau
- la rétropropagation distribue les corrections selon la responsabilité locale des neurones