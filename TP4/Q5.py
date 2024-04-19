import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Convertir la colonne "Date" en un objet de date/heure
df['Date'] = pd.to_datetime(df['Date'])

# Sélectionne les données des ventes qui ont eu lieu en 2022
# et les stocke dans une variable
ventes_2022 = df[df['Date'].dt.year == 2022]

# Filtre les données pour afficher uniquement les ventes
# où plus de 100 articles ont été vendus
ventes_plus_100_articles = ventes_2022[ventes_2022['Quantité vendue'] > 100]

# Affiche les ventes qui répondent aux critères
print("\n", ventes_plus_100_articles)