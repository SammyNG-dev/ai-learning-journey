# Projet 7 — Simple Decision Agent

## 🎯 Objectif

Mettre en place un système de décision simple basé sur l’état d’une grille.

---

## 🧩 Description

Ce programme :

- génère une grille 10x10 contenant des valeurs aléatoires (`0` ou `1`)
- place un joueur dans la grille (valeur `2`)
- observe la case située devant le joueur (à droite)
- prend une décision en fonction de cette case :
  - obstacle → "SAUTER"
  - sinon → "AVANCER"

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Représentation d’un agent

- `2` représente le joueur dans la grille
- la position du joueur est définie par ses coordonnées `(ligne, colonne)`

---

### 2. Perception

Lecture d’une case spécifique dans la grille :

```python
grid[player_row][player_column + 1]
```

---

### 3. Interprétation

- `0` → espace libre
- `1` → obstacle

---

### 4. Décision

Transformation d’une information en action :

- obstacle → SAUTER
- sinon → AVANCER

---

### 5. Cycle d’un agent

- perception → lecture de la grille
- interprétation → compréhension de la situation
- décision → choix d’une action

---

## 📌 Exemple de sortie

```text
Grille :
[[0 1 0 ...]
 [1 0 1 ...]
 ...]

Action :
AVANCER
```

---

## 📚 Ce que j'ai retenu

- un agent peut prendre une décision simple à partir d’un environnement
- la logique perception → interprétation → décision est fondamentale
- c’est la base du fonctionnement d’une IA
- même une IA complexe repose sur ce principe simple