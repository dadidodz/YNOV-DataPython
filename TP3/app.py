from scipy import io

# Créer des données pour les variables x et y
x = 10
y = 20

# Créer un dictionnaire contenant les variables
data = {'x': x, 'y': y}

# Enregistrer les données dans un fichier .mat
io.savemat('data.mat', data)

print("Le fichier data.mat a été créé avec succès.")