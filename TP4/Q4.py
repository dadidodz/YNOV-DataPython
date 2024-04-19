import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Ajoute la colonne "Revenu" remplie à chaque ligne par
# produit de la "Quantité vendue" par "Prix unitaire" de la même ligne
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire']

# Ajoute la colonne "Année" contenant l'année extraite de la colonne "Date"
df['Année'] = pd.to_datetime(df['Date']).dt.year

# Affiche les 5 premières lignes du fichier modifié
print("\nLes cinq premières lignes du fichier :\n", df.head())