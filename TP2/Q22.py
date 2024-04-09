import numpy as np

# print(np.eye(5))

matrice = np.array([[2, -3, 1], [4, 0, 2], [-1, 5, 3]])
determinant = np.linalg.det(matrice)

print(matrice)
print("")
print(determinant)