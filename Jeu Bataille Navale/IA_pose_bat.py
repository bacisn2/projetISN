# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 16:18:58 2014

@author: mickael
"""

import random
import Dico_Grille2
from Fonction_Ship import *
CasePlayer2 = Dico_Grille2.GrillePlayer2
ordonnee = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
abscisse = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a = random.randrange(0,2)
if a ==0 :
    bat = "CuirSuper"  #Bateau "6 cases" horizontale
    NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
    EchecPosition = True
    while EchecPosition == True :
        o = random.choice(ordonnee)
        a = random.choice(abscisse)
        coord = oa
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
            Nb6Case = Nb6Case+1
else :
    bat = "CuirSuperV"  #Bateau "6 cases" horizontale
    NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
    EchecPosition = True
    while EchecPosition == True :
        o = random.choice(ordonnee)
        a = random.choice(abscisse)
        coord = oa
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
            Nb6Case = Nb6Case+1