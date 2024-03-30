#Création d'une variable contenant une phrase
phrase = "Bonjour, je suis un etudiant en informatique"

#Découpage de la phrase mot par mot et stockant dans une liste
listeMots = phrase.split()

#Inversion de l'ordre des mots de la phrase
listeMots.reverse()

#Création vide d'une varible qui stockera notre phrase inversée
phraseInverse = ""

#Parcours de notre liste de mot inversé et concaténation dans la 
#variable "phraseInverse"
for mot in listeMots:
    phraseInverse += mot + " "

print(phraseInverse)