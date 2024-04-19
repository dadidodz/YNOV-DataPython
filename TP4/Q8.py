import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Effectue une jointure entre df et df_promotions
df_joint = pd.merge(df, df_promotions, on=['Date', 'Magasin'], how='left')



# Afficher le DataFrame résultant
print(df_joint)