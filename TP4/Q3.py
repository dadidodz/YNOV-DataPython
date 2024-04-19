import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# print(df.isnull())
# print("")

# print("\n", df.isnull().sum().sum())
# print("")

# print(df.isnull().values.any())
# print("")

# Affiche le nombre de valeurs manquantes par colonne
print("\nNombre de valeurs manquantes :\n",df.isnull().sum())

# Affiche le nombre total de valeurs manquantes dans le fichier
print("\nNombre total de valeurs manquantes :\n", df.isnull().sum().sum())

# Supprime les lignes où il y a une valeur manquante
df.dropna(inplace=True)

# Remplace les valeurs nulles par la valeur en paramètre
df.fillna(0)

# Supprime les doublons du fichier
df.drop_duplicates(inplace=True)