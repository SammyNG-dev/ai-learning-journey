# 20.final_survival_ai

## Objectif

Ce projet a pour objectif de construire un réseau de neurones plus grand que celui utilisé pour apprendre XOR.

L'objectif n'est pas de créer une IA réaliste, mais de mettre en pratique :

- les couches cachées ;
- les matrices de poids ;
- la rétropropagation matricielle ;
- l'apprentissage d'une logique de décision.

Le réseau devra apprendre à décider s'il faut :

- combattre ;
- ou fuir.

à partir de plusieurs informations décrivant une situation.

---

## Problème

Nous incarnons un personnage dans un jeu vidéo.

Pour chaque situation, nous devons décider :

```text
0 = fuir
1 = combattre
```

Les informations disponibles sont :

```text
vie élevée ?
faim élevée ?
beaucoup de munitions ?
danger loin ?
ennemi plus fort ?
boss ?
```

Chaque information est représentée par :

```text
0 = non
1 = oui
```

---

## Dataset

Le dataset est construit manuellement.

Chaque ligne représente une situation.

Exemple :

```python
[1, 0, 1, 1, 0, 0]
```

signifie :

```text
vie élevée
faim faible
beaucoup de munitions
danger loin
ennemi moins fort
pas un boss
```

La sortie associée est :

```python
1
```

ce qui signifie :

```text
combattre
```

---

## Architecture du réseau

Le réseau possède :

```text
6 entrées
↓
4 neurones
↓
2 neurones
↓
1 neurone de sortie
```

Soit :

```text
6 → 4 → 2 → 1
```

---

## Paramètres du réseau

### Couche 1

```text
6 entrées → 4 neurones
```

Nombre de poids :

```text
6 × 4 = 24
```

Nombre de biais :

```text
4
```

---

### Couche 2

```text
4 entrées → 2 neurones
```

Nombre de poids :

```text
4 × 2 = 8
```

Nombre de biais :

```text
2
```

---

### Couche finale

```text
2 entrées → 1 neurone
```

Nombre de poids :

```text
2 × 1 = 2
```

Nombre de biais :

```text
1
```

---

### Total

```text
34 poids
7 biais
41 paramètres
```

---

## Fonction d'activation

Tous les neurones utilisent la fonction sigmoid.

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

Sa dérivée :

```python
def sigmoid_derivative(s):
    return s * (1 - s)
```

---

## Forward Propagation

Les données traversent successivement :

```text
Couche 1
↓
Couche 2
↓
Couche finale
```

Exemple :

```python
hidden1 = neuron(x_train, weights1, bias1)

hidden2 = neuron(hidden1, weights2, bias2)

output = neuron(hidden2, weights_final, bias_final)
```

---

## Fonction de coût

Le réseau utilise l'erreur quadratique moyenne :

```python
cost = np.mean(error ** 2)
```

avec :

```python
error = output - y_train
```

---

## Backpropagation

L'erreur est propagée depuis la sortie vers les couches précédentes.

### Delta final

```python
final_delta = error * sigmoid_derivative(output_final)
```

### Delta couche 2

```python
delta_hidden_neurons_layer2 = (
    np.dot(final_delta, weights_final.T)
    * sigmoid_derivative(output_hidden_neurons_layer2)
)
```

### Delta couche 1

```python
delta_hidden_neurons_layer1 = (
    np.dot(delta_hidden_neurons_layer2, weights2.T)
    * sigmoid_derivative(output_hidden_neurons_layer1)
)
```

---

## Calcul des gradients

### Couche 1

```python
dw1 = np.dot(x_train.T, delta_hidden_neurons_layer1) / len(x_train)

db1 = np.mean(delta_hidden_neurons_layer1, axis=0)
```

### Couche 2

```python
dw2 = np.dot(
    output_hidden_neurons_layer1.T,
    delta_hidden_neurons_layer2
) / len(x_train)

db2 = np.mean(delta_hidden_neurons_layer2, axis=0)
```

### Couche finale

```python
dw_final = np.dot(
    output_hidden_neurons_layer2.T,
    final_delta
) / len(x_train)

db_final = np.mean(final_delta, axis=0)
```

---

## Mise à jour des paramètres

```python
weights = weights - lr * dw

bias = bias - lr * db
```

---

## Test du réseau

Après l'entraînement, le réseau est testé sur des situations :

- déjà présentes dans le dataset ;
- jamais vues pendant l'entraînement.

Les prédictions sont obtenues avec :

```python
predictions = (output > 0.5).astype(int)
```

Interprétation :

```text
0 = fuir
1 = combattre
```

---

## Ce que ce projet permet d'apprendre

Ce projet introduit :

- les matrices de poids ;
- les couches cachées multiples ;
- la rétropropagation matricielle ;
- la conception d'un dataset ;
- la généralisation sur des exemples non vus ;
- la prise de décision à partir de plusieurs paramètres.

Il constitue une étape importante avant les projets de classification d'images et les futurs agents capables d'interagir avec un environnement.