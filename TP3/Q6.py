import numpy as np
from scipy.stats import zscore

tableau = np.array([1,2,3,4,5])
tableaubis = zscore(tableau)

print("Tableau original : ", tableau)
print("Tableau normalisé par la méthode zscore : ", tableaubis)