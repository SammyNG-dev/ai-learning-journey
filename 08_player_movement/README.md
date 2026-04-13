# Projet 8 — Player Movement

## 🎯 Objectif

Implémenter le déplacement réel d’un joueur dans une grille en fonction de l’environnement.

---

## 🧩 Description

Ce programme :

- génère une grille 10x10 contenant des valeurs aléatoires (`0` ou `1`)
- place un joueur dans la grille (valeur `2`)
- observe la case située devant le joueur (à droite)
- déplace le joueur si la case est libre (`0`)
- ne fait rien si un obstacle (`1`) est présent
- met à jour la grille en conséquence

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Représentation du joueur

- `2` représente le joueur dans la grille
- sa position est stockée avec deux variables :
  - `player_row`
  - `player_column`

---

### 2. Perception

Lecture de la case devant le joueur :

```python
grid[player_row][player_column + 1]
```

---

### 3. Décision

- si la case vaut `0` → déplacement possible
- si la case vaut `1` → obstacle → pas de déplacement

---

### 4. Action (déplacement)

```python
player_column += 1
grid[player_row][player_column] = 2
grid[player_row][player_column - 1] = 0
```

- mise à jour de la position logique (`player_column`)
- mise à jour de la grille :
  - nouvelle position → `2`
  - ancienne position → `0`

---

### 5. Synchronisation des états

- la position du joueur est représentée à deux niveaux :
  - dans la grille (visuel)
  - dans les variables (logique)
- les deux doivent rester cohérents

---

## 📌 Exemple de sortie

```text
Avant :
[[0 1 0 ...]
 [1 0 1 ...]
 ...]

Après déplacement :
[[0 1 0 ...]
 [1 0 1 ...]
 ...]
```

---

## 📚 Ce que j'ai retenu

- un agent peut agir sur son environnement
- il faut mettre à jour à la fois :
  - la position logique
  - la représentation visuelle
- un déplacement implique toujours :
  - ajouter le joueur à une nouvelle position
  - supprimer l’ancienne position
- c’est une étape clé vers une simulation dynamique

---