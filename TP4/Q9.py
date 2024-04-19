import pandas as pd
import matplotlib.pyplot as plt



# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Calculer le revenu
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire']

# df.insert(loc=len(df.columns), column='Revenu', value=df['Quantité vendue'] * df['Prix unitaire'])

# Convertir la colonne "Date" en un objet de date/heure
df['Date'] = pd.to_datetime(df['Date'])

# Extraire l'année et créer une nouvelle colonne "Année"
df['Année'] = df['Date'].dt.year

# Convertir la colonne "Date" en un objet de date/heure
df['Date'] = pd.to_datetime(df['Date'])

# Sélectionner les données des ventes qui ont eu lieu en 2022
ventes_2022 = df[df['Date'].dt.year == 2022]

# Filtrer les données pour afficher uniquement les ventes où plus de 100 articles ont été vendus
ventes_plus_100_articles = ventes_2022[ventes_2022['Quantité vendue'] > 100]

# Calculer le total des revenus par magasin
revenus_par_magasin = df.groupby('Magasin')['Revenu'].sum()

# Trouver le produit le plus vendu
produit_plus_vendu = df.groupby('Produit')['Quantité vendue'].sum().idxmax()

# Trier le DataFrame par date de vente en ordre décroissant
df_trie = df.sort_values(by='Date', ascending=False)

# Calculer le revenu total par magasin
revenus_par_magasin = df.groupby('Magasin')['Revenu'].sum()

# Trier les magasins selon le revenu total en ordre décroissant
magasins_tries = revenus_par_magasin.sort_values(ascending=False)

# Exporte le DataFrame final en fichier CSV
# df.to_csv("resultats_ventes.csv", index=False)

# Convertie la colonne "Date" en un objet de date/heure
df['Date'] = pd.to_datetime(df['Date'])

# Tri le DataFrame par date de vente
df_sorted = df.sort_values(by='Date')

# Créer un graphique des revenus au cours du temps
plt.figure(figsize=(10, 6))
plt.plot(df_sorted['Date'], df_sorted['Revenu'], linestyle='-')
plt.title('Tendances des revenus au cours du temps')
plt.xlabel('Date')
plt.ylabel('Revenu')
plt.show()