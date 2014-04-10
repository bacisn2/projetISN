# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 18:35:51 2014

@author: mickael
"""

import random

<<<<<<< HEAD
def IA_Pose_Bat():
    #on globalise toutes les variables
=======
def IA_Pose_Bat() : #Pose des bateaux par l'IA
>>>>>>> b8449c024f1bc890e9a59a0cf019fc8d54c1dc93
    global batcase
    global IndexCase
    global Grille2
    global EchecPosition
<<<<<<< HEAD
    x = 0 #compteur pour mettre dix bateaux
    ListShip = [6,5,4,4,3,3,3,2,2,2]
    while x < 10 :
        batcase = ListShip[x]
        b = random.randint(0,1) #aléatoire pour verticale ou horizontal
        IndexCase = random.randint(0, 398) #choisi une case au hasard dans Grille2
        if b == 0 :
            Case = Grille2[IndexCase]
            #appelle fonction
        else:
            Case = Grille2[IndexCase]
            #appelle fonction 
        if EchecPosition == False:
            if b == 0:
                #appelle Fonction BPB
                Check_IA_Ship_H
            else:
                #appelle Fonction BPB
                Check_IA_Ship_V                
            x = x+1
            
def Check_IA_Ship():
    #On globalise les variables
    global Grille2
    global dessus
    global dessous
    global gauche
    global droite
    global TupleCoord
    global Echec
    global IndexCase
    print("\n")
    print("IndexCase = " + str(IndexCase))
    Grille2[IndexCase][3] = 1
    print("1er case: ")
    print(Grille2[IndexCase])
    #Variable Bolléenne qui détermine si il existe des cases en dessous/dessus/droite/gauche 
    #de la case choisi (on part du principe que "oui"), True = la (les) case(s) existe(nt)
    dessus = True
    dessous = True
    droite = True
    gauche = True
    #Variable qui détermine le sens du navire (Horizontale/Verticale)
    H = 0
    V = 0
    TupleCoord = list(Grille2[IndexCase][0])
    #détermination des cases existante (quatre test)
    #Si les test sont "Vrais", alors les cases en question n'existent pas
    if IndexCase-1 < 0: #Y a-t-il une case à gauche ?
        gauche = False
    if TupleCoord[0]+20 > 485: #Y a-t-il une case à droite ?
        droite = False
    if IndexCase+20 > len(Grille2): #Y a-t-il une case en dessous ?
        dessous = False
    if TupleCoord[1]-20 < 105: #Y a-t-il une case au dessus ?
        dessus = False
        
    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
    print("\n")
    print("dessus = " + str(dessus))
    print("dessous = " + str(dessous))
    print("gauche = " + str(gauche))
    print("droite = " + str(droite))
    print("TupleCoordTestAbsisse (test droite): " + str(TupleCoord[0]+20))
    print("TupleCoordTestOrdonnee (test dessus): " + str(TupleCoord[1]-20))
    print("IndexTestgauche: " + str(IndexCase-1))
    print("IndexTestdessous: " + str(IndexCase+20))
    print("\n")
    #FIN Partie TEST
                    
    #Travail sur les cases du dessus (si elles existent):
    if dessus == True: #Cases supérieures
        print("passage --> case dessus")
        Grille2[IndexCase-20][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if droite == True: #Case supérieure droite (diagonale)
            print("passage --> case dessus droite")
            Grille2[IndexCase-19][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if gauche == True: #Case  supérieure gauche (diagonale)
            print("passage --> case gauche")
            Grille2[IndexCase-21][3] = 1 #On n'oublie pas de checker la case dans le cas contraire  
        
    #Travail sur les cases du dessous (si elles existent):        
    if dessous == True: 
        print("passage --> case dessous")
        if droite == True: #Case inférieure droite (diagonale)
            print("passage --> case dessous droite")
            Grille2[IndexCase+21][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if gauche == True: #Case inférieure gauche (diagonale)
            print("passage --> case dessous gauche")
            Grille2[IndexCase+19][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if Grille2[IndexCase+20][1] == 1: #Case immédiatement au dessous 
            Grille2[IndexCase+20][3] = 1  #On check la Case                          
            V = V+1 #Si un bateau se trouve ici, c'est que le navire doit être vertical
        else:
            Grille2[IndexCase+20][3] = 1  #On check la Case
            
    #Travail sur la case à gauche (si elle existe):          
    if gauche == True:
        print("passage --> case gauche")
        Grille2[IndexCase-1][3] = 1 #On n'oublie pas de checker la case dans le cas contraire 
    #Travail sur la case à droite (si elle existe):        
    if droite == True:
        print("passage --> case droite")
        if Grille2[IndexCase+1][1] == 1: #Case immédiatement à droite
            Grille2[IndexCase+1][3] = 1  #On check la Case
            H = H+1 #Si un bateau se trouve ici, c'est que le navire doit être horizontal
        else:
            Grille2[IndexCase+1][3] = 1  #On check la Case
                        
    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
    #Les nombreux test de variables servent à éviter des bugs liés à l'affichage des cases (au cas où elles n'existeraient pas)
    print("\nFin Passage check PI")
    print("ListeCases (dans l'ordre du dessin)")
    if dessus == True:
        if gauche == True:
            print(Grille2[IndexCase-19])
        print(Grille2[IndexCase-20])
        if droite == True:
            print(Grille2[IndexCase-21])
    if droite == True:
        print(Grille2[IndexCase-1])
    if dessous == True:
        if droite == True:
            print(Grille2[IndexCase+19])
        print(Grille2[IndexCase+20])
        if gauche == True:
            print(Grille2[IndexCase+21])
    if gauche == True:
        print(Grille2[IndexCase+1])
    print("Horizontal = " + str(H))
    print("Vertical = " +str(V))
    print("\n")
    #FIN Partie TEST
                
    #Détermination du type de navire (Horizontale/Verticale) à l'aide des variable H/V:                   
    if H > 0 and V == 0: #Le bateau est-il Horizontal ?
        #La technique utilisé pourra être réutiliser pour la programme "Coulage des Navires" de l'IA
        print("Verif_Final_PII_NavireH")                        
        Check_PII_NavireH_IA()
    elif H == 0 and V > 0: #Le bateau est-il Verticale ?
        #La technique utilisé pourra être réutiliser pour la programme "Coulage des Navires" de l'IA
        print("Verif_Final_PII_NavireV")                        
        Check_PII_NavireV_IA()
    print("\n")
    print("FIN DU CHECK DU NAVIRE") #Utile à savoir
    print("\n")

    
def Check_PII_NavireH_IA(): #Spécifique aux navires horizontaux
    #on globalise les variables
    global Grille2
    global dessus
    global dessous
    global droite
    global TupleCoord
    global Echec
    global batcase
    NbCase = 2 #On commence à la deuxième case
    for NbCase in range (batcase): #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        print("\n")
        print("Case: " + str(NbCase))
        print("Index: " + str(IndexCase)) 

        #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
        print("TupleAbsisse: " + str(TupleCoord[0]+20*NbCase))
        print("Case testé: ")
        print(Grille2[IndexCase+2])
        if dessus == True:
            print("case dessus: ")
            print(Grille2[IndexCase-18])
        if dessous == True:
            print("case dessous: ")
            print(Grille2[IndexCase+22])
        #FIN Partie TEST
            
        #La case suivante appartient t'elle au bateau ?
        Grille2[IndexCase+2][3] = 1 #On check la Case
        if dessus == True: #On vérifie que la case au dessus existe...
            Grille2[IndexCase-18][3] = 1 #On n'oublie pas de checker la Case 
        if dessous == True:  #On vérifie que la case en dessous existe...
            Grille2[IndexCase+22][3] = 1 #On n'oublie pas de checker la Case
    
    if droite == True: #On check les cases à droite si elles existent
        Grille2[IndexCase+3][3] = 1 #On check la Case
        if dessus == True: #On vérifie que la case au dessus existe...
            Grille2[IndexCase-17][3] = 1 #On n'oublie pas de checker la Case 
        if dessous == True:  #On vérifie que la case en dessous existe...
            Grille2[IndexCase+23][3] = 1 #On n'oublie pas de checker la Case
                
    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
    print("\nCase après ckeck")
    print("Case testé: ")
    print(Grille2[IndexCase+2])
    if dessus == True:
        print("case dessus: ")
        print(Grille2[IndexCase-18])
    if dessous == True:
        print("case dessous: ")
        print(Grille2[IndexCase+22])
    #FIN Partie TEST
    
def Check_PII_NavireV_IA(): #Spécifique aux navires verticaux
    #on globalise les variables
    global Grille2
    global gauche
    global dessous
    global droite
    global TupleCoord
    global Echec
    global batcase
    NbCase = 2 #On commence à la deuxième case
    for NbCase in range (batcase): #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        print("\n")
        print("Case: " + str(NbCase))
        print("Index: " + str(IndexCase)) 

        #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
        print("TupleAbsisse: " + str(TupleCoord[1]+20*NbCase))
        print("Case testé: ")
        print(Grille2[IndexCase+40])
        if gauche == True:
            print("case dessus: ")
            print(Grille2[IndexCase+39])
        if droite == True:
            print("case dessous: ")
            print(Grille2[IndexCase+41])
        #FIN Partie TEST
            
        #La case suivante appartient t'elle au bateau ?
        Grille2[IndexCase+40][3] = 1 #On check la Case
        if gauche == True: #On vérifie que la case au dessus existe...
            Grille2[IndexCase+39][3] = 1 #On n'oublie pas de checker la Case 
        if droite == True:  #On vérifie que la case en dessous existe...
            Grille2[IndexCase+41][3] = 1 #On n'oublie pas de checker la Case
    
    if dessous == True: #On check les cases en dessous si elle existe
        IndexCase = IndexCase+1
        Grille2[IndexCase+60][3] = 1 #On check la Case
        if gauche == True: #On vérifie que la case au dessus existe...
            Grille2[IndexCase+59][3] = 1 #On n'oublie pas de checker la Case 
        if droite == True:  #On vérifie que la case en dessous existe...
            Grille2[IndexCase+61][3] = 1 #On n'oublie pas de checker la Case
                
    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
    print("\nCase après ckeck")
    print("Case testé: ")
    print(Grille2[IndexCase+40])
    if gauche == True:
        print("case dessus: ")
        print(Grille2[IndexCase+39])
    if droite == True:
        print("case dessous: ")
        print(Grille2[IndexCase+41])
    #FIN Partie TEST
=======
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

>>>>>>> b8449c024f1bc890e9a59a0cf019fc8d54c1dc93
