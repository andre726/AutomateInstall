# -*- coding: utf-8 -*-

import os



def installationflatpak():
    ''' Installation de logiciel via flatpak'''
    liste_flatpak = [
<<<<<<< HEAD
                     "com.slack.Slack",
                     "com.spotify.Client",
                     "org.signal.Signal",
                     "com.visualstudio.code.oss"
                     #ajouter discord
                     ]
=======

        "com.spotify.Client",
        "org.signal.Signal",
        "com.discordapp.Discord",
        "io.dbeaver.DBeaverCommunity"

    ]
>>>>>>> 4fdeb61e3b3b9d5117a681e096916bfe53ce5ada
    for i in liste_flatpak:
        os.system("flatpak install flathub" + i)


def installbase(installcmd):
    ''' Installation des logiciel de base'''
    software = soft_to_install()
    for i in software:
        os.system("sudo apt instal "+i)

##fonction à supprimé car tout se fait dans le fichier texte.
def ajouteindb(soft):
    '''permet d'ajouter un logiciel dans la db'''

    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Software(Logiciel) VALUES(?);""", (soft,))
    conn.commit()
    cursor.close()







def showcontent():
    """affiche ce qu'il y a dans le fichiers texte"""
   file = open("Software.txt", "r")
   return file.read()


def install_zsh():
    os.system("./install_zsh")


def soft_to_install():
    file = open("Software.txt","r")


<<<<<<< HEAD
def install_zsh():
    #ajout du script de mickael afin de l'automatisé
    print("pas encore fini")
    
=======
    list_software = file.read().split()
    return list_software
# TODO Ajouter une fonction afin de lire juste le contenu d"un fichier texte pour installer les logiciels qui sont nécéssaire
# TODO Supprimé tout ce qui est en rapport avec la base de données et crée un fichier pour les serveurs
>>>>>>> 4fdeb61e3b3b9d5117a681e096916bfe53ce5ada
