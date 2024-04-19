from scipy.stats import norm

# Générer une matrice 3x3 de nombres aléatoires tirés de cette distribution
random_numbers = norm(loc=0, scale=1).rvs(size=(3, 3))

print("Matrice 3x3 de nombres aléatoires tirés d'une distribution normale :\n", random_numbers)
