import numpy as np

# Créer un tableau NumPy
arr = np.array([10, 20, 30, 40, 50])

# Trouver l'indice de la valeur minimale
min_index = np.argmin(arr)

# Trouver l'indice de la valeur maximale
max_index = np.argmax(arr)

print("Indice de la valeur minimale :", min_index)
print("Indice de la valeur maximale :", max_index)

