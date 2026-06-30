# AI Learning Journey

## Le but

Objectif final : créer une IA capable de jouer et terminer Sonic 2 de manière autonome.

# Roadmap

## 🧱 Phase 1 — Bases Python

- [x] Projet 1 — Jeu du nombre mystère  
- [x] Projet 2 — Liste de courses  

---

## 🔢 Phase 2 — NumPy & calculs

- [x] Projet 3 — Statistiques sur un tableau (mean, min, max)  
- [x] Projet 4 — Matrice 3x3 (moyennes et sommes par axes)  

---

## 👁️ Phase 3 — Représentation des données (pré-vision)

- [x] Projet 5 — Simuler un "écran" avec une matrice (grille 2D)  
- [x] Projet 6 — Détection de valeurs dans une matrice  
- [x] Projet 7 — Identifier des positions (coordonnées)  

---

## 🎮 Phase 4 — Logique de jeu (sans IA)

- [x] Projet 8 — Simulation de déplacement dans une grille  
- [x] Projet 9 — Gestion des collisions (obstacles)  
- [x] Projet 10 — Règles simples (si obstacle → action)  
- [x] Projet 11 — Boucle de jeu (état → décision → action)  

---

## 🧠 Phase 5 — Mathématiques utiles

- [x] Projet 12 — Vecteurs et opérations  
- [x] Projet 13 — Matrices et multiplication  
- [x] Projet 14 — Comprendre une fonction de coût simple  

---

## 📊 Phase 6 — Machine Learning

- [x] Projet 15 — Régression simple  
- [x] Projet 16 — Classification simple  
- [x] Projet 17 — Entraînement + test  
- [x] Projet 18 — Ajustement des paramètres  

---

## 🤖 Phase 7 — Réseaux de neurones

- [x] Projet 19 — Premier neurone
- [x] Projet 20 — Réseau de neurones dense
  - [x] Projet 20.1 — Forward d’un neurone caché
  - [x] Projet 20.2 — Construction du `final_dataset`
  - [x] Projet 20.3 — Neurone final
  - [x] Projet 20.4 — Première propagation d’erreur naïve
  - [x] Projet 20.5 — Pourquoi la propagation naïve échoue
  - [x] Projet 20.6 — Intuition de la pente de la sigmoid
  - [x] Projet 20.7 — Dérivée de la sigmoid
  - [x] Projet 20.8 — Delta et erreur locale
  - [x] Projet 20.9 — Gradient d’un poids
  - [x] Projet 20.10 — Rétropropagation propre
  - [x] Projet 20.11 — Stabilisation et validation sur XOR
  - [ ] Projet 20.12 — Refactorisation POO du réseau (plus tard)
- [x] Projet 21 — Classification d’images simples
---

## 🎯 Phase 8 — Reinforcement Learning

- [x] Projet 22 — Environnement simple  
- [x] Projet 23 — Agent avec récompense  
- [x] Projet 24 — Q-learning  
- [x] Projet 25 — Deep Q Network (DQN)
  - [x] 25.01 : Réseau de neurones pour approximer une Q-table
  - [x] 25.02 : Entraînement du réseau par Q-Learning
  - [x] 25.03 : Premier DQN simplifié

---

## 🕹️ Phase 9 — Jeux simples

- [x] Projet 26 — Agent dans une grille
- [ ] Projet 27 — Agent avec position de l’objectif en entrée
- [ ] Projet 28 — Objectif mobile simple
- [ ] Projet 29 — Jeu avec inertie simple
- [ ] Projet 30 — Obstacle et navigation
- [ ] Projet 31 — Terminer un niveau simple

---

## 🧩 Phase 10 — Interaction avec un jeu réel

- [ ] Projet 32 — Capturer l’écran  
- [ ] Projet 33 — Envoyer des inputs clavier  
- [ ] Projet 34 — Lire l’état du jeu  

---

## 🌀 Phase 11 — Sonic (progression)

- [ ] Projet 35 — Agent basique (bouger Sonic)  
- [ ] Projet 36 — Éviter les obstacles  
- [ ] Projet 37 — Survivre  
- [ ] Projet 38 — Finir un niveau  
- [ ] Projet 39 — Enchaîner plusieurs niveaux  

---

## 🏁 Phase 12 — Objectif final

- [ ] Projet 40 — IA autonome sur Sonic 2  

---

## 📌 Règles

- ❌ Interdiction de sauter un projet  
- ❌ Interdiction de valider sans comprendre  
- ✅ Être capable d’expliquer chaque projet  
- ✅ Être capable de modifier le code sans aide  

---

# Structure du repo

```
sammy@sammy-Nitro-AN515-58:~/Bureau/Dev/ai-learning-journey$ tree
.
├── 01_python_guess_number
│   ├── main.py
│   └── README.md
├── 02_shopping_list
│   ├── main.py
│   └── README.md
├── 03_array_numpy
│   ├── main.py
│   └── README.md
├── 04_numpy_matrix
│   ├── main.py
│   └── README.md
├── 05_grid_screen_simulation
│   ├── main.py
│   └── README.md
├── 06_grid_value_detection
│   ├── main.py
│   └── README.md
├── 07_simple_decision_agent
│   ├── main.py
│   └── README.md
├── 08_player_movement
│   ├── main.py
│   └── README.md
├── 09_collision_handling
│   ├── main.py
│   └── README.md
├── 10_multi_direction_movement
│   ├── main.py
│   └── README.md
├── 11_multi_step_agent
│   ├── main.py
│   └── README.md
├── 12_vectors_and_operations
│   ├── main.py
│   └── README.md
├── 13_matrix_multiplication
│   ├── main.py
│   └── README.md
├── 14_cost_function
│   ├── main.py
│   └── README.md
├── 15_linear_regression
│   ├── main.py
│   └── README.md
├── 16_classification
│   ├── main.py
│   └── README.md
├── 17_training_and_testing
│   ├── main.py
│   └── README.md
├── 18_parameters_adjustment
│   ├── main.py
│   └── README.md
├── 19_first_multiparameters_neuron
│   ├── main.py
│   └── README.md
├── 20_neurons_network
│   ├── 20.01_forward_hidden_neuron
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.02_build_hidden_dataset
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.03_final_neuron
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.04_naive_error_propagation
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.05_why_naive_error_propagation_fails
│   │   └── README.md
│   ├── 20.06_sigmoid_slope_intuition
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.07_sigmoid_derivative
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.08_delta_and_local_error
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.09_weight_gradient
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.10_clean_backpropagation
│   │   ├── main.py
│   │   └── README.md
│   ├── 20.11_XOR_stabilisation
│   │   ├── main.py
│   │   └── README.md
│   └── 20.final_survival_ai
│       ├── main.py
│       └── README.md
├── 21_simple_images_classification
│   ├── main.py
│   └── README.md
├── 22_simple_environment
│   ├── main.py
│   └── README.md
├── 23_agent_with_reward
│   ├── main.py
│   └── README.md
├── 24_Q_learning
│   ├── main.py
│   └── README.md
├── 25_dqn_network
│   ├── 25.01_q_table_to_neuron
│   │   ├── main.py
│   │   └── README.md
│   ├── 25.02_one_output_per_action
│   │   ├── main.py
│   │   └── README.md
│   ├── 25.03_mini_deep_q_network
│   │   ├── play.py
│   │   ├── README.md
│   │   └── train.py
│   └── README.md
└── README.md
```

