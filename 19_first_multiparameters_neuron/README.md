# Projet 19 — Premier neurone multiparamètres

## Objectif

Implémenter un neurone artificiel capable :

- de prendre plusieurs entrées
- de produire une probabilité
- d’apprendre automatiquement à partir des erreurs

---

## Description

Ce programme :

- prend des données en entrée `x`
- associe un poids à chaque entrée `w`
- calcule un score `z`
- transforme ce score en probabilité avec la sigmoid
- compare la prédiction avec la réalité `y`
- ajuste les paramètres `w` et `b` grâce au gradient

---

## Technologies utilisées

- Python
- NumPy

---

## Concepts clés

### 1. Entrées

```python
x = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
```

- chaque ligne représente un exemple
- chaque colonne représente une feature

---

### 2. Sorties attendues

```python
y = np.array([0, 0, 0, 1])
```

Ce dataset représente une logique ET :

```text
[0, 0] -> 0
[0, 1] -> 0
[1, 0] -> 0
[1, 1] -> 1
```

---

### 3. Paramètres du neurone

```python
w = np.array([0.0, 0.0])
b = 0.0
lr = 0.1
```

- `w` : poids du neurone
- `b` : biais
- `lr` : learning rate

Il y a un poids par feature.

---

### 4. Combinaison linéaire

```python
z = np.dot(x, w) + b
```

Le neurone calcule un score brut.

Pour une ligne :

```text
z = x1 * w1 + x2 * w2 + b
```

---

### 5. Fonction sigmoid

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

La sigmoid transforme le score brut en valeur comprise entre 0 et 1.

```text
z négatif -> valeur proche de 0
z = 0 -> valeur égale à 0.5
z positif -> valeur proche de 1
```

---

### 6. Prédiction

```python
y_pred = sigmoid(z)
```

`y_pred` contient les probabilités prédites par le neurone.

---

### 7. Erreur

```python
error = y_pred - y
```

L’erreur mesure l’écart entre la prédiction et la réalité.

---

### 8. Fonction de coût

```python
cost = np.mean(error ** 2)
```

Le coût mesure l’erreur globale du modèle.

Objectif :

```text
faire diminuer le coût
```

---

### 9. Gradient

```python
dw = np.dot(x.T, error) / len(x)
db = np.mean(error)
```

Le gradient indique comment corriger les paramètres.

- `dw` corrige les poids
- `db` corrige le biais

---

## Rôle de `x.T`

`x` est organisé par exemples :

```text
[0, 0]
[0, 1]
[1, 0]
[1, 1]
```

`x.T` est organisé par features :

```text
[0, 0, 1, 1]
[0, 1, 0, 1]
```

On utilise `x.T` pour calculer une correction par feature.

```text
2 features -> 2 poids -> 2 gradients
```

Exemple de dimensions :

```text
x.shape = (4, 2)
x.T.shape = (2, 4)
error.shape = (4,)
dw.shape = (2,)
```

Calcul :

```text
(2, 4) · (4,) -> (2,)
```

---

## Mise à jour des paramètres

```python
w = w - lr * dw
b = b - lr * db
```

Le modèle ajuste progressivement ses poids et son biais.

---

## Décision finale

```python
predictions = (y_pred > 0.5).astype(int)
```

Règle :

```text
proba > 0.5 -> 1
proba <= 0.5 -> 0
```

---

## Boucle d’apprentissage

```text
entrée
-> combinaison linéaire
-> sigmoid
-> probabilité
-> erreur
-> coût
-> gradient
-> mise à jour
-> répétition
```

---

## Code complet

```python
import numpy as np

x = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])

w = np.array([0.0, 0.0])
b = 0.0
lr = 0.1

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for i in range(1000):
    z = np.dot(x, w) + b
    y_pred = sigmoid(z)

    error = y_pred - y
    cost = np.mean(error ** 2)

    dw = np.dot(x.T, error) / len(x)
    db = np.mean(error)

    w = w - lr * dw
    b = b - lr * db

predictions = (y_pred > 0.5).astype(int)

print("w:", w)
print("b:", b)
print("cost:", cost)
print("y_pred:", y_pred)
print("predictions:", predictions)
```

---

## Résultat attendu

```text
w: valeurs positives
b: valeur négative
cost: faible
y_pred: proche de [0, 0, 0, 1]
predictions: [0 0 0 1]
```

---

## Limite du neurone

Un seul neurone ne peut apprendre que des séparations linéaires.

Il peut apprendre une logique ET.

Il ne peut pas apprendre XOR.

XOR n’est pas linéairement séparable.

---

## Ce que j’ai retenu

- un neurone prend des entrées
- chaque entrée a un poids
- le neurone calcule une combinaison linéaire
- la sigmoid transforme le score en probabilité
- l’erreur permet de mesurer l’écart avec la réalité
- le gradient permet de corriger les poids et le biais
- `x.T` sert à calculer un gradient par feature
- un seul neurone est limité aux problèmes linéaires

---

## Lien avec l’objectif final

Ce neurone est une brique de base.

Pour construire une IA capable de jouer à Sonic 2, il faudra combiner plusieurs neurones.

Un réseau de neurones permettra de traiter des situations plus complexes qu’un seul neurone.