# P25.2 - Une sortie par action

## Objectif

Dans le projet précédent, nous avons entraîné un neurone à prédire une seule Q-value.

Exemple :

```text
Position 2 → 8.20
```

Cependant, une Q-value seule ne permet pas à un agent de choisir entre plusieurs actions.

L'objectif de ce projet est de permettre au réseau de prédire plusieurs Q-values simultanément :

```text
Q(avancer)
Q(reculer)
```

afin de pouvoir comparer les actions disponibles.

---

## Pourquoi plusieurs sorties ?

Dans une Q-Table classique, nous stockons :

```python
q_table[(position, "avancer")]
q_table[(position, "reculer")]
```

Exemple :

```text
Position 2 :

Q(avancer) = 8.20
Q(reculer) = 6.05
```

L'agent choisit alors :

```text
8.20 > 6.05
↓
avancer
```

Nous voulons maintenant que le réseau réalise cette estimation.

---

## Dataset utilisé

Entrées :

```python
x_train = np.array([
    [0],
    [1],
    [2],
    [3],
    [4]
])
```

Sorties attendues :

```python
y_train = np.array([
    [7.05, 5.64],
    [7.56, 5.64],
    [8.20, 6.05],
    [9.00, 6.56],
    [10.00, 7.20]
])
```

Chaque ligne représente :

```text
[Q(avancer), Q(reculer)]
```

---

## Architecture du réseau

Entrée :

```text
Position
```

Sorties :

```text
Q(avancer)
Q(reculer)
```

Architecture :

```text
1 → 2
```

---

## Shapes importantes

Dataset :

```python
x_train.shape
```

```text
(5, 1)
```

```python
y_train.shape
```

```text
(5, 2)
```

Paramètres :

```python
weights.shape
```

```text
(1, 2)
```

```python
bias.shape
```

```text
(1, 2)
```

Prédictions :

```python
y_pred.shape
```

```text
(5, 2)
```

---

## Calcul de la prédiction

Le réseau effectue :

```python
y_pred = np.dot(x_train, weights) + bias
```

Calcul matriciel :

```text
(5,1) dot (1,2)
↓
(5,2)
```

Le résultat contient deux Q-values pour chaque position.

---

## Fonction de coût

Nous conservons la même fonction de coût que dans le projet précédent :

```python
cost = np.mean(error ** 2)
```

avec :

```python
error = y_pred - y_train
```

Cette fonction fonctionne naturellement avec plusieurs sorties.

---

## Calcul des gradients

Gradient des poids :

```python
d_weights = 2 * np.dot(x_train.T, error) / len(x_train)
```

Gradient des biais :

```python
d_bias = 2 * np.mean(error, axis=0, keepdims=True)
```

### Pourquoi axis=0 ?

Nous calculons une erreur moyenne pour chaque sortie :

```text
Q(avancer)
Q(reculer)
```

afin de mettre à jour chaque biais séparément.

### Pourquoi keepdims=True ?

Cela conserve la shape :

```text
(1, 2)
```

afin qu'elle corresponde à celle de :

```python
bias
```

---

## Apprentissage

À chaque itération :

```text
Prédiction
↓
Erreur
↓
Coût
↓
Gradients
↓
Mise à jour des paramètres
```

Le coût diminue progressivement :

```text
Iteration 0   : 49.49
Iteration 100 : 0.0239
```

Le réseau converge rapidement.

---

## Résultat obtenu

Après entraînement :

```text
Position 0 :
Q(avancer) ≈ 6.89
Q(reculer) ≈ 5.41

Position 1 :
Q(avancer) ≈ 7.63
Q(reculer) ≈ 5.81

Position 2 :
Q(avancer) ≈ 8.36
Q(reculer) ≈ 6.22

Position 3 :
Q(avancer) ≈ 9.10
Q(reculer) ≈ 6.62

Position 4 :
Q(avancer) ≈ 9.83
Q(reculer) ≈ 7.03
```

Le réseau reproduit correctement les tendances observées dans la Q-Table.

---

## Ce que j'ai appris

À la fin de ce projet, je comprends :

* pourquoi un DQN prédit plusieurs Q-values ;
* pourquoi il y a une sortie par action ;
* comment construire un dataset multi-sorties ;
* comment adapter les shapes des poids et des biais ;
* comment calculer les gradients pour plusieurs sorties ;
* comment comparer plusieurs Q-values pour choisir une action.

---

## Préparation du projet suivant

Dans ce projet, le réseau apprend à partir de Q-values déjà connues.

Dans un vrai DQN :

```text
Le réseau ne connaît aucune Q-value au départ.
```

Il devra apprendre directement à partir :

```text
État
↓
Action
↓
Récompense
↓
Nouvel état
↓
Mise à jour du réseau
```

Le prochain projet rapprochera encore davantage notre réseau du fonctionnement réel d'un DQN.
