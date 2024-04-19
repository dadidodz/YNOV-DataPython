import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Calculer le revenu
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire']

# Trie le DataFrame par date de vente en ordre décroissant
df_trie = df.sort_values(by='Date', ascending=False)

# Afficher le DataFrame trié par date de vente
print("\nDataFrame trié par date de vente en ordre décroissant :\n", df_trie)

# Calcule le revenu total par magasin
revenus_par_magasin = df.groupby('Magasin')['Revenu'].sum()

# Tri les magasins selon le revenu total en ordre décroissant
magasins_tries = revenus_par_magasin.sort_values(ascending=False)

# Affiche les magasins classés selon le revenu total
print("\nMagasins classés selon le revenu total en ordre décroissant :\n", magasins_tries)
