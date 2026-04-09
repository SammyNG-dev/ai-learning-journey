# Projet 5 — Grid Screen Simulation

## 🎯 Objectif

Simuler un écran de jeu simplifié à l’aide d’une matrice NumPy.

---

## 🧩 Description

Ce programme :

- génère une matrice 10x10 contenant des valeurs aléatoires (0 ou 1)
- interprète cette matrice comme un écran simplifié
- affiche :
  - la matrice brute
  - une version lisible avec des symboles

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Représentation d’un écran

- un écran peut être vu comme une matrice de pixels
- chaque case correspond à une position dans la grille

---

### 2. Interprétation des données

- les valeurs numériques n’ont pas de sens absolu
- ici :
  - `0` → case vide (`.`)
  - `1` → obstacle (`#`)

---

### 3. Transformation des données

- conversion d’une matrice numérique en affichage lisible
- utilisation de boucles pour parcourir les lignes et colonnes

---

### 4. Formatage de l’affichage

- utilisation de `" ".join()` pour afficher une ligne proprement
- différence entre structure de données et rendu visuel

---

## 📌 Exemple de sortie

```
Matrice NumPy : 
[[0 1 0 0 0 0 0 0 1 1]
 [0 1 1 1 1 1 1 0 0 1]
 [0 1 1 1 1 0 1 0 1 1]
 [1 0 1 1 0 0 0 0 0 0]
 [1 0 0 0 1 1 0 0 0 0]
 [0 0 0 1 1 1 0 0 1 0]
 [0 1 1 1 0 0 0 1 0 1]
 [1 0 1 0 0 0 1 1 1 0]
 [0 1 0 1 1 0 0 1 0 0]
 [0 1 0 1 1 0 0 0 1 1]]

. # . . . . . . # #
. # # # # # # . . #
. # # # # . # . # #
# . # # . . . . . .
# . . . # # . . . .
. . . # # # . . # .
. # # # . . . # . #
# . # . . . # # # .
. # . # # . . # . .
. # . # # . . . # #
```
---

## 📚 Ce que j'ai retenu

- une matrice peut représenter un écran
- les données doivent être interprétées pour être compréhensibles
- NumPy permet de manipuler facilement des grilles de données
- c’est une première étape vers la simulation d’un environnement de jeu

---