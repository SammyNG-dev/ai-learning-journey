# P24 - Q-Learning

## Objectif

Dans ce projet, nous découvrons le Q-Learning.

Jusqu'à présent, notre agent recevait des récompenses mais ne conservait aucune mémoire de ses expériences.

L'objectif est maintenant de permettre à l'agent :

* d'explorer son environnement ;
* de mémoriser les résultats de ses actions ;
* d'améliorer progressivement ses décisions ;
* d'apprendre seul une stratégie efficace.

---

## Contexte

L'environnement est un monde linéaire composé de plusieurs positions.

Exemple :

```text
0 → 1 → 2 → 3 → 4 → 5
```

L'objectif de l'agent est d'atteindre la dernière case.

Actions possibles :

```python
"avancer"
"reculer"
```

Récompenses :

```text
+10 si l'objectif est atteint
+1 si l'agent se rapproche de l'objectif
0 sinon
```

---

## La Q-Table

L'agent possède une mémoire appelée Q-Table.

Elle associe :

```text
(position, action)
```

à une valeur.

Exemple :

```python
{
    (0, "avancer"): 7.04,
    (0, "reculer"): 5.63,
    (1, "avancer"): 7.56
}
```

Cette valeur représente :

```text
À quel point l'agent pense que cette action est intéressante.
```

---

## Exploration

Lors de l'exploration, l'agent choisit une action au hasard.

Exemple :

```python
action = random.choice(actions)
```

L'exploration permet :

* de découvrir de nouvelles situations ;
* de tester des actions inconnues ;
* d'obtenir de nouvelles récompenses.

Sans exploration, l'agent risque de ne jamais découvrir certaines stratégies.

---

## Exploitation

Lors de l'exploitation, l'agent choisit l'action ayant la meilleure Q-value.

Exemple :

```python
q_avancer = q_table.get((current_position, "avancer"), 0)
q_reculer = q_table.get((current_position, "reculer"), 0)
```

L'agent sélectionne ensuite l'action ayant la valeur la plus élevée.

L'exploitation utilise les connaissances déjà apprises.

---

## Epsilon

La variable :

```python
epsilon
```

contrôle le rapport entre exploration et exploitation.

Exemple :

```python
epsilon = 0.3
```

signifie :

```text
30 % exploration
70 % exploitation
```

---

## La valeur future

Pour évaluer une action, l'agent ne regarde pas seulement la récompense immédiate.

Il regarde également ce qui pourrait arriver ensuite.

Cette idée est représentée par :

```python
next_q_value
```

qui correspond à la meilleure valeur connue depuis l'état suivant.

Exemple :

```python
next_q_value = max(q_avancer, q_reculer)
```

---

## Gamma

```python
gamma
```

contrôle l'importance accordée au futur.

Exemple :

```python
gamma = 0.8
```

signifie :

```text
Le futur compte, mais un peu moins que le présent.
```

---

## Learning Rate

```python
learning_rate
```

contrôle la vitesse d'apprentissage.

Exemple :

```python
learning_rate = 0.1
```

L'agent ne modifie pas brutalement ses connaissances.

Il effectue seulement une petite correction à chaque expérience.

---

## Mise à jour d'une Q-value

La formule centrale du Q-Learning est :

```python
q_value = q_value + learning_rate * (
    reward + gamma * next_q_value - q_value
)
```

Elle peut se lire ainsi :

```text
Nouvelle estimation
=
Ancienne estimation
+
Petite correction
```

L'erreur de prédiction est :

```python
reward + gamma * next_q_value - q_value
```

Cette erreur représente :

```text
Ce que l'action vaut réellement
-
Ce que l'agent pensait qu'elle valait
```

---

## Résultat observé

Après plusieurs centaines d'épisodes, l'agent apprend progressivement que :

```text
avancer est plus intéressant que reculer
```

Exemple :

```text
Position 0 : avancer = 7.05
Position 0 : reculer = 5.64

Position 1 : avancer = 7.56
Position 1 : reculer = 5.64

Position 2 : avancer = 8.20
Position 2 : reculer = 6.05

Position 3 : avancer = 9.00
Position 3 : reculer = 6.56

Position 4 : avancer = 10.00
Position 4 : reculer = 7.20
```

La récompense finale remonte progressivement vers les positions précédentes grâce à :

```python
next_q_value
```

---

## Ce que j'ai appris

À la fin de ce projet, je comprends :

* ce qu'est une Q-Table ;
* la différence entre exploration et exploitation ;
* le rôle de epsilon ;
* le rôle de gamma ;
* le rôle du learning rate ;
* ce qu'est une récompense ;
* ce qu'est une valeur future estimée ;
* comment une Q-value est mise à jour ;
* comment un agent peut apprendre progressivement une stratégie efficace.