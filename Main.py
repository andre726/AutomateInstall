# -*- coding: utf-8 -*-
import functions

functions.creadb()
choix = 0
functions.showcontent()
functions.soft_to_install()




while choix!=4:
    print("Script d'installation logiciel, que voulez vous faire? \n choississez 1 pour installez tout les logiciel \n choissisez 2 pour ajouter une logiciel dans la base de donnée \n choissiez 3 pour supprimé un logiciel de la  base de donnée \n choississez 4 pour afficher la liste des logiciel dans la base de données \n choissisez  5 pour quitter")
    choix = int(input("votre choix : "))
    if choix== 1:
        print("Quel est votre gestionnaire de paquet? le taper  \n exemple : sudo apt install")
        installateur= input("commande de votre installateur : ")
        functions.installbase(installateur)
        functions.install_zsh()
        functions.installationflatpak()
    elif choix ==2:
        logiciel =input("quel logiciel souhaitez vous ajouter?: ")
        functions.ajouteindb(logiciel)
    elif choix==3:
        logiciel=input("quel logiciel souhaitez vous enlever?")
        functions.supprimer(logiciel)
    elif choix==4:
        functions.showcontent()
    else:
        break

