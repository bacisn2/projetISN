# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:47:41 2014

@author: IG 158
"""

# Liste des fonctions utile pour le programme de recherche de navire de l'IA

import Fonction_Ship
from random import *
from Fonction_Ship import Grille1

def Define_List_Case_and_Strategie():
    global Grille1
    global CaseIA
    #variable locale utile
    x = 0
    y = True
    #Variable Stratégie IA
    A_Z = False
    Z_A = False
    Random = False
    #Liste des cases que l'IA choisira)
    CaseIA = []
    for x in range(0, 20):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(20, 40):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(40, 60):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(60, 80):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(80, 100):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(100, 120):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(120, 140):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(140, 160):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(160, 180):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(180, 200):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(200, 220):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(220, 240):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(240, 260):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(260, 280):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(280, 300):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(300, 320):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(320, 340):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(340, 360):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(360, 380):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(380, 400):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    print("Liste Case IA:")
    print(CaseIA)
    print("\n")
    x = randint(1,3)
    print("choix strategie = " + str(x))
    if x == 1:
        A_Z = True
        print("Strategie A a Z")
        #Stratégie A à Z
    elif x == 2:
        Z_A = True
        print("Strategie Z a A")
        #Stratégie Z à A
    else:
        Random = True
        print("Strategie Case Aleatoire")
        #Stratégie case aléatoire
        
    