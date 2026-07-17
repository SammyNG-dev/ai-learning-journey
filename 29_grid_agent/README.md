# Projet 29 — Agent neuronal dans une grille avec obstacles

## 🎯 Objectif

Créer un agent capable de se déplacer dans une grille fixe de `10 × 10`, d’éviter les obstacles et d’atteindre une cible dont la position change à chaque épisode.

L’objectif est de remplacer progressivement la logique d’un agent codé manuellement par un réseau de neurones entraîné avec des principes de reinforcement learning.

---

## 🧩 Description

Le projet contient principalement deux programmes :

```text
train.py
play.py
```

### `train.py`

Le programme d’entraînement :

* crée une grille avec des obstacles fixes
* place l’agent en `(0, 0)`
* place une cible sur une position libre aléatoire
* donne toute la grille au réseau de neurones
* produit quatre Q-values
* choisit une action
* applique une récompense
* calcule une cible d’apprentissage
* corrige les paramètres du réseau par rétropropagation
* évalue régulièrement le modèle
* sauvegarde les meilleurs paramètres

### `play.py`

Le programme de test :

* charge les paramètres sauvegardés
* place successivement la cible sur toutes les cases accessibles
* laisse le réseau choisir ses actions sans exploration
* affiche les Q-values et les déplacements
* mesure le taux de réussite
* mesure le nombre de mouvements nécessaires

---

## 🛠️ Technologies utilisées

* Python
* NumPy
* fichiers `.npz`
* Git

---

## 🌍 Représentation du monde

Le monde est représenté par une matrice NumPy de taille :

```text
10 × 10
```

Chaque nombre représente un élément de l’environnement :

```text
0 = case libre
1 = obstacle
2 = agent
3 = cible
```

Exemple simplifié :

```python
world = np.array([
    [2, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 3]
])
```

La grille complète est transformée en vecteur avant d’être donnée au réseau.

Pour une grille de `10 × 10`, le réseau reçoit donc :

```text
100 valeurs d’entrée
```

---

## 🧠 Architecture du réseau

Le réseau contient :

```text
une couche d’entrée
deux couches cachées
une couche finale
```

La couche finale contient quatre neurones.

Chaque neurone représente la Q-value d’une action :

```text
index 0 = haut
index 1 = bas
index 2 = droite
index 3 = gauche
```

Exemple de sortie :

```python
q_values = [[10.2, 12.6, 21.2, 6.1]]
```

La plus grande valeur se trouve à l’index `2`.

L’action choisie est donc :

```text
droite
```

---

## 🎮 Choix de l’action

Pendant l’entraînement, l’agent utilise une stratégie epsilon-greedy.

Il peut :

```text
explorer
```

en choisissant une action aléatoire,

ou :

```text
exploiter
```

en choisissant l’action possédant la plus grande Q-value.

La valeur d’epsilon diminue progressivement pendant l’entraînement.

Elle commence proche de :

```text
1.0
```

puis descend jusqu’à une valeur minimale de :

```text
0.15
```

Cela permet :

* beaucoup d’exploration au début
* davantage d’exploitation lorsque le réseau commence à apprendre
* une petite quantité d’exploration conservée en fin d’entraînement

---

## 🏆 Système de récompenses

L’agent reçoit différentes récompenses selon le résultat de son action.

Les récompenses utilisées sont notamment :

```text
+25    cible atteinte
+5.8   déplacement rapprochant l’agent de la cible
-4.2   déplacement éloignant l’agent de la cible
-8.2   déplacement contre un obstacle ou une limite
-10.2  dépassement du nombre maximal de mouvements
```

Le but est d’encourager l’agent à :

* atteindre la cible
* réduire la distance avec elle
* éviter les obstacles
* éviter les déplacements inutiles
* terminer l’épisode rapidement

---

## 📏 Distance utilisée

Pour savoir si l’agent se rapproche de la cible, le programme utilise une distance calculée à partir des coordonnées.

Exemple :

```text
agent : (2, 3)
cible : (5, 7)
```

Le programme compare la distance avant et après le mouvement.

Cela permet de déterminer si l’action :

```text
rapproche l’agent
```

ou :

```text
éloigne l’agent
```

de la cible.

Cette récompense ne donne pas directement le chemin à suivre.

Elle indique seulement si le dernier mouvement semble aller dans une meilleure direction.

---

## 🔁 Boucle d’un épisode

Un épisode suit cette logique :

```text
1. choisir une position de cible
2. créer la grille
3. donner la grille au réseau
4. produire les Q-values
5. choisir une action
6. déplacer l’agent si le mouvement est possible
7. calculer la récompense
8. créer une cible d’apprentissage
9. calculer l’erreur
10. rétropropager cette erreur
11. recommencer jusqu’au succès ou à la limite de mouvements
```

La cible change à chaque nouvel épisode.

Le réseau doit donc apprendre à atteindre plusieurs positions différentes avec les mêmes paramètres.

---

## 🎯 Valeur cible des Q-values

Pour l’action choisie, le programme construit une valeur cible inspirée du Q-learning :

```text
récompense immédiate
+
valeur estimée du meilleur futur
```

L’idée est qu’une action peut être intéressante :

* parce qu’elle donne immédiatement une bonne récompense
* parce qu’elle conduit vers un état offrant de meilleures possibilités ensuite

Les autres Q-values ne sont pas directement remplacées.

Seule la valeur correspondant à l’action choisie reçoit une cible modifiée.

---

## 🧮 Fonction de coût

Le programme compare :

```text
les Q-values produites
```

et :

```text
les Q-values cibles
```

L’erreur est utilisée pour calculer un coût.

Ce coût sert ensuite à corriger :

* les poids de la couche finale
* les biais de la couche finale
* les poids des couches cachées
* les biais des couches cachées

La rétropropagation traverse donc tout le réseau.

---

## 💾 Sauvegarde des modèles

Deux types de modèles sont sauvegardés.

### Meilleur score

Le fichier :

```text
best_score_model.npz
```

est sauvegardé lorsque le modèle atteint un nombre de cibles supérieur au précédent record.

Exemple :

```text
Nouveau meilleur modèle : 52/58
Nouveau meilleur modèle : 53/58
Nouveau meilleur modèle : 56/58
Nouveau meilleur modèle : 58/58
```

### Modèle le plus efficace

Une fois le score maximal atteint, le fichier :

```text
best_optimal_model.npz
```

est sauvegardé uniquement si :

```text
le modèle atteint toutes les cibles
```

et si :

```text
sa moyenne de mouvements est inférieure au précédent record
```

La condition utilisée est :

```python
if score == len(free_positions) and mean_test_moves < min_mean_test_moves:
```

Cela permet de conserver un modèle qui ne se contente pas de réussir.

Il doit également réduire le nombre moyen de déplacements.

---

## 📊 Résultat final

L’agent a atteint :

```text
58 succès sur 58 cibles accessibles
```

soit :

```text
100 % de réussite
```

Le premier modèle parfait obtenait une moyenne d’environ :

```text
12.47 mouvements
```

L’entraînement a ensuite continué à améliorer cette moyenne :

```text
12.47
12.02
11.88
11.78
11.53
11.50
11.47
11.22
11.09
```

Le meilleur modèle final obtient donc :

```text
58/58
```

avec une moyenne de :

```text
11.09 mouvements
```

Le programme `play.py` a confirmé ce résultat :

```text
Succès : 58
Echecs : 0
```

---

## 📉 Optimisation observée

Le modèle a progressivement réduit certains grands détours.

Exemples observés sur des cibles difficiles :

```text
cible (4, 5) : 21 mouvements
cible (5, 5) : 20 mouvements
cible (7, 3) : 18 mouvements
cible (8, 4) : 22 mouvements
```

Le réseau ne trouve pas toujours le plus court chemin possible.

Cependant, il a appris une politique :

* fiable
* stable
* plus efficace que les premiers modèles parfaits

---

## 🧪 Test sur de nouvelles grilles

Après l’entraînement, le modèle a été testé sur deux grilles qu’il n’avait jamais rencontrées.

### Grille légèrement différente

Résultat :

```text
20 succès sur 64 cibles
31.25 % de réussite
```

Le réseau conserve certaines décisions utiles, notamment dans des zones ressemblant à la grille d’entraînement.

Cependant, de nombreux nouveaux obstacles rendent ses anciennes décisions incorrectes.

### Grille très différente

Résultat :

```text
1 succès sur 61 cibles
1.64 % de réussite
```

Le réseau échoue presque complètement.

Il ne réussit essentiellement que lorsqu’une cible est immédiatement accessible.

---

## 🔄 Boucles observées

Sur les nouvelles grilles, le réseau peut répéter indéfiniment une action impossible.

Exemple :

```text
Position : (1, 4)
Action : droite
Position : (1, 4)
Action : droite
Position : (1, 4)
Action : droite
```

La position ne change pas, car un obstacle bloque le mouvement.

Le réseau reçoit alors presque exactement le même état.

Il produit donc :

```text
les mêmes Q-values
```

puis choisit :

```text
la même action
```

Cela crée une boucle déterministe jusqu’à la limite de mouvements.

---

## 🧠 Spécialisation et généralisation

Le résultat de `58/58` signifie :

```text
l’agent maîtrise la grille sur laquelle il a été entraîné
```

Mais cela ne signifie pas :

```text
l’agent sait résoudre n’importe quelle grille
```

Le réseau a appris une politique fortement adaptée :

* à la disposition fixe des obstacles
* aux passages disponibles
* aux chemins rencontrés pendant l’entraînement

Il possède une petite capacité de généralisation sur une grille proche.

Mais cette généralisation reste très limitée lorsque la structure du monde change fortement.

---

## 📚 Concepts appris

### 1. Représentation complète de l’état

Toute la grille peut être utilisée comme entrée d’un réseau.

Le réseau reçoit ainsi :

* la position de l’agent
* la position de la cible
* la position des obstacles
* les cases libres

---

### 2. Une sortie par action

Un réseau peut produire plusieurs valeurs.

Chaque valeur représente l’intérêt estimé d’une action différente.

---

### 3. Q-values

Une Q-value ne représente pas directement une direction obligatoire.

Elle représente l’estimation de l’intérêt d’effectuer une action dans un état donné.

---

### 4. Exploration et exploitation

L’exploration permet de découvrir de nouveaux comportements.

L’exploitation permet d’utiliser les comportements déjà appris.

---

### 5. Apprentissage à partir des récompenses

Le réseau n’a pas reçu les chemins corrects sous la forme d’un dataset préparé à l’avance.

Il a appris à partir des conséquences de ses actions.

---

### 6. Récompense immédiate et futur estimé

Une action peut être intéressante même si elle n’atteint pas immédiatement la cible.

Elle peut conduire vers un meilleur état futur.

---

### 7. Rétropropagation dans un agent

La rétropropagation peut servir à entraîner un réseau produisant des Q-values.

Elle ne se limite pas à la classification supervisée.

---

### 8. Importance de l’évaluation

Le coût d’entraînement ne suffit pas pour savoir si l’agent fonctionne.

Il faut mesurer concrètement :

* le nombre de cibles atteintes
* le nombre d’échecs
* le nombre de mouvements
* la stabilité des résultats

---

### 9. Différence entre réussite et efficacité

Un modèle peut atteindre toutes les cibles tout en prenant de très longs détours.

Il faut donc distinguer :

```text
le taux de réussite
```

et :

```text
l’efficacité des chemins
```

---

### 10. Modèle utile et modèle optimal

Un modèle n’a pas toujours besoin d’être parfaitement optimal.

Un modèle peut être considéré comme satisfaisant s’il :

* fonctionne de manière fiable
* respecte les contraintes principales
* est suffisamment efficace
* ne nécessite pas un coût d’entraînement disproportionné

---

### 11. Généralisation

Un modèle performant sur son environnement d’entraînement peut échouer sur un environnement différent.

Tester uniquement la grille connue aurait caché cette faiblesse.

---

### 12. Données d’entraînement limitées

Même si la cible change à chaque épisode, la disposition des obstacles reste fixe.

Le réseau observe donc de nombreuses cibles différentes, mais toujours dans le même monde.

Il apprend à généraliser entre les positions de cible.

Il n’apprend pas encore à généraliser entre différentes cartes.

---

## ⚠️ Limites du projet

Le modèle actuel :

* est entraîné sur une seule disposition d’obstacles
* ne garantit pas les chemins les plus courts
* peut rester bloqué contre un obstacle
* peut répéter une action impossible
* généralise peu à de nouvelles cartes
* utilise toujours une grille de taille fixe
* nécessite une entrée de 100 valeurs
* ne possède pas de mémoire explicite de ses mouvements précédents

---

## 📌 Ce que j’ai retenu

* un réseau de neurones peut remplacer une Q-table
* une sortie peut représenter chaque action possible
* un agent peut apprendre à partir de récompenses
* une cible aléatoire oblige le même réseau à résoudre plusieurs objectifs
* atteindre toutes les cibles ne signifie pas emprunter les chemins les plus courts
* le meilleur score et la meilleure efficacité sont deux critères différents
* continuer l’entraînement peut améliorer une politique déjà fonctionnelle
* une excellente performance sur une grille connue ne prouve pas la généralisation
* changer la disposition des obstacles peut faire chuter brutalement les performances
* un agent déterministe peut rester bloqué en répétant la même action
* l’environnement d’entraînement détermine fortement ce que le réseau apprend
* pour généraliser à plusieurs grilles, il faudra entraîner le réseau sur plusieurs environnements

---

## ✅ Conclusion

Le projet 29 a permis de créer un agent neuronal capable de terminer entièrement un niveau simple représenté par une grille.

Le modèle final atteint toutes les positions accessibles avec :

```text
100 % de réussite
```

et une moyenne de :

```text
10.36 mouvements
```

Le projet a également montré une limite fondamentale :

```text
l’agent maîtrise une grille précise
mais ne sait pas encore résoudre des grilles inconnues
```

Cette observation conduit naturellement au projet suivant :

```text
Projet 30 — Généralisation à plusieurs grilles
```
