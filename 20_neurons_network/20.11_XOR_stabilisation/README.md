# Projet 20.11 — Stabilisation de XOR

## 🎯 Objectif

Stabiliser l'apprentissage de XOR.

Ce projet consiste à recoder entièrement le projet 20.10 afin de vérifier que tous les mécanismes de la rétropropagation sont compris et peuvent être reconstruits sans aide.

Deux améliorations sont ajoutées :

- une initialisation reproductible avec `np.random.seed(42)`
- un jeu de données de test séparé de l'entraînement

---

## 🧩 Description

Le réseau est composé de :

```text
2 entrées
→ 2 neurones cachés
→ 1 neurone final
```

Le réseau apprend la fonction XOR :

```text
0 XOR 0 = 0
1 XOR 0 = 1
1 XOR 1 = 0
0 XOR 1 = 1
```

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts consolidés

### 1. Reconstruction complète du réseau

Le réseau a été recodé entièrement à partir de zéro.

Toutes les étapes ont été réécrites :

- forward propagation
- calcul de l'erreur
- calcul des deltas
- calcul des gradients
- mise à jour des poids
- prédiction finale

---

### 2. Rétropropagation complète

Le réseau calcule :

```text
erreur finale
→ delta final
→ deltas cachés
→ gradients
→ correction des poids
```

Le neurone final apprend.

Les neurones cachés apprennent également.

---

### 3. Importance du delta

Le delta représente le signal local de correction.

Pour le neurone final :

```python
delta_final = error * sigmoid_derivative(final_output)
```

Pour les neurones cachés :

```python
hidden_delta =
delta_suivant
×
poids_de_connexion
×
dérivée_locale
```

---

### 4. Importance du learning rate

Un learning rate trop faible ralentit fortement l'apprentissage.

Des expérimentations ont montré que :

```python
lr = 0.1
```

apprenait très lentement.

Alors que :

```python
lr = 1.0
```

permettait d'apprendre XOR beaucoup plus efficacement.

---

### 5. Compréhension de `np.random.seed()`

Les poids sont initialisés aléatoirement :

```python
np.random.rand()
```

Par défaut, chaque exécution produit des poids différents.

L'instruction :

```python
np.random.seed(42)
```

force NumPy à générer toujours les mêmes poids initiaux.

Cela permet :

- d'obtenir les mêmes résultats à chaque exécution
- de reproduire les expériences
- de comparer les modifications du code sans influence de l'aléatoire

---

### 6. Jeu de données de test

Un second dataset est utilisé :

```python
x_test
y_test
```

Les exemples sont les mêmes que pour l'entraînement mais dans un ordre différent.

L'objectif est de vérifier que le réseau a appris la logique XOR et ne dépend pas simplement de l'ordre des lignes du dataset.

---

### 7. Observation du coût

Le coût est affiché pendant l'entraînement :

```python
cost = np.mean(error ** 2)
```

Cela permet de visualiser :

- la vitesse d'apprentissage
- la stabilité du réseau
- l'influence du learning rate

---

## 📌 Ce que j'ai retenu

- un réseau multicouche apprend grâce à la rétropropagation
- les neurones cachés ne connaissent jamais directement `y_true`
- les deltas cachés sont calculés à partir du delta de la couche suivante
- les gradients permettent de corriger les poids
- le learning rate influence fortement la vitesse d'apprentissage
- `np.random.seed()` permet de reproduire exactement une expérience
- il est important de séparer conceptuellement entraînement et test

---

## Résultat obtenu

Le réseau apprend correctement la fonction XOR :

```text
[0, 0] → 0
[1, 0] → 1
[1, 1] → 0
[0, 1] → 1
```

Les prédictions finales sont cohérentes avec les valeurs attendues.

Le coût devient très faible après entraînement.

---

## Validation pédagogique

À la fin de ce projet, je suis capable de :

- reconstruire un réseau multicouche simple
- implémenter la rétropropagation complète
- expliquer le rôle des deltas
- expliquer le rôle des gradients
- expliquer le rôle du learning rate
- expliquer le rôle de `np.random.seed()`
- entraîner un réseau de neurones à apprendre XOR