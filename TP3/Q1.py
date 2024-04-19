import scipy

# Charger le fichier MATLAB (.mat)
data = scipy.io.loadmat('data.mat')

# Accéder aux variables x et y
x = data['x']
y = data['y']

# Afficher les variables x et y
print("Variable x :", x)
print("Variable y :", y)