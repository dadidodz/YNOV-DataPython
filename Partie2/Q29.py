#Dictionnaire de livres ayant comme comme clé un nom de livre
#et comme valeur leur auteur
livres = {
    "Le Petit Chaperon rouge" : "Charles Perrault",
    "1984": "George Orwell",
    "Le Petit Prince": "Antoine de Saint-Exupéry",
    "Orgueil et Préjugés": "Jane Austen"
}

#Accès à l'auteur du livre "1984"
print(livres.get("1984"))