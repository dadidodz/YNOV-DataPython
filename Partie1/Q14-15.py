#Création d'une variable contenant une phrase
phrase = "Bonjour, je suis un etudiant en informatique"

#Découpage de la phrase mot par mot et stockant dans une liste
liste_mots = phrase.split()

#Inversion de l'ordre des mots de la phrase
liste_mots.reverse()

#Création vide d'une varible qui stockera notre phrase inversée
phrase_inverse = ""

#Parcours de notre liste de mot inversé et concaténation dans la 
#variable "phrase_inverse"
for mot in liste_mots:
    phrase_inverse += mot + " "

print(phrase_inverse)