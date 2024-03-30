#Fonction retournant la moyenne d'une liste
def moyenne(listeNombres):
    return sum(listeNombres) / len(listeNombres)

#Liste de nombres
listeNombres = [1, 12, 48, 20, 10]

print(moyenne(listeNombres))