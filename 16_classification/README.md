# Projet 16 — Classification binaire (0 / 1)

## 🎯 Objectif

Créer un modèle capable de prédire une **catégorie (0 ou 1)** à partir d’une entrée `x`.

Contrairement au projet 15 :
- Régression → prédire un nombre
- Classification → prédire une **probabilité**, puis une **classe**

---

## 🧩 Données

```python
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y_true = np.array([0, 0, 0, 1, 1])
```

👉 Interprétation :
- petites valeurs → classe 0  
- grandes valeurs → classe 1  

---

## ⚙️ Fonctionnement du modèle

### 1. Score (comme en régression)

```python
z = a * x + b
```

👉 `z` est un **score brut** (non exploitable directement)

---

### 2. Sigmoid

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

👉 transforme le score en **probabilité entre 0 et 1**

---

### 3. Probabilité

```python
y_pred = sigmoid(z)
```

👉 exemples :
- z = -2 → proba ≈ 0.12  
- z = 0 → proba = 0.5  
- z = 2 → proba ≈ 0.88  

---

### 4. Erreur

```python
error = y_pred - y_true
```

👉 sert à :
- mesurer l’écart  
- calculer le coût  
- corriger le modèle  

---

### 5. Coût (MSE simplifié)

```python
cost = np.mean(error ** 2)
```

👉 mesure l’erreur globale

---

### 6. Corrections

```python
da = np.mean(error * x)
db = np.mean(error)
```

👉 `da` → corrige la pente  
👉 `db` → corrige le biais  

---

### 7. Mise à jour

```python
a = a - lr * da
b = b - lr * db
```

---

## 🔁 Boucle d’apprentissage

```
score → sigmoid → erreur → coût → correction → amélioration
```

---

## 🎯 Décision finale

```python
predictions = (y_pred > 0.5).astype(int)
```

👉 règle :
- proba > 0.5 → 1  
- sinon → 0  

---

## 🧠 Concepts clés

### Sigmoid
- transforme un score en probabilité  
- garantit une sortie entre 0 et 1  

### Seuil 0.5
- permet de passer de probabilité à classe  
- 0.5 = zone d’incertitude  

### Interprétation des probabilités
- proche de 0 → classe 0  
- proche de 1 → classe 1  

### Rôle de `a` et `b`
- `a` → contrôle la variation avec `x`  
- `b` → décale globalement le modèle  

---

## 📊 Résultat attendu

- probabilités proches de 0 pour petits `x`  
- probabilités proches de 1 pour grands `x`  
- prédictions proches de `y_true`  

---

## ⚠️ Points importants

- sans sigmoid → impossible d’obtenir une probabilité  
- le seuil est nécessaire pour décider  
- le learning rate influence la stabilité  

---

## 📚 Ce que j’ai retenu

- classification = probabilité + décision  
- sigmoid = élément central  
- le modèle apprend progressivement  
- on cherche la généralisation, pas la perfection  
