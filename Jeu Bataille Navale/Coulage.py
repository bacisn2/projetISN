# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 20:37:51 2014

@author: mickael
"""

def Coulage(Grille2, IndexCible, NbCoul) :
    from Fonction_Ship import Grille2
    liste = []
    x = 0
    z = 0
    if Grille2[IndexCible-1][1] == 1 :
        a = IndexCible-1
        liste.append(a)
        if Grille2[IndexCible-2][1] == 1 :
            b = IndexCible-2
            liste.append(b)
            if Grille2[IndexCible-3][1] == 1 :
                c = IndexCible-3
                liste.append(c)
                if Grille2[IndexCible-4][1] == 1 :
                    d = IndexCible-4
                    liste.append(d)
                    if Grille2[IndexCible-5][1] == 1 :
                        e = IndexCible-5
                        liste.append(e)
    if Grille2[IndexCible+1][1] == 1 :
        a = IndexCible+1
        liste.append(a)
        if Grille2[IndexCible+2][1] == 1 :
            b = IndexCible+2
            liste.append(b)
            if Grille2[IndexCible+3][1] == 1 :
                c = IndexCible+3
                liste.append(c)
                if Grille2[IndexCible+4][1] == 1 :
                    d = IndexCible+4
                    liste.append(d)
                    if Grille2[IndexCible+5][1] == 1 :
                        e = IndexCible+5
                        liste.append(e)
    if Grille2[IndexCible-20][1] == 1 :
        a = IndexCible-20
        liste.append(a)
        if Grille2[IndexCible-40][1] == 1 :
            b = IndexCible-40
            liste.append(b)
            if Grille2[IndexCible-60][1] == 1 :
                c = IndexCible-60
                liste.append(c)
                if Grille2[IndexCible-80][1] == 1 :
                    d = IndexCible-80
                    liste.append(d)
                    if Grille2[IndexCible-100][1] == 1 :
                        e = IndexCible-100
                        liste.append(e)
    if Grille2[IndexCible+20][1] == 1 :
        a = IndexCible+20
        liste.append(a)
        if Grille2[IndexCible+40][1] == 1 :
            b = IndexCible+40
            liste.append(b)
            if Grille2[IndexCible+60][1] == 1 :
                c = IndexCible+60
                liste.append(c)
                if Grille2[IndexCible+80][1] == 1 :
                    d = IndexCible+80
                    liste.append(d)
                    if Grille2[IndexCible+100][1] == 1 :
                        e = IndexCible+100
                        liste.append(e)
    print "liste index coulage :"
    print liste     
    while x < len(liste) :
        if Grille2[liste[x]][2] == 1 :
            z = z + 1
        x = x + 1
    if x == z :
        print "Coulé"
        print "NbCoul avant rajout :" + str(NbCoul)
        NbCoul = NbCoul + 1
        print "Le nombre de bateau coulé est de " + str(NbCoul)