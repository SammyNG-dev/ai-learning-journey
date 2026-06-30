# Projet 26 – Agent dans une grille avec un DQN simplifié

## Objectif

Dans les projets précédents, nous avons remplacé une Q-table par un réseau de neurones.

Le but de ce projet est maintenant de faire apprendre directement un agent qui se déplace dans une grille.

L'agent ne dispose plus d'une Q-table.

Toutes les estimations de Q-values sont produites par le réseau de neurones.

Le projet est découpé en deux parties :

- **train.py** : entraîne le réseau ;
- **play.py** : utilise les poids entraînés pour laisser jouer l'agent.

---

# Environnement

L'environnement est une grille de 10 × 10.

Chaque case possède une signification :

- `0` : case libre ;
- `1` : obstacle ;
- `2` : agent ;
- `3` : objectif.

Au début de chaque épisode :

- l'agent est replacé sur sa position de départ ;
- l'objectif reste à une position fixe ;
- une nouvelle grille est créée.

L'agent peut effectuer quatre actions :

- haut ;
- bas ;
- droite ;
- gauche.

Les déplacements en dehors de la grille sont interdits.

---

# Réseau de neurones

Le réseau reçoit uniquement la position de l'agent.

Les coordonnées sont normalisées entre 0 et 1 afin de faciliter l'apprentissage.

Entrée :

```text
(agent_row / 9, agent_col / 9)
```

Le réseau possède :

- 2 entrées ;
- 4 sorties.

Chaque sortie représente la Q-value d'une action :

- haut ;
- bas ;
- droite ;
- gauche.

Le réseau est entièrement linéaire.

---

# Fonction de récompense

À chaque déplacement :

- +10 si l'objectif est atteint ;
- +1 si l'agent se rapproche de l'objectif ;
- 0 sinon.

La distance est calculée grâce à la distance euclidienne.

---

# Entraînement (train.py)

L'entraînement est réalisé épisode par épisode.

Pour chaque déplacement :

1. le réseau calcule les Q-values ;
2. une action est choisie grâce à la stratégie ε-greedy ;
3. l'agent effectue son déplacement ;
4. une récompense est calculée ;
5. une cible (`target`) est construite ;
6. les poids sont mis à jour par descente de gradient.

Le réseau apprend progressivement quelles actions produisent les meilleures récompenses.

---

# Exploration et exploitation

Au début de l'entraînement :

```text
epsilon = 1
```

L'agent explore presque uniquement des actions aléatoires.

À la fin de chaque épisode :

```text
epsilon = max(0.05, epsilon - 0.0009)
```

L'exploration diminue progressivement.

Au fil des épisodes, le réseau exploite de plus en plus les connaissances acquises.

---

# Utilisation du réseau (play.py)

Une fois l'entraînement terminé :

- les poids et les biais sont copiés dans `play.py` ;
- aucune mise à jour n'est réalisée.

À chaque déplacement :

1. la position de l'agent est normalisée ;
2. le réseau calcule les quatre Q-values ;
3. l'action ayant la plus grande Q-value est choisie ;
4. l'agent se déplace.

Le réseau est alors utilisé uniquement pour prendre des décisions.

---

# Résultat obtenu

Après l'entraînement, l'agent est capable de rejoindre l'objectif placé à sa position d'entraînement.

Dans le meilleur des cas, il atteint l'objectif en réalisant le nombre minimal de déplacements.

Le réseau a donc appris une politique efficace pour cette configuration.

---

# Limites du projet

Ce projet met également en évidence une limite importante.

Le réseau reçoit uniquement les coordonnées de l'agent.

Il ne connaît pas la position de l'objectif.

Pendant tout l'entraînement, l'objectif est resté au même endroit.

Le réseau apprend donc une politique adaptée à cette position unique.

Lorsque l'objectif est déplacé ailleurs :

- il peut encore réussir dans certains cas si la stratégie apprise reste pertinente ;
- mais il peut également continuer à se diriger vers l'ancien objectif ;
- il peut même rester bloqué contre un bord de la grille en répétant la même action.

Le problème ne vient pas du DQN lui-même.

Il provient des informations fournies au réseau.

Un réseau ne peut apprendre qu'à partir des données qu'il reçoit.

Si une information importante est absente, il ne peut pas adapter correctement son comportement.

Pour permettre à l'agent de rejoindre un objectif placé n'importe où dans la grille, il faudra fournir également la position de cet objectif parmi les entrées du réseau.

---

# Ce que ce projet apporte

À la fin de ce projet, nous savons :

- construire un environnement sous forme de grille ;
- entraîner un agent avec un DQN simplifié ;
- remplacer complètement une Q-table par un réseau de neurones ;
- utiliser un réseau entraîné pour jouer sans apprentissage ;
- mettre en place une stratégie ε-greedy avec décroissance progressive de l'exploration ;
- comprendre qu'un réseau ne peut apprendre que les informations qui lui sont fournies.

Ce projet constitue une première version fonctionnelle d'un agent utilisant un réseau de neurones pour prendre ses décisions dans un environnement.