import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Calculer le revenu
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire']

# Calcule le total des revenus par magasin
revenus_par_magasin = df.groupby('Magasin')['Revenu'].sum()

# Affiche les revenus par magasin
print("\nTotal des revenus par magasin :\n", revenus_par_magasin)

# Trouve le produit le plus vendu
produit_plus_vendu = df.groupby('Produit')['Quantité vendue'].sum().idxmax()

# Affiche le produit le plus vendu
print("\nLe produit le plus vendu est :", produit_plus_vendu)
