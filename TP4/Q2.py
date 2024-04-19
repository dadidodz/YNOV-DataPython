import pandas as pd

# Charge le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Affiche les 5 premières lignes du fichier
print("\nLes cinq premières lignes du fichier :\n", df.head())

# Affiche le nombre de lignes et de colonnes du fichier
print(f"\nNombre de ligne et de colonnes : {df.shape}")

# Affiche le type de chaque colonne du fichier
print("\nType de chaque colonne :\n", df.dtypes)