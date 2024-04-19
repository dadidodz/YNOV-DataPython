# from scipy.spatial import distance

# print(distance.euclidean([1, 2, 0], [4, 6, 0]))

from scipy.spatial.distance import euclidean

# Coordonnées des points
point1 = (1, 2)
point2 = (4, 6)

# Calcul de la distance euclidienne entre les points
distance = euclidean(point1, point2)

print("Distance euclidienne entre les points :", distance)