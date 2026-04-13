# Projet 11 — Multi Step Agent

## 🎯 Objectif

Simuler un agent capable d’effectuer plusieurs déplacements successifs dans une grille en tenant compte des obstacles et des limites.

---

## 🧩 Description

Ce programme :

- génère une grille 10x10 contenant des valeurs aléatoires (`0` ou `1`)
- place un joueur (`2`) sur une case vide ayant au moins une sortie possible
- effectue une série de déplacements (10 tours)
- à chaque tour :
  - choisit une direction aléatoire (`UP`, `DOWN`, `LEFT`, `RIGHT`)
  - vérifie si le mouvement est possible
  - effectue le déplacement si valide
- affiche la grille après chaque action réussie
- enregistre le trajet du joueur

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Simulation multi-étapes

```python
for _ in range(10):
```

- l’agent agit plusieurs fois
- l’état évolue au fil du temps

---

### 2. Choix aléatoire

```python
np.random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
```

- introduit de l’imprévisibilité
- simule un comportement non déterministe

---

### 3. Gestion des déplacements

- chaque direction modifie une coordonnée :
  - `UP` → ligne - 1
  - `DOWN` → ligne + 1
  - `LEFT` → colonne - 1
  - `RIGHT` → colonne + 1

---

### 4. Vérification des contraintes

- empêche :
  - sortie de la grille
  - déplacement sur un obstacle (`1`)

---

### 5. Mise à jour de la grille

```python
grid[player_row][player_col] = 2
grid[ancienne_position] = 0
```

- le joueur est déplacé
- l’ancienne position est effacée

---

### 6. Validation du point de départ

```python
has_free_neighboor(...)
```

- garantit que le joueur peut bouger au moins une fois
- évite les positions complètement bloquées

---

### 7. Historique du trajet

```python
player_way.append((player_row, player_col))
```

- enregistre chaque mouvement réussi
- permet de reconstruire le chemin

---

### 8. Différence action / mouvement

- une action peut échouer
- un mouvement correspond uniquement à une action réussie

---

## 📌 Exemple de sortie

```text
Grille initiale :
[[0 1 0 ...]
 [1 0 0 ...]
 ...]

Mouvement choisi : RIGHT

Grille après action :
[[0 1 2 ...]
 [1 0 0 ...]
 ...]

...

Position initiale : (9, 4)
[(9, 5), (9, 6), (8, 6)]

Le joueur a fait 3 mouvements.
```

---

## 📚 Ce que j'ai retenu

- un agent agit dans le temps et modifie son environnement
- un environnement contraint limite les possibilités d’action
- toutes les actions ne produisent pas un mouvement
- il est important de distinguer :
  - tentative d’action
  - mouvement réussi
- la qualité d’un point de départ influence fortement le comportement de l’agent
- séparer l’état courant et l’historique améliore la lisibilité

---