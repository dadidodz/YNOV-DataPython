#Importe le module datetime
import datetime

#Fonction qui retourne l'âge en fonciton de l'âge 
#de l'utilisateur ainsi que l'année souhaitée
def calcul_annee_future(age, annee):
    return annee - (datetime.datetime.now().year - age)

def main():
    #Variables espérance de vie, année, mois et jour actuel
    esperance_vie = 85
    annee = datetime.datetime.now().year
    mois = datetime.datetime.now().month
    jour = datetime.datetime.now().day

    #Demande le prenom, l'âge et l'année à laquelle il souhaite savoir l'âge qu'il aura
    prenom = input("Renseignez votre prenom : ")
    age = int(input("Renseignez votre âge : "))
    annee_future = int(input("Renseignez l'annee à laquelle vous souhaitez savoir l'age que vous aurez : "))

    #Variable stockant le résultat de la fonction calcul_annee_future
    age_res = calcul_annee_future(age, annee_future)

    print("")
    #Afficher le prénom de l'utilisateur ainsi que la date actuelle
    #Le prénom est affichée avec une majuscule
    print(f"Bonjour {prenom.capitalize()}, aujourd'hui nous sommes le {jour} / {mois} / {annee}.")

    #Affiche un message différent selon les valeurs des variables annee_future et annee, ou, age_res et esperance_vie
    if annee_future < annee:
        print(f"L'annee renseignée précède l'année actuelle.")
    elif age_res > esperance_vie :
        print(f"Vous avez actuellement {age}ans, en {annee_future} vous en aurez plus de {esperance_vie} ans,")
        print(f"{age_res} exactement, ce qui est plus que l'espérance de vie")
    else:
        print(f"Vous avez actuellement {age} ans, en {annee_future} vous en aurez {age_res}.")

#Appel de la fonction "main"
if __name__ == "__main__":
    main()