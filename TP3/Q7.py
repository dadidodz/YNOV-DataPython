import numpy as np
from scipy.stats import scoreatpercentile

tableau = np.array([1,2,3,4,5,6,7,8,9])
score = scoreatpercentile(tableau, 50)

print("Tableau original : ", tableau)
print("50ème percentile (médiane) du tableau : ", score)