import matplotlib.pyplot as plt
import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Convertir la colonne "Date" en un objet de date/heure si ce n'est pas déjà fait
df['Date'] = pd.to_datetime(df['Date'])

# Trier le DataFrame par date de vente
df_sorted = df.sort_values(by='Date')

# Créer un graphique des revenus au cours du temps
plt.figure(figsize=(10, 6))
plt.plot(df_sorted['Date'], df_sorted['Revenu'], marker='o', linestyle='-')
plt.title('Tendances des revenus au cours du temps')
plt.xlabel('Date')
plt.ylabel('Revenu')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

