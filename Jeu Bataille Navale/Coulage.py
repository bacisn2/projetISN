# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 20:37:51 2014

@author: mickael
"""

def Coulage(Grille2, IndexCible):#, NbCoulInterm) :
    from TourJoueur import NbCoulInterm
    global NbCoulInterm
    liste = [] #Liste des index des cases qui vont devoir être vérifiées (touché ou non)
    x = 0 #Variable pour le parcourt de la liste des index
    z = 0 #Variable du nombre de case avec bateau qui sont touchées
    #Début des vérifications case par case si il y a un bateau ou non
    #De un en un pour les cases horizontales
    #De vingt en vingt pour les cases verticales
    CoordCible = list(Grille2[IndexCible][0]) #Transforme les coordonnées de l'IndexCible en liste pour être exploitées
    if CoordCible[0] != 605 : #Vérifie la colonne de l'IndexCible
        if Grille2[IndexCible-1][1] == 1 : #Vérification si il y a un bateaux
            a = IndexCible-1 #Variable de l'index de la case
            liste.append(a) #Rajout de cette variable dans la liste des index
            if CoordCible[0] != 625 :
                if Grille2[IndexCible-2][1] == 1 :
                    b = IndexCible-2
                    liste.append(b)
                    if CoordCible[0] != 645 :
                        if Grille2[IndexCible-3][1] == 1 :
                            c = IndexCible-3
                            liste.append(c)
                            if CoordCible[0] != 665 :
                                if Grille2[IndexCible-4][1] == 1 :
                                    d = IndexCible-4
                                    liste.append(d)
                                    if CoordCible[0] != 685 :
                                        if Grille2[IndexCible-5][1] == 1 :
                                            e = IndexCible-5
                                            liste.append(e)
    if CoordCible[0] != 985 :
        if Grille2[IndexCible+1][1] == 1 :
            a = IndexCible+1
            liste.append(a)
            if CoordCible[0] != 965 :
                if Grille2[IndexCible+2][1] == 1 :
                    b = IndexCible+2
                    liste.append(b)
                    if CoordCible[0] != 945 :
                        if Grille2[IndexCible+3][1] == 1 :
                            c = IndexCible+3
                            liste.append(c)
                            if CoordCible[0] != 925 :
                                if Grille2[IndexCible+4][1] == 1 :
                                    d = IndexCible+4
                                    liste.append(d)
                                    if CoordCible[0] != 905 :
                                        if Grille2[IndexCible+5][1] == 1 :
                                            e = IndexCible+5
                                            liste.append(e)
    if CoordCible[1] != 105 : #Teste de la ligne pour CoordCible[1]
        if Grille2[IndexCible-20][1] == 1 :
            a = IndexCible-20
            liste.append(a)
            if CoordCible[1] != 125 :
                if Grille2[IndexCible-40][1] == 1 :
                    b = IndexCible-40
                    liste.append(b)
                    if CoordCible[1] != 145 :
                        if Grille2[IndexCible-60][1] == 1 :
                            c = IndexCible-60
                            liste.append(c)
                            if CoordCible[1] != 165 :
                                if Grille2[IndexCible-80][1] == 1 :
                                    d = IndexCible-80
                                    liste.append(d)
                                    if CoordCible[1] != 185 :
                                        if Grille2[IndexCible-100][1] == 1 :
                                            e = IndexCible-100
                                            liste.append(e)
    if CoordCible[1] != 485 :
        if Grille2[IndexCible+20][1] == 1 :
            a = IndexCible+20
            liste.append(a)
            if CoordCible[1] != 465 :
                if Grille2[IndexCible+40][1] == 1 :
                    b = IndexCible+40
                    liste.append(b)
                    if CoordCible[1] != 445 :
                        if Grille2[IndexCible+60][1] == 1 :
                            c = IndexCible+60
                            liste.append(c)
                            if CoordCible[1] != 425 :
                                if Grille2[IndexCible+80][1] == 1 :
                                    d = IndexCible+80
                                    liste.append(d)
                                    if CoordCible[1] != 405 :
                                        if Grille2[IndexCible+100][1] == 1 :
                                            e = IndexCible+100
                                            liste.append(e)
    #Début des vérifications case par case si il y a un bateau ou non
    print "liste index coulage :" #print pour test
    print liste #print pour test
    while x < len(liste) : #Boucle avec incrémentation de x jusqu'au nombre d'élément dans la liste
        if Grille2[liste[x]][2] == 1 : #Vérification si la case a été touchée ou non
            z = z + 1 #Incrémentation de la variable du nombre de case avec bateau qui sont touchées
        x = x + 1 #Incrémentation de x pour le parcourt de la boucle
    if x == z : #Si le nombre de case avec bateau qui sont touchée est égal au nombre de case devant être vérifiée
        print "Coule" #print pour test
        print "NbCoul avant rajout :" + str(NbCoulInterm) #print pour test
        NbCoulInterm = NbCoulInterm + 1
        print "Le nombre de bateau coule est de " + str(NbCoulInterm)