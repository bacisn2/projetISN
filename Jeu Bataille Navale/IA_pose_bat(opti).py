# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 18:35:51 2014

@author: mickael
"""

import random

def IA_Pose_Bat() : #Pose des bateaux par l'IA
    global batcase
    global IndexCase
    global Grille2
    global EchecPosition
    global Case
    EchecPosition = False #On initialise l'echec de position
    x = 0 #Variable pour le déplacement dans la liste listship
    listship = [6,5,4,4,3,3,3,2,2,2] #Nombre de cases des différents bateaux
    while x < 10 : #Dix fois pour dix bateaux
        batcase = listship[x] #Le nombre de case d'un beateau celon la position dans la liste
        b = random.randint(0,1) #Variable pour le choix Verticale/Horizontal du bateau
        IndexCase = random.randint(0,398) #Choix d'un index dans la liste des coordonnées Grille2
        if b == 0 : #Choix Verticale du bateau
            case = Grille2[IndexCase] #La case de positionnement du bateau celon l'index choisis 
            Fonction_Verif_PositionIA_Brute_for_V() #Appel fonction vérifiant position bateaux verticaux dans Grille2 
        else : #Choix Horizontal du bateau
            case = Grille2[IndexCase]   
            Fonction_Verif_PositionIA_Brute_for_H() #Appel fonction vérifiant position bateaux horizontaux dans Grille2
        if EchecPosition == False : 
            x = x + 1
        EchecPosition = False #Réinitialisation de l'echec de posistion
            
#Vérifient que le bateau ne soit pas hors case (spécifique aux navires Verticaux)
def Fonction_Verif_PositionIA_Brute_for_V() : 
    #On globalise toutes les variables
    global batcase
    global Grille2
    global Case
    global IndexCase
    global EchecPosition
    i = 1
    #Les Tuple ne pouvant être modifié, on transforme "Coord" en Liste pour travailler dessus
    TupleCase = list(Grille2[IndexCase][0])
    print("\n") #Test Fais un saut de ligne
    print("Fonction_Verif_Position_Brute") #Test
    print(IndexCase) #Test
    #Boucle qui vérifie que toutes les cases que prendra le bateau existent 
    #Va vérifier que les Colonnes concordent avec les cases existentes (la coordonné la plus basse est 485)      
    while i <= batcase : #Boucle pour faire toutes les cases du bateau
        print(TupleCase) #Test
        if TupleCase[1] <= 485: #Si la deuxième coordonée (ordonnée) est dans la Grille2 (ordonnée max==485)
            i = i + 1 #On passe à la case suivante du bateau
            TupleCase[1] = TupleCase[1] + 20 #Coordonnée suivante
        else:
            print("bateau hors quadrillage.") #Test
            EchecPosition = True
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction "while"
        if EchecPosition == False :
            print("OK for Position Brute") #Test

#Vérifient que le bateau ne soit pas hors case (spécifique aux navires Horizontaux)            
def Fonction_Verif_PositionIA_Brute_for_H() :
    #On globalise toutes les variables
    global batcase
    global Grille2
    global Case
    global IndexCase
    global EchecPosition
    i = 1
    #Les Tuple ne pouvant être modifié, on transforme "Coord" en Liste pour travailler dessus       
    TupleCase = list(Grille2[IndexCase][0])
    print("\n") #Test Fais un saut de ligne
    print("Fonction_Verif_Position_Brute") #Test
    print(IndexCase) #Test
    #Boucle qui vérifie que toutes les cases que prendra le bateau existent 
    #Va vérifier que les Lignes concordent avec les cases existentes (la coordonné la plus basse est 985)       
    while i <= batcase : #Boucle pour faire toutes les cases du bateau
        print(TupleCase) #Test
        if TupleCase[0] <= 985: #Si la première coordonée (abscisse) est dans la Grille2 (abscisse max==985)
            i = i+1 #On passe à la case suivante du bateau
            TupleCase[0] = TupleCase[0] + 20 #Coordonnée suivante
        else:
            print("bateau hors quadrillage.") #Test
            EchecPosition = True
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction "while"
    if EchecPosition == False :
        print("OK for Position Brute") #Test

