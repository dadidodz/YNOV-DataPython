#Création d'un tuple contenant les jours de la semaine
semaine = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi","Samedi", "Dimanche")

#Boucle for qui parcours le tuple "semaine"
for jour in semaine:
    print(jour)

    #Condition if vérifiant si le jour actuelle est "Samedi" ou "Dimanche"
    if jour == "Samedi" or jour == "Dimanche":
        print("C'est le week-end")
    else:
        print("C'est la semaine")