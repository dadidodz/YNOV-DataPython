from scipy.ndimage import median_filter
import numpy as np

tableau = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

tableau_filtre = median_filter(tableau, size=.)

print(tableau)
print(tableau_filtre)