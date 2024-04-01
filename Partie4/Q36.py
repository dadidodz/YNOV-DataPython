#Importe le module datetime
import datetime

#Fonction qui retourne l'année de naissance en fonction de l'âge en paramètre
def calcul_annee_naissance(age):
    return datetime.datetime.now().year - age

def main():
    #Demande le nom, l'âge et la ville du l'utilisateur
    nom = input("Renseignez votre nom : ")
    age = int(input("Renseignez votre âge : "))
    ville = input("Renseignez votre ville : ")

    #Stocke les informations dans un dictionnaire
    utilisateur = {
        "nom": nom,
        "age": age,
        "ville": ville
    }

    print("")
    #Afficher un message avec les informations renseignées par l'utilisateur
    print(f"Bonjour {utilisateur['nom']}, vous avez {utilisateur['age']} ans et vous vivez à {utilisateur['ville']}.")

    #Calcule et affiche l'année de naissance
    annee_naissance = calcul_annee_naissance(utilisateur['age'])
    print(f"Vous êtes né(e) en {annee_naissance}.")

#Appel de la fonction "main"
if __name__ == "__main__":
    main()