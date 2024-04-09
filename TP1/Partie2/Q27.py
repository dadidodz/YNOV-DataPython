#Fonction retournant la moyenne d'une liste
def moyenne(liste_nombres):
    return sum(liste_nombres) / len(liste_nombres)

#Liste de nombres
liste_nombres = [1, 12, 48, 20, 10]

print(moyenne(liste_nombres))