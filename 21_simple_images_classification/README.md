# 21_simple_image_classification

## Objectif

Ce projet introduit la classification d'images simples.

L'objectif n'est pas encore de reconnaître de vraies images, mais de comprendre comment :

- représenter une image sous forme de nombres ;
- transformer une image en entrée pour un réseau de neurones ;
- construire un dataset d'images ;
- entraîner un réseau à distinguer plusieurs catégories.

---

## Problème

Le réseau doit distinguer :

```text
0 = barre verticale
1 = barre horizontale
```

Les images sont volontairement très simples :

```text
3 × 3 pixels
```

---

## Représentation d'une image

Une image est représentée par une matrice.

Exemple :

```python
[
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
```

représente une barre verticale.

---

## Flatten

Un réseau de neurones classique ne travaille pas directement avec une matrice.

L'image est donc aplatie :

```python
[
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
```

↓

```python
[0, 1, 0, 0, 1, 0, 0, 1, 0]
```

On obtient :

```text
9 features
```

---

## Dataset

### Images verticales

```python
vertical_1
vertical_2
vertical_3
```

### Images horizontales

```python
horizontal_1
horizontal_2
horizontal_3
```

---

## x_train

Le dataset contient :

```text
6 images
```

Chaque image possède :

```text
9 pixels
```

Donc :

```python
x_train.shape
```

vaut :

```text
(6, 9)
```

---

## y_train

Les labels sont :

```text
verticale   → 0
horizontale → 1
```

```python
y_train = np.array([
    0,
    0,
    0,
    1,
    1,
    1
])
```

Après transformation :

```python
y_train = y_train.reshape(-1, 1)
```

Shape :

```text
(6, 1)
```

---

## Première tentative

Architecture :

```text
9 → 1
```

Résultat :

```text
Le coût reste proche de 0.25.
```

Le réseau prédit approximativement :

```text
0.5 pour tous les exemples.
```

Conclusion :

```text
Un seul neurone ne suffit pas.
```

---

## Architecture retenue

Architecture :

```text
9 → 2 → 1
```

Le réseau possède :

```text
9 entrées
↓
2 neurones cachés
↓
1 neurone de sortie
```

---

## Paramètres du réseau

### Couche cachée

```text
9 entrées → 2 neurones
```

Nombre de poids :

```text
9 × 2 = 18
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
20 poids
3 biais
23 paramètres
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

```python
output_hidden_neurons_layer = neuron(
    x_train,
    weights1,
    bias1
)

output_final_neuron = neuron(
    output_hidden_neurons_layer,
    weights_final,
    bias_final
)
```

Shapes :

```text
x_train                         (6, 9)
↓
couche cachée                   (6, 2)
↓
sortie                          (6, 1)
```

---

## Fonction de coût

Erreur :

```python
error = output_final_neuron - y_train
```

Coût :

```python
cost = np.mean(error ** 2)
```

---

## Backpropagation

### Delta final

```python
delta_final = (
    error
    * sigmoid_derivative(output_final_neuron)
)
```

### Delta couche cachée

```python
delta_hidden_neurons_layer = (
    np.dot(delta_final, weights_final.T)
    * sigmoid_derivative(output_hidden_neurons_layer)
)
```

---

## Gradients

### Couche cachée

```python
dw1 = np.dot(
    x_train.T,
    delta_hidden_neurons_layer
) / len(x_train)

db1 = np.mean(
    delta_hidden_neurons_layer,
    axis=0
)
```

---

### Couche finale

```python
dw_final = np.dot(
    output_hidden_neurons_layer.T,
    delta_final
) / len(x_train)

db_final = np.mean(
    delta_final,
    axis=0
)
```

---

## Mise à jour des paramètres

```python
weights = weights - lr * dw

bias = bias - lr * db
```

---

## Résultat

Après entraînement :

```python
[[0]
 [0]
 [0]
 [1]
 [1]
 [1]]
```

Le réseau classe correctement toutes les images du dataset.

---

## Ce que ce projet permet d'apprendre

Ce projet introduit :

- la représentation numérique d'une image ;
- le flatten d'une image ;
- les pixels comme features ;
- la classification binaire d'images ;
- l'utilisation d'un réseau multicouche pour reconnaître des motifs simples ;
- la transition entre données abstraites et données visuelles.

---

## Concepts importants découverts

### Image → Features

Une image peut être transformée en vecteur de nombres.

### Couche d'entrée

Le nombre d'entrées correspond au nombre de pixels.

```text
3 × 3 = 9 pixels
↓
9 entrées
```

### Frontière de décision

Un seul neurone ne suffit pas toujours.

Le projet montre qu'une couche cachée peut être nécessaire pour séparer correctement certaines catégories.

---

## Préparation du projet suivant

Ce projet prépare :

- les images plus complexes ;
- les datasets plus grands ;
- les notions de classification ;
- les futurs réseaux spécialisés pour les images.