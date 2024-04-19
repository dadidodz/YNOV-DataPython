from scipy.ndimage import zoom
import numpy as np

# Créer une matrice 10x10 remplie de 1
matrice = np.ones((10, 10))

matrice_zoom = zoom(matrice, 2.0)

print(matrice)
print("")
print(matrice_zoom)