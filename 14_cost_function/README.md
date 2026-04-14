# Projet 14 — Fonction de coût simple

## 🎯 Objectif

Comprendre comment mesurer l’erreur d’un modèle et pourquoi une IA a besoin d’une fonction de coût.

---

## 🧩 Description

Ce programme :

- crée deux vecteurs :
  - `y_true` → valeurs réelles
  - `y_pred` → prédictions du modèle
- calcule l’erreur entre les deux
- calcule un coût avec la MSE (Mean Squared Error)
- affiche les résultats

---

## 🛠️ Technologies utilisées

- Python
- NumPy

---

## 🧠 Concepts appris

### 1. Erreur

```python
error = y_pred - y_true
```

- représente la différence entre la prédiction et la réalité
- peut être positive ou négative

---

### 2. Fonction de coût (MSE)

```python
cost = np.mean(error ** 2)
```

- mesure l’erreur globale du modèle
- retourne un seul nombre

---

### 3. Pourquoi on met au carré

- éviter que les erreurs positives et négatives se compensent
- pénaliser davantage les grandes erreurs

Exemple :

```text
erreurs = [-2, +2] → moyenne = 0 ❌
erreurs² = [4, 4] → moyenne = 4 ✔️
```

---

### 4. Pourquoi on fait une moyenne

- obtenir une erreur moyenne par donnée
- comparer des modèles sur des datasets de tailles différentes

---

### 5. Rôle dans le Machine Learning

- le coût indique à quel point le modèle se trompe
- il permet d’ajuster les paramètres du modèle :
  - les poids
  - le biais
- objectif : minimiser le coût

---

## 📌 Exemple de sortie

```text
y_true : [ 3 -1  2]

y_pred : [2.5 0.  2. ]

error : [-0.5  1.   0. ]

cost : 0.4166666666666667
```

---

## 📚 Ce que j'ai retenu

- une IA ne peut pas se baser sur "bon" ou "mauvais"
- elle a besoin d’un nombre pour mesurer son erreur
- la fonction de coût transforme les erreurs en une valeur exploitable
- les poids et le biais sont ajustés pour réduire cette erreur
- la MSE est une méthode simple et efficace pour mesurer l’erreur

---