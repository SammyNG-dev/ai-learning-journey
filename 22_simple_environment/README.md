# Projet 22 — Environnement simple

## 🎯 Objectif

Créer un environnement minimal pour introduire les bases du Reinforcement Learning.

L'objectif est de comprendre comment un agent interagit avec un environnement à travers des actions et comment l'environnement évolue en réponse.

---

## 🧩 Description

Ce programme :

- crée un monde composé de plusieurs positions
- place un agent au début du monde
- définit une position objectif
- permet à l'agent d'effectuer des actions :
  - `AVANCER`
  - `RECULER`
- empêche l'agent de sortir des limites du monde
- vérifie si l'objectif est atteint

---

## 🛠️ Technologies utilisées

- Python

---

## 🧠 Concepts appris

### 1. Environnement

L'environnement représente le monde dans lequel évolue l'agent.

Dans ce projet :

```text
[ A ][   ][   ][ G ]
```

- `A` = Agent
- `G` = Goal (objectif)

---

### 2. État

L'état décrit la situation actuelle de l'environnement.

Exemple :

```python
agent_position = 2
```

L'état répond à la question :

```text
"Où se trouve l'agent actuellement ?"
```

---

### 3. Agent

L'agent est l'entité qui agit dans l'environnement.

Son but est d'atteindre l'objectif.

---

### 4. Actions

L'agent peut effectuer deux actions :

```text
AVANCER
RECULER
```

Ces actions modifient potentiellement son état.

---

### 5. Transition d'état

Une action peut produire un nouvel état.

Exemple :

```text
Position 1
↓ AVANCER
Position 2
```

L'environnement applique ses règles pour produire ce nouvel état.

---

### 6. Limites du monde

L'agent ne peut pas sortir du monde.

Exemples :

```python
if action == "RECULER" and agent_position > 0:
    agent_position -= 1
```

```python
if action == "AVANCER" and agent_position < world_size - 1:
    agent_position += 1
```

Ces règles empêchent les déplacements invalides.

---

### 7. Objectif

L'environnement possède une position cible :

```python
goal_position = world_size - 1
```

L'objectif est atteint lorsque :

```python
agent_position == goal_position
```

---

### 8. Séparation des responsabilités

L'agent choisit une action :

```text
AVANCER
```

L'environnement applique les règles :

```text
déplacement autorisé ou refusé
```

Cette séparation est fondamentale en Reinforcement Learning.

---

## 📌 Exemple

État initial :

```text
[ A ][   ][   ][ G ]
```

Action :

```text
AVANCER
```

Nouvel état :

```text
[   ][ A ][   ][ G ]
```

Puis :

```text
[   ][   ][ A ][ G ]
```

Puis :

```text
[   ][   ][   ][ A ]
```

Objectif atteint.

---

## 📚 Ce que j'ai retenu

- un environnement décrit le monde dans lequel évolue un agent
- un état représente la situation actuelle de ce monde
- un agent agit à travers des actions
- une action peut modifier l'état de l'environnement
- les règles de l'environnement déterminent les transitions possibles
- un objectif permet de définir une condition de réussite
- l'agent choisit les actions, l'environnement applique les règles

---

## 🔗 Lien avec l'objectif final

Dans Sonic 2 :

- l'environnement sera le niveau du jeu
- l'état contiendra des informations sur Sonic et le monde
- l'agent choisira des actions (droite, gauche, saut, etc.)
- l'environnement appliquera ces actions
- un nouvel état sera produit

Ce projet constitue la première version simplifiée d'un environnement de Reinforcement Learning.