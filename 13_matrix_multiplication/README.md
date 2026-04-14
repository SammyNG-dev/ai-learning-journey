# Projet 13 — Matrices et multiplication

## 🎯 Objectif

Comprendre ce qu’est une matrice et maîtriser la multiplication matricielle.

---

## 🧩 Description

Ce programme :

- crée deux matrices NumPy
- affiche les matrices
- effectue une multiplication matricielle avec `np.dot()` ou `@`
- affiche le résultat

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Matrice

- une matrice est un tableau de nombres en 2 dimensions
- elle est composée de lignes et de colonnes

Exemple :

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

👉 ici :
- 2 lignes
- 3 colonnes → matrice 2x3

---

### 2. Règle de multiplication matricielle

👉 On peut multiplier deux matrices si :

```text
colonnes de A = lignes de B
```

---

### 3. Taille du résultat

Si :

```text
A = (m x n)
B = (n x p)
```

👉 alors :

```text
résultat = (m x p)
```

---

### 4. Calcul d’un élément

👉 Chaque élément du résultat est obtenu en faisant :

```text
produit scalaire entre une ligne de A et une colonne de B
```

Exemple :

```text
[1, 2, 3] × [7, 9, 11]
= (1×7) + (2×9) + (3×11)
```

---

### 5. Différence avec multiplication classique

```python
A * B
```

👉 multiplication élément par élément (pas matricielle)

```python
np.dot(A, B)
```

👉 multiplication matricielle

---

## 📌 Exemple de sortie

```text
Matrice 1 :
[[1 2 3]
 [4 5 6]]

Matrice 2 :
[[ 7  8]
 [ 9 10]
 [11 12]]

Résultat :
[[ 58  64]
 [139 154]]
```

---

## 📚 Ce que j'ai retenu

- une matrice est une structure fondamentale pour représenter des données
- la multiplication matricielle est une série de produits scalaires
- il est essentiel de respecter les dimensions pour éviter les erreurs
- NumPy permet d’effectuer ces opérations facilement et efficacement
- la multiplication matricielle est au cœur des réseaux de neurones

---