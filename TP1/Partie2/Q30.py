#Dictionnaire de livres ayant comme comme clé un nom de livre
#et comme valeur leur auteur
livres = {
    "Le Petit Chaperon rouge" : "Charles Perrault",
    "1984": "George Orwell",
    "Le Petit Prince": "Antoine de Saint-Exupery",
    "Orgueil et Prejuges": "Jane Austen"
}

# Affichage du titre et de l'auteur de chaque livre
for titre, auteur in livres.items():
    print(f"Titre: {titre} - Auteur: {auteur}")