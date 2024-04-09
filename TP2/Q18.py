import numpy as np

matrice = np.arange(1, 7).reshape(2, 3)

matrice[matrice > 2] = 0

print(matrice)