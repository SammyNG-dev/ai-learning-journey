# Projet 23 — Agent avec récompense

## 🎯 Objectif

Ajouter un système de récompense à un environnement simple.

L'objectif est de comprendre comment un environnement peut indiquer à un agent si une action a été bénéfique ou non.

---

## 🧩 Description

Ce programme :

- crée un environnement linéaire
- place un agent dans cet environnement
- définit une position objectif
- permet à l'agent d'effectuer une action :
  - `AVANCER`
  - `RECULER`
- calcule la distance à l'objectif avant et après l'action
- attribue une récompense selon le résultat obtenu

---

## 🛠️ Technologies utilisées

- Python

---

## 🧠 Concepts appris

### 1. Récompense

La récompense est un signal envoyé à l'agent après une action.

Elle indique si le résultat obtenu est :

- bon
- neutre
- mauvais

Exemples :

```text
+10 → objectif atteint
+1  → progression
0   → aucune progression