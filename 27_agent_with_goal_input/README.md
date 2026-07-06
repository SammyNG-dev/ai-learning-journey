# Projet 27 — Agent avec position de l'objectif en entrée

## Objectif

Dans le projet précédent, l'agent apprenait uniquement à rejoindre une position fixe.

L'objectif de ce projet est de permettre au réseau de neurones de connaître également la position de la cible afin qu'il puisse apprendre une stratégie générale.

Le réseau reçoit désormais :

- la ligne de l'agent ;
- la colonne de l'agent ;
- la ligne de l'objectif ;
- la colonne de l'objectif.

L'objectif n'est plus seulement d'apprendre un chemin particulier, mais de comprendre où se trouve la cible.

---

## Compétences acquises

- passage de 2 à 4 entrées ;
- ajout d'une couche cachée ;
- rétropropagation sur plusieurs couches ;
- calcul des gradients d'une couche cachée ;
- approximation des Q-values avec un réseau de neurones ;
- apprentissage avec une cible variable.

---

## Architecture du réseau

Entrées :

- ligne de l'agent ;
- colonne de l'agent ;
- ligne de l'objectif ;
- colonne de l'objectif.

Architecture :

```text
4 entrées
     │
     ▼
Couche cachée (2 neurones)
     │
     ▼
4 sorties
```

Les quatre sorties correspondent aux actions possibles :

- haut ;
- bas ;
- droite ;
- gauche.

---

## Fonction de récompense

Le réseau reçoit :

- +15 lorsque l'objectif est atteint ;
- +1 lorsqu'il se rapproche de l'objectif ;
- 0 lorsqu'il s'en éloigne ;
- -2 lorsqu'il tente un déplacement impossible.

---

## Fonctionnement

Pour chaque épisode :

- une position d'objectif est générée aléatoirement ;
- l'agent est replacé à la position de départ ;
- le réseau choisit une action ;
- une récompense est calculée ;
- les Q-values sont mises à jour ;
- la rétropropagation met à jour les deux couches du réseau.

L'exploration est réalisée grâce à une stratégie ε-greedy.

---

## Expériences réalisées

Plusieurs expériences ont été menées afin d'étudier l'influence de différents paramètres :

- modification de la récompense finale ;
- modification des pénalités ;
- comparaison de plusieurs nombres d'épisodes ;
- évaluation sur 100 entraînements indépendants ;
- comparaison entre un objectif fixe et un objectif aléatoire.

---

## Résultats

Deux méthodes d'entraînement ont été comparées.

### Objectif fixe

Pendant tout l'entraînement, l'objectif restait toujours à la même position.

Le réseau obtenait de bons résultats uniquement autour de cette position.

Le taux de réussite global sur plusieurs positions de test était de **28,38 %**.

### Objectif aléatoire

À chaque épisode, une nouvelle position d'objectif était générée aléatoirement.

Le réseau devait alors réellement utiliser les quatre entrées pour choisir ses actions.

Le taux de réussite global est passé à **86,38 %**.

Cette expérience montre qu'un réseau de neurones apprend beaucoup mieux lorsqu'il rencontre des situations variées pendant son entraînement.

---

## Ce que ce projet m'a appris

Ce projet m'a permis de comprendre qu'ajouter une information en entrée d'un réseau ne suffit pas.

Pour qu'un réseau apprenne réellement à utiliser une information, cette information doit varier pendant l'entraînement.

Ce principe est fondamental en machine learning : un modèle ne peut apprendre une règle générale que si les données d'entraînement sont suffisamment variées.

---

## Limites du projet

Ce projet reste volontairement simple.

- aucun obstacle ;
- objectif immobile pendant un épisode ;
- position de départ toujours identique ;
- environnement entièrement observable ;
- rétropropagation simplifiée ;
- aucune fonction d'activation ;
- une seule couche cachée composée de deux neurones.

Ces limites seront progressivement levées dans les projets suivants.