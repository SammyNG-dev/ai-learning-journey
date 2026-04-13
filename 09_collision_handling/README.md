# Projet 9 — Collision Handling

## 🎯 Objectif

Gérer correctement les collisions, les limites de la grille et suivre précisément le trajet du joueur.

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
- enregistre le trajet du joueur

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

```python
if player_column == cols - 1:
```

- empêche de sortir de la grille
- évite les erreurs d’index

---

### 3. Initialisation contrôlée

```python
while True:
    player_row = np.random.randint(0, rows)
    player_column = np.random.randint(0, cols)

    if grid[player_row][player_column] == 0:
        grid[player_row][player_column] = 2
        initial_position = (player_row, player_column)
        break
```

- le joueur est placé uniquement sur une case vide
- évite d’écraser un obstacle
- enregistre la position initiale séparément

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

### 6. Historique du trajet

```python
player_way.append((player_row, player_column))
```

- enregistre chaque déplacement du joueur
- permet de reconstruire le trajet dans l’ordre

---

### 7. Séparation des données

- `initial_position` → point de départ
- `player_way` → déplacements uniquement

- permet de distinguer :
  - position initiale
  - trajet

---

## 📌 Exemple de sortie

```text
[[1 1 0 0 1 1 0 1 1 0]
 [1 0 0 0 1 1 1 0 1 0]
 [0 0 0 1 1 1 1 0 0 0]
 [0 1 0 0 0 1 1 1 1 1]
 [0 1 1 0 1 0 0 0 1 1]
 [1 0 0 0 1 0 0 1 2 0]
 [0 1 0 1 0 0 0 1 1 0]
 [1 1 1 0 1 1 1 0 1 1]
 [1 0 0 1 0 0 1 1 1 1]
 [0 0 0 0 1 0 1 1 0 1]]

[[1 1 0 0 1 1 0 1 1 0]
 [1 0 0 0 1 1 1 0 1 0]
 [0 0 0 1 1 1 1 0 0 0]
 [0 1 0 0 0 1 1 1 1 1]
 [0 1 1 0 1 0 0 0 1 1]
 [1 0 0 0 1 0 0 1 0 2]
 [0 1 0 1 0 0 0 1 1 0]
 [1 1 1 0 1 1 1 0 1 1]
 [1 0 0 1 0 0 1 1 1 1]
 [0 0 0 0 1 0 1 1 0 1]]

BORD

Trajet :
Position initiale : (5, 8)
Mouvements : [(5, 9)]
```

---

## 📚 Ce que j'ai retenu

- un agent doit vérifier son environnement avant d’agir
- il faut gérer les limites pour éviter les erreurs
- un déplacement valide dépend de plusieurs conditions
- la grille représente l’état actuel du système
- séparer l’état courant (grille) de l’historique (trajet) rend le système plus clair
- une bonne structure de données simplifie la logique du programme

---