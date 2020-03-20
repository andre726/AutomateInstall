# -*- coding: utf-8 -*-

import os
import sqlite3


def installationflatpak():
    ''' Installation de logiciel via flatpak'''
    liste_flatpak = [
                     "com.slack.Slack",
                     "com.spotify.Client",
                     "org.signal.Signal","org.telegram.desktop",
                    "com.discordapp.Discord",
                    "io.dbeaver.DBeaverCommunity"

                     ]
    for i in liste_flatpak:
            os.system("flatpak install flathub"+i)


def installbase(installcmd):
    ''' Installation des logiciel de base'''
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    sqlrequest= 'SELECT * FROM Software ORDER BY Logiciel'
    
    for row in cursor.execute(sqlrequest):
        os.system(installcmd+" "+row[0])
        


def ajouteindb(soft):
    '''permet d'ajouter un logiciel dans la db'''

    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Software(Logiciel) VALUES(?);""", (soft,))
    conn.commit()
    cursor.close()





def supprimer(logiciel):
    '''Permet de supprimer un logiciel de la base de données'''
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    sqlrequest = "DELETE FROM Software WHERE Logiciel = ?"
    cursor.execute(sqlrequest, (logiciel,))
    conn.commit()
    conn.close()


def creadb():
    '''création de la base de donnée avec les différente tables et colone'''
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS Software(
     Logiciel TEXT)
""")

    conn.commit()
    conn.close()


def showcontent():
    """affiche ce qu'il y a dans la base de données"""
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    sqlrequest = "SELECT * FROM  Software ORDER BY Logiciel"
    for row in cursor.execute(sqlrequest):
         print(row)



def install_zsh():
    os.system("./install_zsh")
