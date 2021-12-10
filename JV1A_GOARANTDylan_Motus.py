import random

from colorama import init
from colorama import Fore, Back, Style
init()


listemotus=["castor", "raisin", "bobine", "bulles", "claque", "discos", "glyphe", "stylet", "thunes", "unique"]
motMystère= random.choice(listemotus)
print(motMystère)
Gagné="Vous avez gagné"
Solution= "C'est Cassé"           #Definition des constantes
affichage = ""
tentatives = 8
reponse=input("Choisissez un mot de 6 lettres \n")

def motus(reponse, affichage):
    couleur=""
    for i in range (len(reponse)):#création du tableau
        if reponse[i] in motMystère:
            couleur=Back.RED+reponse[i]+Back.RESET    #si lettre du mot mystere presente dans le mot proposé colorie en rouge cette lettre
            affichage = affichage+reponse[i]+couleur
        else:
            if reponse[i] not in motMystère:
                couleur=Back.BLUE+reponse+Back.RESET    #si lettre proposée n'est pas présente dans le mot mystere colorie en bleu
                affichage = affichage+reponse[i]+couleur
                print (affichage)
            else:
                couleur=Back.YELLOW+reponse+Back.RESET
                affichage = affichage+couleur   #si lettre proposée n'est pas bien placée dans le mot colorie en jaune
motus(reponse , affichage)

def Victoire(affichage):
    for i in range (len(affichage)):



while tentatives > 0:
    print("\nMot à deviner : ", affichage)
    reponse = input("proposez une lettre : ")[0:1].lower()

    if reponse in motMystère:
        lettres_trouvees = lettres_trouvees + reponse
    print("-> Bien vu!")
        else:
        tentatives = tentatives - 1
        print("il vous reste"+(tentatives))