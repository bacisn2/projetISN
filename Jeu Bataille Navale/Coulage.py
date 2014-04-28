# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 20:37:51 2014

@author: mickael
"""

def Coulage() :
    from Fonction_Ship import Grille2
    global IndexCible
    global Grille2
    global NbCoul
    if Grille2[IndexCible-1][1] == 1 :
        a = IndexCible-1
        if Grille2[IndexCible-2][1] == 1 :
            b = IndexCible-2
            if Grille2[IndexCible-3][1] == 1 :
                c = IndexCible-3
                if Grille2[IndexCible-4][1] == 1 :
                    d = IndexCible-4
                    if Grille2[IndexCible-5][1] == 1 :
                        e = IndexCible-5
    else :
        a = IndexCible+1
    if Grille2[IndexCible+2][1] == 1 :
        b = IndexCible+2
        if Grille2[IndexCible+3][1] == 1 :
            c = IndexCible+3
            if Grille2[IndexCible+4][1] == 1 :
                d = IndexCible+4
                if Grille2[IndexCible+5][1] == 1 :
                    e = IndexCible+5
    if Grille2[IndexCible-20][1] == 1 :
        a = IndexCible-20
        if Grille2[IndexCible-40][1] == 1 :
            b = IndexCible-40
            if Grille2[IndexCible-60][1] == 1 :
                c = IndexCible-60
                if Grille2[IndexCible-80][1] == 1 :
                    d = IndexCible-80
                    if Grille2[IndexCible-100][1] == 1 :
                        e = IndexCible-100
    else :
        a = IndexCible+20
    if Grille2[IndexCible+40][1] == 1 :
        b = IndexCible+40
        if Grille2[IndexCible+60][1] == 1 :
            c = IndexCible+60
            if Grille2[IndexCible+80][1] == 1 :
                d = IndexCible+80
                if Grille2[IndexCible+100][1] == 1 :
                    e = IndexCible+100
    if Grille2[a][2] == 1 :
        if Grille2[b][2] == 1 :
            if Grille2[c][2] == 1 :
                if Grille2[d][2] == 1 :
                    if Grille2[e][2] == 1 :
                        NbCoul = NbCoul + 1
                        print "Coulé"
                        
def CoulageIA() :
    from Fonction_Ship import Grille1
    global IndexCible
    global Grille2
    global NbCoulIA
    if Grille1[IndexCible-1][1] == 1 :
        a = IndexCible-1
        if Grille1[IndexCible-2][1] == 1 :
            b = IndexCible-2
            if Grille1[IndexCible-3][1] == 1 :
                c = IndexCible-3
                if Grille1[IndexCible-4][1] == 1 :
                    d = IndexCible-4
                    if Grille1[IndexCible-5][1] == 1 :
                        e = IndexCible-5
    else :
        a = IndexCible+1
    if Grille1[IndexCible+2][1] == 1 :
        b = IndexCible+2
        if Grille1[IndexCible+3][1] == 1 :
            c = IndexCible+3
            if Grille1[IndexCible+4][1] == 1 :
                d = IndexCible+4
                if Grille1[IndexCible+5][1] == 1 :
                    e = IndexCible+5
    if Grille1[IndexCible-20][1] == 1 :
        a = IndexCible-20
        if Grille1[IndexCible-40][1] == 1 :
            b = IndexCible-40
            if Grille1[IndexCible-60][1] == 1 :
                c = IndexCible-60
                if Grille1[IndexCible-80][1] == 1 :
                    d = IndexCible-80
                    if Grille1[IndexCible-100][1] == 1 :
                        e = IndexCible-100
    else :
        a = IndexCible+20
    if Grille1[IndexCible+40][1] == 1 :
        b = IndexCible+40
        if Grille1[IndexCible+60][1] == 1 :
            c = IndexCible+60
            if Grille1[IndexCible+80][1] == 1 :
                d = IndexCible+80
                if Grille1[IndexCible+100][1] == 1 :
                    e = IndexCible+100
    if Grille1[a][2] == 1 :
        if Grille1[b][2] == 1 :
            if Grille1[c][2] == 1 :
                if Grille1[d][2] == 1 :
                    if Grille1[e][2] == 1 :
                        NbCoulIA = NbCoulIA + 1
                        print "Coulé"