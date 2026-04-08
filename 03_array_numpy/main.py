import numpy as np

random_numbers_np_array = np.random.randint(1, 1000, size=10)

print("Tableau :", random_numbers_np_array)
print()
print("Moyenne :", np.mean(random_numbers_np_array))
print()
print("Max :", np.max(random_numbers_np_array))
print()
print("Min :", np.min(random_numbers_np_array))
print()

arr = np.array([1, 2, 3])
print(arr * 2)

arr2 = [1, 2, 3] * 2

print(arr2)