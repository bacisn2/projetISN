# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 18:35:51 2014

@author: mickael
"""

import random
import Dico_Grille2
from Fonction_Ship import *
CasePlayer2 = Dico_Grille2.GrillePlayer2
ordonnee = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
abscisse = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
bateaux = ["CuirSuper","PA","CuirBase","Cuir2","SM","MNB","MNR","LitShip","Voilier"]
bateauxV = ["CuirSuperV","PAV","CuirBaseV","Cuir2V","SMV","MNBV","MNRV","LitShip","Voilier"]
x = 0 #compteur pour mettre neuf bateaux
for x in range(9) : #il manque un bateau dans les listes pour en avoir dix
    b = random.randint(0,1) #aléatoire pour verticale ou horizontal
    if b == 0 :
        bat = bateaux[x] #choisis les bateaux de la liste un par un celon leur place
        o = random.choice(ordonnee) 
        a = random.choice(abscisse)
        oa = o + a #permet de coller les deux coordonées
        coord = oa
    else :
        bat = bateauxV[x]
        o = random.choice(ordonnee)
        a = random.choice(abscisse)
        oa = o + a
        coord = oa