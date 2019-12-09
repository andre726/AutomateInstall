# -*- coding: utf-8 -*-
import functions

functions.creadb()
choix = 0
functions.showcontent()

cmdinstall=functions.install_cmd()

while choix!=4:
    print("Script d'installation logiciel, que voulez vous faire? \n choississez 1 pour installez tout les logiciel \n choissisez 2 pour ajouter une logiciel dans la base de donnée \n choissiez 3 pour supprimé un logiciel de la  base de donnée \n choissisez sur 4 pour quitter")
    choix = int(input("votre choix : "))
    if choix== 1:
        functions.installbase(cmdinstall)
        functions.installationflatpak()

    elif choix ==2:
        logiciel =input("quel logiciel souhaitez vous ajouter?: ")
        functions.ajouteindb(logiciel)
    elif choix==3:
        logiciel=input("quel logiciel souhaitez vous enlever?")
        functions.supprimer(logiciel)
    else:
        print("aucun choix n'est correct, veuillez recommencer")
        break

