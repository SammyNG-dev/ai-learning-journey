# Projet 28 – Objectif mobile

## Objectif

Jusqu'à présent, l'agent devait rejoindre une cible fixe.

Dans ce projet, la difficulté augmente : la cible peut désormais se déplacer pendant que l'agent tente de l'atteindre.

L'objectif est de vérifier si le réseau de neurones est capable de s'adapter à un environnement dynamique plutôt que d'apprendre uniquement un trajet.

---

## Nouveautés

- La position de la cible est générée aléatoirement au début de chaque épisode.
- La cible effectue un déplacement aléatoire toutes les cinq actions de l'agent.
- Le réseau de neurones doit continuellement prendre en compte la nouvelle position de la cible.
- L'apprentissage et le test sont réalisés sur plusieurs positions différentes.

---

## Récompenses

| Situation | Récompense |
|-----------|-----------:|
| L'agent atteint la cible | +15 |
| L'agent se rapproche de la cible | +1 |
| L'agent reste bloqué contre un mur | -2 |
| L'agent s'éloigne ou conserve la même distance | 0 |

---

## Réseau de neurones

Entrées :

- ligne de l'agent ;
- colonne de l'agent ;
- ligne de la cible ;
- colonne de la cible.

Architecture :

- 4 neurones d'entrée ;
- 2 neurones cachés ;
- 4 neurones de sortie (une Q-value par action).

Les sorties représentent les Q-values des quatre actions possibles :

- haut ;
- bas ;
- droite ;
- gauche.

---

## Déroulement d'un épisode

Pour chaque épisode :

1. L'agent démarre en `(0, 0)`.
2. Une cible est placée à une position aléatoire.
3. Toutes les cinq actions de l'agent, la cible se déplace aléatoirement.
4. L'agent choisit une action grâce à la stratégie ε-greedy.
5. Les Q-values sont mises à jour à partir de la cible de Bellman.
6. Les poids du réseau sont ajustés par rétropropagation.

---

## Résultats

L'entraînement a été réalisé sur **1 000 000 d'épisodes**.

Une fois l'entraînement terminé, l'agent est testé sur treize positions différentes de la cible.

Résultats obtenus sur dix entraînements indépendants :

- 130 tests réalisés ;
- 127 réussites ;
- 3 échecs ;
- **97,69 % de réussite**.

Les trois échecs concernent uniquement les positions :

- `(8, 9)` : 1 échec ;
- `(9, 9)` : 2 échecs.

Toutes les autres positions obtiennent un taux de réussite de **100 %**.

Temps d'entraînement :

- **2 h 43 min 41 s**

---

## Ce que j'ai appris

Ce projet montre qu'un réseau de neurones peut apprendre une stratégie générale de poursuite plutôt qu'un simple trajet.

L'agent apprend à adapter ses décisions en fonction de la position actuelle de la cible, même lorsque celle-ci change pendant l'épisode.

Cette évolution rapproche le projet d'environnements plus réalistes, où les éléments importants ne restent pas immobiles.

---

## Prochaine étape

Introduire un environnement encore plus riche afin de rapprocher progressivement l'agent du fonctionnement nécessaire pour évoluer dans un véritable jeu vidéo.