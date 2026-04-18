# Projet 15 — Régression linéaire simple

## 🎯 Objectif

Créer un modèle capable d’apprendre une relation entre une entrée `x` et une sortie `y` :

```text
y ≈ a * x + b
```

Le modèle doit ajuster automatiquement :
- `a` → la pente (inclinaison)
- `b` → le biais (hauteur)

---

## 🧩 Données

```python
x = np.array([1, 2, 3, 4])
y_true = np.array([3, 5, 7, 9])
```

Relation attendue :

```text
y = 2x + 1
```

---

## ⚙️ Fonctionnement du modèle

À chaque itération :

### 1. Prédiction

```python
y_pred = a * x + b
```

### 2. Erreur

```python
error = y_pred - y_true
```

### 3. Coût (MSE)

```python
cost = np.mean(error ** 2)
```

### 4. Calcul des corrections

```python
da = 2 * np.mean(error * x)
db = 2 * np.mean(error)
```

### 5. Mise à jour

```python
a = a - lr * da
b = b - lr * db
```

---

## 🧠 Concepts clés

### 1. Erreur

- mesure l’écart entre la prédiction et la réalité
- signe important :
  - positif → trop haut
  - négatif → trop bas

---

### 2. Coût (MSE)

- mesure l’erreur globale du modèle
- permet de suivre l’amélioration
- ne sert pas directement à corriger

---

### 3. Pente (`a`) vs biais (`b`)

- `a` → contrôle l’inclinaison de la droite
- `b` → décale toute la droite vers le haut ou le bas

---

### 4. Interprétation des erreurs

- erreurs identiques → problème de biais (`b`)
- erreurs qui varient avec `x` → problème de pente (`a`)

---

### 5. Gradients (`da`, `db`)

- `da` → comment corriger la pente
- `db` → comment corriger le biais

---

### 6. Learning rate (`lr`)

- contrôle la vitesse d’apprentissage
- trop grand → instable
- trop petit → lent

---

## 🔁 Boucle d’apprentissage

Le modèle répète :

```text
prédiction → erreur → coût → correction → amélioration
```

---

## 📊 Résultat attendu

Après plusieurs itérations :

```text
a ≈ 2
b ≈ 1
cost ≈ 0
```

---

## 📚 Ce que j’ai retenu

- un modèle peut apprendre une relation automatiquement
- l’erreur indique la direction de correction
- le coût mesure la qualité globale
- `a` et `b` sont ajustés progressivement
- l’apprentissage est une approximation, pas une solution parfaite
