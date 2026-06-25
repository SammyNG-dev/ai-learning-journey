# P25.03 — Mini Deep Q-Network (DQN)

## Objectif

Remplacer la Q-table du projet précédent par un réseau de neurones.

Le réseau ne mémorise plus directement une Q-value pour chaque couple (état, action). Il apprend à approximer ces Q-values à partir de l'état courant.

---

## Ce que ce projet introduit

- utilisation d'un réseau de neurones pour approximer une fonction Q ;
- entraînement par descente de gradient ;
- construction d'un vecteur cible (`target_vector`) ;
- exploration / exploitation avec une stratégie ε-greedy ;
- séparation entre entraînement (`train.py`) et utilisation (`play.py`).

---

## Réseau de neurones

Entrée :

- position actuelle de l'agent.

Sorties :

- Q(avancer)
- Q(reculer)

Architecture :

```
1 → 2
```

---

## Fonctionnement

À chaque déplacement :

1. le réseau prédit les deux Q-values de la position actuelle ;
2. l'agent choisit une action :
   - exploration avec une probabilité ε ;
   - exploitation sinon ;
3. l'agent reçoit une récompense ;
4. une cible est calculée :

```
target = reward + gamma × max(next_q_values)
```

5. seule la sortie correspondant à l'action jouée est remplacée dans le `target_vector` ;
6. l'erreur est calculée ;
7. une descente de gradient met à jour les poids.

---

## Récompenses

Objectif atteint :

```
+10
```

L'agent se rapproche du but :

```
+1
```

Sinon :

```
0
```

---

## Fichiers

### train.py

Entraîne le réseau de neurones.

Le réseau est initialisé avec des poids aléatoires.

À la fin de l'entraînement, les poids peuvent être récupérés puis copiés dans `play.py`.

---

### play.py

Utilise uniquement les poids déjà appris.

Aucun apprentissage n'est effectué.

Le script montre simplement comment le réseau joue avec les poids obtenus pendant l'entraînement.

---

## Observations

Pendant l'entraînement :

- plusieurs épisodes sont nécessaires avant que le réseau apprenne une bonne politique ;
- la fonction de coût diminue progressivement ;
- l'agent améliore peu à peu son comportement.

Pendant l'évaluation :

- le réseau joue directement avec les poids appris ;
- l'agent atteint systématiquement l'objectif en 5 mouvements, qui est le minimum possible dans cet environnement.

---

## Expériences réalisées

Deux entraînements ont été comparés :

- ε = 0.3 (exploration partielle)
- ε = 1 (exploration totale)

Dans les deux cas, le réseau apprend une politique optimale.

Cela montre que le comportement de l'agent pendant l'entraînement peut être très différent de la politique finalement représentée par les poids du réseau.

---

## Limites

Ce projet est volontairement très simplifié.

Contrairement à un véritable DQN, il ne contient pas encore :

- Experience Replay ;
- Target Network ;
- mini-batchs ;
- sauvegarde automatique des poids.

Ces éléments seront introduits progressivement dans les projets suivants.

---

## Compétences acquises

À la fin de ce projet, je sais :

- utiliser un réseau de neurones comme approximation d'une fonction Q ;
- construire un `target_vector` ;
- entraîner un réseau par descente de gradient en reinforcement learning ;
- utiliser une stratégie ε-greedy ;
- séparer une phase d'entraînement d'une phase d'utilisation du réseau ;
- comprendre qu'un agent apprend progressivement au fil des épisodes.

## Arborescence

```
.
├── play.py
├── README.md
└── train.py
```
