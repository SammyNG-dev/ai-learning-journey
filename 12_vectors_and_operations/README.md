# Projet 12 — Vecteurs et opérations

## 🎯 Objectif

Comprendre ce qu’est un vecteur et savoir effectuer des opérations de base avec NumPy.

---

## 🧩 Description

Ce programme :

- crée deux vecteurs NumPy
- affiche les vecteurs
- effectue différentes opérations :
  - addition
  - soustraction
  - multiplication par un scalaire
  - produit scalaire

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Vecteur

- un vecteur est une liste de nombres
- exemple :
```python
v = np.array([1, 2, 3])
```

---

### 2. Scalaire

- un scalaire est un nombre unique
- exemple : `2`, `-1`, `0.5`

---

### 3. Addition de vecteurs

```python
v1 + v2
```

- addition élément par élément

---

### 4. Soustraction de vecteurs

```python
v1 - v2
```

- soustraction élément par élément

---

### 5. Multiplication par un scalaire

```python
v1 * 2
```

- chaque élément du vecteur est multiplié par le scalaire

---

### 6. Produit scalaire

```python
np.dot(v1, v2)
```

- multiplication élément par élément puis somme des résultats

---

## 📌 Exemple de sortie

```text
Vecteur 1 : [1 2 3]
Vecteur 2 : [4 5 6]

Addition des deux vecteurs : [5 7 9]
Soustraction des deux vecteurs : [-3 -3 -3]
Multiplication par un scalaire : [2 4 6]
Produit scalaire : 32
```

---

## 📚 Ce que j'ai retenu

- un vecteur est une structure de données simple mais puissante
- NumPy permet d’effectuer des opérations rapidement sans boucle
- le produit scalaire est une opération fondamentale en mathématiques et en IA
- multiplier par un scalaire permet de modifier l’intensité d’un vecteur

---