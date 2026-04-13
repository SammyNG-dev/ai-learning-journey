# Projet 10 — Multi Direction Movement

## 🎯 Objectif

Permettre au joueur de se déplacer dans 4 directions (haut, bas, gauche, droite) en tenant compte des obstacles et des limites de la grille.

---

## 🧩 Description

Ce programme :

- génère une grille 10x10 contenant des valeurs aléatoires (`0` ou `1`)
- place un joueur (`2`) sur une case vide aléatoire
- choisit une direction aléatoire :
  - `"UP"`
  - `"DOWN"`
  - `"LEFT"`
  - `"RIGHT"`
- vérifie si le déplacement est possible :
  - pas hors de la grille
  - pas sur un obstacle
- effectue le déplacement si valide
- affiche :
  - la grille initiale
  - la direction choisie
  - la position finale (si déplacement)
  - la grille après mouvement

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Gestion multi-directionnelle

- chaque direction modifie une coordonnée spécifique :
  - `UP` → ligne - 1
  - `DOWN` → ligne + 1
  - `LEFT` → colonne - 1
  - `RIGHT` → colonne + 1

---

### 2. Vérification des limites

```python
if player_row == 0        # bord haut
if player_row == rows - 1 # bord bas
if player_col == 0        # bord gauche
if player_col == cols - 1 # bord droit
```

- empêche les accès hors de la grille
- évite les erreurs d’index

---

### 3. Gestion des obstacles

```python
grid[next_row][next_col] == 1
```

- bloque le déplacement si la case est occupée

---

### 4. Mise à jour de la position

```python
grid[player_row][player_col] = 2
grid[ancienne_position] = 0
```

- le joueur est déplacé dans la grille
- l’ancienne position est effacée

---

### 5. Synchronisation des états

- `player_row` / `player_col` → position logique
- `grid` → représentation visuelle
- les deux doivent rester cohérents

---

## 📌 Exemple de sortie

```text
Grille initiale :
[[1 1 1 0 1 1 1 1 1 1]
 [1 0 0 0 0 0 1 0 1 1]
 [1 0 0 0 0 0 0 1 0 1]
 [1 0 1 1 0 1 0 1 0 1]
 [1 1 0 0 1 1 0 0 0 0]
 [1 0 2 0 1 0 1 1 1 0]
 [0 0 1 1 0 1 0 0 1 1]
 [0 1 0 1 1 1 1 0 0 0]
 [1 0 0 0 0 1 0 0 1 1]
 [1 1 1 0 1 0 1 0 0 0]]

Input : LEFT

Position initiale : (5, 2)

Position atteinte : (5, 1)

Grille après mouvement :

[[1 1 1 0 1 1 1 1 1 1]
 [1 0 0 0 0 0 1 0 1 1]
 [1 0 0 0 0 0 0 1 0 1]
 [1 0 1 1 0 1 0 1 0 1]
 [1 1 0 0 1 1 0 0 0 0]
 [1 2 0 0 1 0 1 1 1 0]
 [0 0 1 1 0 1 0 0 1 1]
 [0 1 0 1 1 1 1 0 0 0]
 [1 0 0 0 0 1 0 0 1 1]
 [1 1 1 0 1 0 1 0 0 0]]
```

---

## 📚 Ce que j'ai retenu

- un déplacement dépend de la direction choisie
- il faut vérifier les limites avant d’accéder à une matrice
- un mouvement valide dépend de plusieurs conditions (bord + obstacle)
- la gestion multi-directionnelle est plus complexe qu’un mouvement simple
- garder une logique claire évite les erreurs

---