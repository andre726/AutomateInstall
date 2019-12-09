# -*- coding: utf-8 -*-

import os
import sqlite3
import distro


def installationflatpak():
    ''' Installation de logiciel spécifique au developpeur'''
    liste_flatpak = ["com.jetbrains.PyCharm-Community",
                     "com.slack.Slack",
                     "com.spotify.Client",
                     "io.dbeaver.DBeaverCommunity",
                     "org.signal.Signal","org.telegram.desktop",
                     "com.visualstudio.code.oss"
                     #ajouter discord
                     ]
    for i in liste_flatpak:
            os.system("flatpak install "+i)


def installbase(cmdinstall):
    ''' Installation des logiciel de base'''
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    distrotype = os_distribution()
    sqlrequest= 'SELECT * FROM '+distrotype+' ORDER BY Logiciel'
    
    for row in cursor.execute(sqlrequest):
        os.system(install_cmd()+" "+row[0])
        


def ajouteindb(soft):
    '''permet d'ajouter un logiciel dans la db'''

    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Ubuntu(Logiciel) VALUES(?);""", (soft,))
    conn.commit()
    cursor.close()





def supprimer(logiciel):
    '''Permet de supprimer un logiciel de la base de données'''
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    sqlrequest = "DELETE FROM "+os_distribution()+ " WHERE Logiciel = ?"
    cursor.execute(sqlrequest, (logiciel,))
    conn.commit()
    conn.close()


def creadb():
    '''création de la base de donnée avec les différente tables et colone'''
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS Ubuntu(
     Logiciel TEXT,
     Adresse TEXT,
     Commande TEXT
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS Fedora(
     Logiciel TEXT,
     Adresse TEXT,
     Commande TEXT
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS Manjaro(
     Logiciel TEXT,
     Adresse TEXT,
     Commande TEXT
)
""")
    conn.commit()
    conn.close()


def showcontent():
    """montre ce qu'il y dans la base de données"""
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    sqlrequest = "SELECT * FROM "+ os_distribution()+ " ORDER BY Logiciel"
    for row in cursor.execute(sqlrequest):

        return row


def install_cmd():
    '''détermine le système linux utiliser afin d'utiliser la bonne commande d'installation'''
    distrotype = distro.linux_distribution()
    systeme = distrotype[0]
    
    if systeme == "Linux Mint" or systeme == "Debian" or systeme == "Ubuntu":
        install = 'sudo apt install'
        return install
    elif systeme == "Manjaro" or "Arch Linux":
        install = " sudo pamac -S"
        return install
    elif systeme == "CentOS" or "Fedora":
        install = "sudo dnf install"
        return install
    else:
        return "il doit y avoir une erreur"

def os_distribution():
    '''détermine le système linux utiliser afin d'avoir le bon nom de la table dans la bdd'''
    distrotype = distro.linux_distribution()
    systeme = distrotype[0]
    
    if systeme == "Linux Mint" or systeme == "Debian" or systeme == "Ubuntu":
        osdistribution = 'Ubuntu'
        return osdistribution
    elif systeme == "Manjaro" or "Arch Linux":
        osdistribution = " Manjaro"
        return osdistribution
    elif systeme == "CentOS" or "Fedora":
        osdistribution = "sudo dnf install"
        return osdistribution
    else:
        return "il doit y avoir une erreur" 
