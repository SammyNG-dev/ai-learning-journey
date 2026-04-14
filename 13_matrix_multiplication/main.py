import numpy as np

matrix_1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix_2 = np.array([[7, 8],
                     [9, 10],
                     [11, 12]])

print("Matrice 1 :")
print(matrix_1)
print()
print("Matrice 2 :")
print(matrix_2)
print()
print("Multiplication matricielle :")
result = np.dot(matrix_1, matrix_2)
print(result)