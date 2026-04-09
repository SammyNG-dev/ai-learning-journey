# Projet 6 — Grid Value Detection

## 🎯 Objectif

Détecter la position d’une valeur spécifique dans une matrice NumPy.

---

## 🧩 Description

Ce programme :

- génère une matrice 10x10 contenant des valeurs aléatoires (0 ou 1)
- considère cette matrice comme un écran simplifié
- détecte toutes les positions où la valeur est égale à `1`
- affiche les coordonnées de ces positions

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Détection dans une matrice

- utilisation de `np.argwhere()`
- identification des positions correspondant à une condition

---

### 2. Coordonnées (ligne, colonne)

- une matrice 2D utilise deux indices :
  - ligne (`i`)
  - colonne (`j`)
- chaque position est représentée sous la forme `[ligne, colonne]`

---

### 3. Interprétation des données

- la matrice représente un écran simplifié
- les valeurs sont interprétées :
  - `0` → vide
  - `1` → obstacle

---

### 4. Passage des données à la logique

- détection d’un élément → première étape vers la prise de décision
- base du fonctionnement d’un agent (perception)

---

## 📌 Exemple de sortie

```
Obstacles trouves aux positions :
[0 3]
[1 5]
[4 2]
[7 8]
...
```
---

## 📚 Ce que j'ai retenu

- un programme peut repérer des éléments dans une grille
- chaque position correspond à une coordonnée (ligne, colonne)
- les données doivent être interprétées pour avoir du sens
- c’est une étape clé pour créer un agent capable d’interagir avec un environnement
---