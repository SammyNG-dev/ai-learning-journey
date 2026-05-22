# Projet 20.8 — Delta et erreur locale

## 🎯 Objectif

Comprendre comment un neurone reçoit une information locale de correction grâce au delta.

---

## 🧩 Description

Ce programme :

- définit une valeur réelle `y_true`
- teste plusieurs prédictions `y_pred`
- calcule :
  - l’erreur
  - la dérivée de la sigmoid
  - le delta
- affiche les résultats
- permet d’observer l’influence de la dérivée sur la correction

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Erreur

```python
error = y_pred - y_true
```

L’erreur mesure :

```text
à quel point le neurone se trompe
```

---

### 2. Dérivée de la sigmoid

```python
def sigmoid_derivative(s):
    return s * (1 - s)
```

La dérivée mesure :

```text
à quel point le neurone peut encore réagir
```

---

### 3. Delta

```python
delta = error * derivative
```

Le delta combine :

- l’erreur
- la capacité de réaction du neurone

---

### 4. Rôle du delta

Le delta représente :

```text
la force locale réelle de correction
```

---

### 5. Neurone réactif

Quand :

```text
dérivée forte
```

alors :

```text
le neurone peut encore apprendre efficacement
```

Même une erreur modérée peut produire une correction importante.

---

### 6. Neurone saturé

Quand :

```text
sigmoid proche de 0 ou 1
```

la sigmoid devient presque plate.

Donc :

```text
la dérivée devient faible
```

et :

```text
le delta devient faible
```

---

### 7. Grande erreur ≠ grande correction

Un neurone peut :

- se tromper énormément
- mais recevoir une faible correction

si la dérivée est très faible.

---

### 8. Exemple de saturation

```text
y_pred = 0.999
y_true = 0
```

Le neurone est très sûr de lui mais se trompe fortement.

Cependant :

```text
la dérivée est presque nulle
```

Donc :

```text
la correction reste très faible
```

---

### 9. Lien avec l’apprentissage

Le delta sera utilisé plus tard pour :

```text
corriger les poids du neurone
```

Le delta devient le signal local de correction transmis dans le réseau.

---

## 📌 Exemple de code

```python
import numpy as np

y_true = 0

y_pred = np.array([0.5, 0.9, 0.999])

def sigmoid_derivative(s):
    return s * (1 - s)

i = 0

for pred in y_pred:

    i += 1

    error = pred - y_true

    derivative = sigmoid_derivative(pred)

    delta = error * derivative

    print(i, "------------------")
    print("error: ", error)
    print("derivative: ", derivative)
    print("delta :", delta)
    print()
```

---

## 📌 Exemple de sortie

```text
1 ------------------
error:  0.5
derivative:  0.25
delta : 0.125

2 ------------------
error:  0.9
derivative:  0.09
delta : 0.081

3 ------------------
error:  0.999
derivative:  0.000999
delta : 0.000998
```

---

## 📚 Ce que j’ai retenu

- l’erreur seule ne suffit pas pour corriger un neurone
- la dérivée indique la capacité locale de réaction
- le delta combine erreur et réactivité
- un neurone saturé reçoit des corrections très faibles
- une grosse erreur ne garantit pas une grosse correction
- le delta devient le signal local de correction du neurone
- la saturation de la sigmoid ralentit fortement l’apprentissage