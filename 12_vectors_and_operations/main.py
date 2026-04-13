import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Vecteur 1 :", v1)
print("Vecteur 2 :", v2)
print()
print("Addition des 2 vecteurs :", v1 + v2)
print("Soustraction des deux vecteurs :", v1 - v2)
print("Multiplication par un scalaire :", v1 * 2)
print("Produit scalaire :", np.dot(v1, v2))