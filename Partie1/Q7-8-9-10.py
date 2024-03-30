#Création d'une liste contenant les jours de la semaine
semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi","Samedi", "Dimanche"]

#Affiche le 3ème élément de la liste semaine dans la console
#print(semaine[2])

#Ajout de "Dimanche" comme premier élément de la liste avec la 
#fonction "insert", spécifiant l'emplacement voulu et la variable
semaine.insert(0, "Dimanche")

#Suppression de "Lundi" dans la liste avec la fonction "remove"
semaine.remove("Lundi")
print(semaine)