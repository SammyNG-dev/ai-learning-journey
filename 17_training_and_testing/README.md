# Projet 17 — Entraînement + Test

## 🎯 Objectif

Apprendre à **évaluer correctement un modèle**.

Contrairement au projet 16 :
- Avant → entraînement et test sur les mêmes données  
- Maintenant → séparation en **train / test**

👉 objectif :
- vérifier si le modèle **généralise**
- éviter qu’il **apprenne par cœur**

---

## 🧩 Données

```python
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, 0, 0, 1, 1, 1, 1])
```

👉 Interprétation :
- petites valeurs → classe 0  
- grandes valeurs → classe 1  

---

## ⚙️ Fonctionnement du modèle

### 1. Séparation train / test

```python
x_train = x[0:5]
y_train = y[0:5]

x_test = x[5:]
y_test = y[5:]
```

👉 règles :
- garder les correspondances `(x, y)`
- ne jamais mélanger les paires

---

### 2. Score (sur train)

```python
z = a * x_train + b
```

👉 calcul effectué uniquement sur les données d’entraînement

---

### 3. Sigmoid

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

👉 transforme le score en probabilité

---

### 4. Probabilité (train)

```python
y_pred = sigmoid(z)
```

---

### 5. Erreur

```python
error = y_pred - y_train
```

---

### 6. Coût

```python
cost = np.mean(error ** 2)
```

---

### 7. Corrections

```python
da = np.mean(error * x_train)
db = np.mean(error)
```

---

### 8. Mise à jour

```python
a = a - lr * da
b = b - lr * db
```

---

## 🔁 Boucle d’apprentissage

```
train → score → sigmoid → erreur → coût → correction → amélioration
```

---

## 🎯 Test du modèle

### 9. Score (test)

```python
z_test = a * x_test + b
```

---

### 10. Probabilité

```python
proba_test = sigmoid(z_test)
```

---

### 11. Décision finale

```python
predictions = (proba_test > 0.5).astype(int)
```

👉 règle :
- proba > 0.5 → 1  
- sinon → 0  

---

### 12. Comparaison

```python
print(predictions)
print(y_test)
```

👉 permet de vérifier si le modèle fonctionne sur des données jamais vues

---

## 🧠 Concepts clés

### Train vs Test
- train → apprentissage  
- test → évaluation  

---

### Généralisation
- capacité à réussir sur des données inconnues  
- objectif principal d’un modèle  

---

### Overfitting
- bon sur train  
- mauvais sur test  
- le modèle mémorise les données  

---

### Underfitting
- mauvais sur train et test  
- le modèle ne comprend pas le problème  

---

## 📊 Résultat attendu

- bonnes prédictions sur `x_test`
- cohérence entre `predictions` et `y_test`

⚠️ Attention :
> un bon résultat sur peu de données ne garantit pas un bon modèle

---

## ⚠️ Points importants

- ne jamais utiliser `x_test` pendant l’apprentissage  
- toujours garder les paires `(x, y)` intactes  
- un test trop petit n’est pas fiable  
- un modèle doit être testé sur des données variées  

---

## 📚 Ce que j’ai retenu

- il faut séparer les données pour évaluer un modèle  
- le test permet de détecter le surapprentissage  
- un bon modèle généralise  
- 100% sur peu de données ne suffit pas  
- l’évaluation est aussi importante que l’apprentissage  

---

## 🔗 Lien avec l’objectif final

👉 Une IA pour Sonic doit :
- apprendre sur certaines situations  
- réussir sur des situations nouvelles  

Sinon :
> elle ne sait pas jouer, elle répète simplement