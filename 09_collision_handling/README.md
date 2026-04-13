# Projet 9 — Collision Handling

## 🎯 Objectif

Gérer correctement les collisions et les limites de la grille pour empêcher des déplacements invalides du joueur.

---

## 🧩 Description

Ce programme :

- génère une grille 10x10 contenant des valeurs aléatoires (`0` ou `1`)
- place un joueur (`2`) sur une case vide aléatoire
- fait avancer automatiquement le joueur vers la droite
- gère les cas suivants :
  - si le joueur atteint le bord → arrêt
  - si un obstacle est rencontré → arrêt
- met à jour la grille à chaque déplacement

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Gestion des collisions

- détection d’un obstacle (`1`) avant déplacement
- blocage du mouvement si la case est occupée

---

### 2. Gestion des limites

- vérification du bord droit de la grille :
```python
if player_column == cols - 1:
```
- évite les erreurs d’index

---

### 3. Initialisation contrôlée

```python
while True:
    player_row = np.random.randint(0, rows)
    player_column = np.random.randint(0, cols)

    if grid[player_row][player_column] == 0:
        grid[player_row][player_column] = 2
        break
```

- le joueur est placé uniquement sur une case vide
- évite d’écraser un obstacle

---

### 4. Boucle de simulation

```python
while True:
```

- permet au joueur d’avancer tant que les conditions sont valides
- s’arrête avec `break` en cas de collision ou de bord

---

### 5. Mise à jour de l’état

```python
player_column += 1
grid[player_row][player_column] = 2
grid[player_row][player_column - 1] = 0
```

- mise à jour de la position logique
- mise à jour de la grille
- suppression de l’ancienne position

---

## 📌 Exemple de sortie

```text
[[1 1 0 1 1 1 1 1 0 0]
 [1 1 0 0 0 1 0 0 1 0]
 [1 0 1 1 1 1 0 1 0 0]
 [1 0 2 0 1 0 1 0 1 1]
 [1 0 0 1 1 0 1 1 1 1]
 [1 1 0 1 0 1 1 1 0 0]
 [0 1 1 1 1 0 0 1 1 0]
 [0 0 1 1 0 1 0 0 0 1]
 [0 0 1 1 1 1 1 1 1 0]
 [0 0 0 1 1 0 1 0 1 1]]

[[1 1 0 1 1 1 1 1 0 0]
 [1 1 0 0 0 1 0 0 1 0]
 [1 0 1 1 1 1 0 1 0 0]
 [1 0 0 2 1 0 1 0 1 1]
 [1 0 0 1 1 0 1 1 1 1]
 [1 1 0 1 0 1 1 1 0 0]
 [0 1 1 1 1 0 0 1 1 0]
 [0 0 1 1 0 1 0 0 0 1]
 [0 0 1 1 1 1 1 1 1 0]
 [0 0 0 1 1 0 1 0 1 1]]

OBSTACLE
```

---

## 📚 Ce que j'ai retenu

- un agent doit vérifier son environnement avant d’agir
- il faut gérer les limites d’un système pour éviter les erreurs
- un déplacement valide dépend de plusieurs conditions
- la cohérence entre logique et affichage est essentielle
- c’est une étape clé vers une simulation fiable

---