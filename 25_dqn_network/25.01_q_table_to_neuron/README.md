# P25.1 - Remplacer une Q-Table par un neurone

## Objectif

Dans le projet précédent, nous avons utilisé une Q-Table pour mémoriser les valeurs associées à chaque action.

Exemple :

```python
q_table[(0, "avancer")] = 7.05
q_table[(1, "avancer")] = 7.56
q_table[(2, "avancer")] = 8.20
```

Cette approche fonctionne bien pour les petits environnements.

Cependant, lorsqu'un environnement devient très grand, le nombre d'états possibles explose rapidement.

L'objectif de ce projet est de découvrir comment un réseau de neurones peut remplacer progressivement une Q-Table.

---

## Pourquoi remplacer la Q-Table ?

Une Q-Table mémorise chaque situation individuellement.

Exemple :

```text
Position 0 → 7.05
Position 1 → 7.56
Position 2 → 8.20
Position 3 → 9.00
Position 4 → 10.00
```

Cela fonctionne avec quelques positions.

Mais dans un jeu comme Sonic :

* la position du personnage change constamment ;
* la vitesse change ;
* les ennemis se déplacent ;
* les obstacles sont nombreux ;
* le nombre d'états possibles devient gigantesque.

Il devient alors impossible de mémoriser chaque situation dans une simple table.

---

## Idée du projet

Au lieu de mémoriser chaque valeur :

```text
Position → Q-value
```

nous allons entraîner un neurone à apprendre cette relation.

L'objectif est que le neurone soit capable de prédire :

```text
Position 2 → environ 8.20
Position 3 → environ 9.00
Position 4 → environ 10.00
```

sans utiliser de Q-Table.

---

## Dataset utilisé

Nous réutilisons les Q-values obtenues dans le projet précédent.

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
    [7.05],
    [7.56],
    [8.20],
    [9.00],
    [10.00]
])
```

Chaque ligne représente :

```text
Position → Q-value associée
```

---

## Architecture du réseau

Pour ce premier projet, un seul neurone est suffisant.

Entrée :

```text
Position
```

Sortie :

```text
Q-value estimée
```

Le calcul effectué est :

```python
y_pred = x * weight + bias
```

---

## Pourquoi aucune fonction d'activation ?

Dans les projets précédents, nous avons utilisé la fonction sigmoid pour produire une probabilité comprise entre 0 et 1.

Ici, nous voulons prédire des valeurs comme :

```text
7.05
8.20
10.00
```

La sigmoid ne convient donc pas.

La sortie du neurone est directement :

```python
y_pred = z
```

On parle alors de sortie linéaire.

---

## Fonction de coût

Nous utilisons l'erreur quadratique moyenne :

```python
cost = np.mean(error ** 2)
```

avec :

```python
error = y_pred - y_train
```

Cette fonction mesure l'écart entre :

* les Q-values prédites ;
* les Q-values attendues.

---

## Apprentissage

Le neurone apprend progressivement grâce à la descente de gradient.

À chaque itération :

```text
Prédiction
↓
Erreur
↓
Coût
↓
Gradient
↓
Mise à jour des paramètres
```

Les paramètres modifiés sont :

```python
weight
bias
```

---

## Résultat obtenu

Après plusieurs centaines d'itérations, le coût diminue fortement.

Exemple :

```text
75.67
3.50
1.07
0.33
0.11
0.04
0.02
```

Le neurone apprend progressivement à reproduire les Q-values de la Q-Table.

---

## Ce que j'ai appris

À la fin de ce projet, je comprends :

* pourquoi une Q-Table devient insuffisante dans un grand environnement ;
* comment transformer une Q-Table en dataset ;
* comment entraîner un neurone à prédire une Q-value ;
* pourquoi une sortie linéaire est nécessaire ;
* comment utiliser l'erreur quadratique moyenne ;
* comment un réseau de neurones peut remplacer progressivement une Q-Table.

---

## Préparation du projet suivant

Dans ce projet, le neurone ne prédit qu'une seule Q-value.

Dans le projet suivant, le réseau devra être capable de prédire plusieurs Q-values simultanément :

```text
Q(avancer)
Q(reculer)
```

afin de choisir automatiquement la meilleure action.
