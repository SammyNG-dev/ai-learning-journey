# Projet 18 — Ajustement des paramètres

## 🎯 Objectif

Comprendre comment **ajuster le learning rate (`lr`)** pour améliorer l’apprentissage d’un modèle.

👉 Objectif principal :
- trouver un bon équilibre entre **vitesse** et **stabilité**

---

## 🧩 Données

```python
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, 0, 0, 1, 1, 1, 1])
```

---

## ⚙️ Fonctionnement du modèle

### 1. Liste de learning rates

```python
learning_rates = [0.1, 0.01, 0.001]
```

👉 on va tester plusieurs valeurs automatiquement

---

### 2. Boucle sur les learning rates

```python
for lr in learning_rates:
    a = 0.0
    b = 0.0
```

👉 important :
- on réinitialise le modèle à chaque test
- sinon la comparaison est faussée

---

### 3. Boucle d’apprentissage

```python
for i in range(1000):
```

👉 même nombre d’itérations pour chaque `lr`

---

### 4. Score

```python
z = a * x_train + b
```

---

### 5. Probabilité

```python
y_pred = sigmoid(z)
```

---

### 6. Erreur

```python
error = y_pred - y_train
```

---

### 7. Coût

```python
cost = np.mean(error ** 2)
```

---

### 8. Corrections

```python
da = np.mean(error * x_train)
db = np.mean(error)
```

---

### 9. Mise à jour

```python
a = a - lr * da
b = b - lr * db
```

---

### 10. Observation du coût

```python
if i % 100 == 0:
    print(cost)
```

👉 permet de voir :
- la vitesse d’apprentissage
- la stabilité

---

### 11. Résultat final

```python
print("lr =", lr, "cost final =", cost)
```

---

## 🧠 Concepts clés

### Learning rate (`lr`)

- contrôle la taille des pas d’apprentissage

---

### Effets du learning rate

- trop grand → instable, oscillations  
- trop petit → lent  
- bien réglé → stable et efficace  

---

### Comparaison des learning rates

Pour comparer correctement :
- même dataset  
- même nombre d’itérations  
- mêmes valeurs initiales (`a`, `b`)  

---

### Critères de choix

Un bon `lr` doit :

- faire descendre le coût  
- être stable  
- converger rapidement  

---

## 📊 Interprétation des résultats

### Cas 1 — Descente rapide mais instable

```text
coût oscille
```

👉 `lr` trop grand

---

### Cas 2 — Descente lente mais stable

```text
coût diminue progressivement
```

👉 `lr` correct mais lent

---

### Cas 3 — Bonne descente

```text
coût diminue rapidement et reste stable
```

👉 bon `lr`

---

## ⚠️ Points importants

- ne jamais comparer des `lr` avec des conditions différentes  
- toujours réinitialiser le modèle  
- observer la courbe du coût est essentiel  
- un bon `lr` dépend du problème  

---

## 📚 Ce que j’ai retenu

- le learning rate est un paramètre clé  
- il influence directement la qualité de l’apprentissage  
- trop grand = instable  
- trop petit = inefficace  
- il faut tester plusieurs valeurs  
- on choisit le meilleur compromis stabilité / vitesse  

---

## 🔗 Lien avec l’objectif final

👉 Pour une IA plus complexe (comme Sonic) :

- les bons paramètres sont essentiels  
- un mauvais réglage peut empêcher totalement l’apprentissage  

👉 Ajuster les paramètres = étape obligatoire pour créer une IA efficace