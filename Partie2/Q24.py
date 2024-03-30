#Fonction ayant en entrée un nombre qui retourne un string 
#indiquant si le nombre en entrée est pair ou impair
def pairOuImpair(nombre):
    if nombre % 2:
        return "Impair"
    else:
        return "Pair"
    

print(pairOuImpair(10))
print(pairOuImpair(15))