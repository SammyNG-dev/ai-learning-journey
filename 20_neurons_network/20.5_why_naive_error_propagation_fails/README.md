# Projet 20.5 — Pourquoi cette propagation est incomplète (celle du 20.4)

## 🎯 Objectif

Comprendre pourquoi corriger uniquement le neurone final ne suffit pas pour entraîner correctement un réseau multicouche.

---

## 🧩 Description

Ce programme :

- utilise une couche cachée composée de neurones figés
- construit un dataset caché (`final_dataset`)
- entraîne uniquement le neurone final
- observe :
  - le coût final
  - les prédictions
  - la stabilité des résultats

Le but est d’identifier les limites de cette méthode naïve.

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Dépendance aux features cachées

Le neurone final apprend à partir de :

```python
final_dataset
```

Mais ce dataset est produit par des neurones cachés aléatoires :

```python
w1
b1
w2
b2
```

---

### 2. Couche cachée figée

Les neurones cachés :

- produisent les features
- mais ne sont jamais corrigés

Leurs poids restent constants pendant tout l’apprentissage.

---

### 3. Limitation du neurone final

Le neurone final peut modifier :

```python
w_final
b_final
```

mais il ne peut pas améliorer les features cachées.

Il doit travailler avec les données qu’il reçoit.

---

### 4. Features cachées mauvaises

Certaines initialisations peuvent produire :

- des features peu utiles
- des features presque identiques
- des features qui séparent mal les données

Dans ce cas :

```text
le neurone final est fortement limité
```

---

### 5. Instabilité des résultats

En relançant plusieurs fois le programme :

- les prédictions changent
- le coût reste souvent bloqué
- les performances varient selon les poids aléatoires

---

### 6. Coût bloqué

Le coût reste souvent proche de :

```text
0.25
```

Cela montre que :

```text
le réseau n’apprend pas correctement le problème
```

malgré les corrections du neurone final.

---

### 7. Problème fondamental découvert

Le système actuel ne peut pas dire :

```text
“les neurones cachés produisent de mauvaises features”
```

Donc :

```text
les neurones cachés doivent probablement être corrigés eux aussi
```

---

## 📌 Exemple d’observations

```text
cost_final: 0.24997
predictions: [0 1 0 1]
y_true: [1 1 0 0]
```

ou :

```text
cost_final: 0.25005
predictions: [0 1 1 0]
y_true: [1 1 0 0]
```

Les résultats changent selon l’initialisation des neurones cachés.

---

## 📚 Ce que j’ai retenu

- le neurone final dépend entièrement des features cachées
- des neurones cachés aléatoires peuvent bloquer l’apprentissage
- corriger uniquement la sortie est insuffisant
- un réseau multicouche doit probablement corriger aussi ses couches cachées
- cette limitation conduit naturellement vers la rétropropagation