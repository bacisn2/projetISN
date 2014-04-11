# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 17:21:26 2014

@author: IG 158
"""

#Listes des Fonctions d'Initialisation utile pour le jeu (seront importer dans la partie "IMPORTATION" du programme principal)

#SOMMAIRE DES FONCTIONS (NB: Incomplet à ce jour: en attente des Fonctions pour les Parties V - VII et IX) - ligne: 10
#I - PARTIE IMPORTATION DES DICOS ET INITIALISATION DES COMPTEURS DE NAVIRES
#   Importaion Dico - ligne: 66
#   Initialisation Compteurs Navires - ligne: 69
#
#II - PARTIE FONCTIONS D'INITIALISATION GRILLES
#   Grille1 - ligne: 80
#   Grille2 - ligne: 99
#
#III - PARTIE FONCTION POSITIONNEMENT DES NAVIRES
#   Grille1_Pos_Navire (Entrée du bateau et de la case - For Joueur) - ligne: 122
#   "A-FAIRE" Grille2_Pos_Navire (Entrée du bateau et de la case - For IA) - ligne: Unknow
#
#IV - PARTIE FONCTIONS VERIFICATION POSITIONNEMENT JOUEUR
#   Notes utiles (commentaire) - ligne: 155
#   Fonction_Search_Index_CaseListe_for_Grille1 (recherche l'index de la case à partir de ses coordonnées) - ligne: 165
#   Verif_VariableBPB_in_Grille1_for_H (vérifie l'état de BPB pour les navires Horizontaux) - ligne: 181
#   Verif_VariableBPB_in_Grille1_for_V (vérifie l'état de BPB pour les navires Verticaux) - ligne: 209
#   Fonction_Verif_Position_Brute_for_V (vérifie que le bateau vertical est entièrement dans la grille) - ligne: 239
#   Fonction_Verif_Position_Brute_for_H (vérifie que le bateau horizontal est entièrement dans la grille) - ligne: 275
#
#V - PARTIE FONCTIONS VERIFICATION POSITIONNEMENT IA (NB: Cette partie n'existe pas encore) 
#   "A-FAIRE" Notes utiles (commentaire) - ligne: Unknow
#   Fonction_Search_Index_CaseListe_for_Grille2 (recherche l'index de la case à partir de ses coordonnées) - ligne: 315
#   Verif_VariableBPB_in_Grille2_for_H (vérifie l'état de BPB pour les navires Horizontaux) - ligne: 325
#   Verif_VariableBPB_in_Grille2_for_V (vérifie l'état de BPB pour les navires Verticaux) - ligne: 352
#   "A-FAIRE" (vérifie que le bateau vertical est entièrement dans la grille) - ligne: Unknow
#   "A-FAIRE" (vérifie que le bateau horizontal est entièrement dans la grille) - ligne: Unknow
#
#VI - PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB) JOUEUR
#   Grille1_Navire_Horizontale (change BPB pour les autres cases des navires horizontaux) - ligne: 387
#   Grille1_Navire_Verticale (change BPB pour les autres cases des navires verticaux) - ligne: 408
#   Chgmt_State_Case1 (change BPB pour la première case du navire choisi) - ligne: 429
#   ListShip_for_Chgmt_State (Fonction Maître de la Partie: détermine le navire choisi et appelle les fonctions ci-dessus au besoins) - ligne: 448
#
#VII - PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB) IA
#   "A-FAIRE" (change BPB pour les autres cases des navires horizontaux) - ligne: Unknow
#   "A-FAIRE" (change BPB pour les autres cases des navires verticaux) - ligne: Unknow
#   "A-FAIRE" (change BPB pour la première case du navire choisi) - ligne: Unknow
#   "A-FAIRE" (Fonction Maître de la Partie: détermine le navire choisi et appelle les fonctions ci-dessus au besoins) - ligne: Unknow
#
#VIII - PARTIE VERIFICATION FINALE JOUEUR
#   Verification_Final_Grille1 (Fonction Maître de la Partie: gère la première case et évite les bug lié à des cases inexistantes) - ligne: 596
#   Verif_Final_PII_NavireH (vérifie les cases adjacentes des cases suivantes des navires horizontaux) - ligne: 800
#   Verif_Final_PII_NavireV (vérifie les cases adjacentes des cases suivantes des navires verticaux) - ligne: 887
#   Reinitialisation_NbXCase (réinitialise les Compteurs Navires en case de réinitialisation de la partie) - ligne: 981
#
#IX - PARTIE CHECK CASE IA
#   "A-FAIRE" (Fonction Maître de la Partie: gère la première case et évite les bug lié à des cases inexistantes) - ligne: Unknow
#   "A-FAIRE" (vérifie les cases adjacentes des cases suivantes des navires horizontaux) - ligne: Unknow
#   "A-FAIRE" (vérifie les cases adjacentes des cases suivantes des navires verticaux) - ligne: Unknow
#   "A-FAIRE" (réinitialise les Compteurs Navires de l'IA en case de réinitialisation de la partie) - ligne: Unknow
# FIN SOMMAIRE DES FONCTIONS

#DEBUT PROGRAMME "FONCTION_SHIP"
#//////////////////////////////////////////////////////////////////////////////
#PARTIE IMPORTATION DES DICOS
import Dico_Ship
import Dico_Grille1
import random
#INITIALISATION DES COMPTEURS DE NAVIRES
Nb2Case = 0
Nb3Case = 0
Nb4Case = 0
Nb5Case = 0
Nb6Case = 0
#FIN PARTIE IMPORTATION DES DICOS

#//////////////////////////////////////////////////////////////////////////////
#PARTIE FONCTIONS D'INITIALISATION GRILLES
#Fonctions d'Initialisation des Grilles
def IniListeCaseGrille1():
    global Grille1
    Grille1 = []
    x = 105 #Première coordonnées possible en "X"
    y = 85  #Première coordonnées possible en "Y" -1 (car elle est augmenté dès le début de la boucle)
    b = 0   #Variable BPB par défaut ("Pas de bateau")
    t = 0   #Variable TPT par défaut ("Pas Touché")
    v = 0   #Variable VPV par défaut ("Pas Vérifié")
    c = 1   #Compteur de lignes
    for c in range (20):
       l = 1  #Compteur de colonne
       y = y+20 #Ligne suivante
       x = 105 #On revient à la 1er colonne
       while l <= 20:
           Case = [(x, y), b, t, v] #Forme de la "CaseListe"
           Grille1.append(Case) #Ajout de la "CaseListe" dans "Grille1"
           x = x+20 #Colonne suivante (pour les coordonnées)
           l = l+1  #Colonne suivante (pour la boucle) 
    
def IniListeCaseGrille2():
    global Grille2
    Grille2 = []
    x = 605 #Première coordonnées possible en "X"
    y = 85  #Première coordonnées possible en "Y" -1 (car elle est augmenté dès le début de la boucle)
    b = 0   #Variable BPB par défaut ("Pas de bateau")
    t = 0  #Variable TPT par défaut ("Pas Touché")
    v = 0   #Variable VPV par défaut ("Pas Vérifié")
    c = 1   #Compteur de lignes
    for c in range (20):
       l = 1  #Compteur de colonne
       y = y+20 #Ligne suivante
       x = 605 #On revient à la 1er colonne
       while l <= 20:
           Case = [(x, y), b, t, v]  #Forme de la "CaseListe"
           Grille2.append(Case) #Ajout de la "CaseListe" dans "Grille2"
           x = x+20 #Colonne suivante (pour les coordonnées)
           l = l+1  #Colonne suivante (pour la boucle)         
#FIN PARTIE FONCTIONS D'INITIALISATION GRILLES

#//////////////////////////////////////////////////////////////////////////////
#PARTIE FONCTION POSITIONNEMENT DES NAVIRES (début de la partie)          
#Fonction Principale "Positionnement du Navire"           
def Grille1_Pos_Navire():
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global CasePlayer1
    global BateauPlayer
    global IndexCase
    global Bat
    global Coord
    global EchecPosition
    #On récupère les dicos utiles
    CasePlayer1 = Dico_Grille1.GrillePlayer1
    BateauPlayer = Dico_Ship.Ship1
    #On demande au joueur le bateau à placer et sa position
    print("Entrez le bateau")
    Bat = raw_input()
    print("Entrez sa case")
    Coord = raw_input()
    #Vérifie que les infos fournies par le joueur se trouvent bien dans les dicos consernés
    if Bat in BateauPlayer and Coord in CasePlayer1: 
        EchecPosition = False
        ListShip_for_Chgmt_State() #Enchaine avec le changement d'état de la variable "Bateau/pas Bateau" en fonction du navire posé   
    else:
        print("Bateau ou Case inexistante \nVeuillez ressaisir")
        EchecPosition = True
        
def IA_Pose_Bat(): #Pose des bateaux par l'IA
    #on globalise toutes les variables
    global batcase
    global IndexCase
    global Grille2
    global EchecPosition
    global case
    EchecPosition = False #On initialise l'echec de position
    x = 0 #Variable pour le déplacement dans la liste listship
    listship = [6,5,4,4,3,3,3,2,2,2] #Nombre de cases des différents bateaux
    NbE = 0 #variable test pour estimer le nombre de placement tenter par l'IA    
    while x < 10 : #Dix fois pour dix bateaux
        batcase = listship[x] #Le nombre de case d'un beateau celon la position dans la liste
        b = random.randint(0,1) #Variable pour le choix Verticale/Horizontal du bateau (0 = vertical, choix arbitraire)
        IndexCase = random.randint(0,398) #Choix d'un index dans la liste des coordonnées Grille2
        print("IA_Pose_Bat")        
        print("batcase: " + str(batcase))
        print("sens bateau (0 = vertical): " + str(b)) 
        print("IndexCase: " + str(IndexCase))
        print("\n")
        if b == 0 : #Choix Verticale du bateau
            case = Grille2[IndexCase] #La case de positionnement du bateau celon l'index choisis 
            Fonction_Verif_PositionIA_Brute_for_V() #Appel fonction vérifiant position bateaux verticaux dans Grille2
            if EchecPosition == False:
                Verif_VariableVPV_in_Grille2_for_V() #Appel fonction qui vérifie que que le navire ne soit ni sur un emplacement déjà pris ni sur une case adjacente à celui-ci
        else : #Choix Horizontal du bateau
            case = Grille2[IndexCase]   
            Fonction_Verif_PositionIA_Brute_for_H() #Appel fonction vérifiant position bateaux horizontaux dans Grille2
            if EchecPosition == False:          
                Verif_VariableVPV_in_Grille2_for_H() #Appel fonction qui vérifie que que le navire ne soit ni sur un emplacement déjà pris ni sur une case adjacente à celui-ci
        if EchecPosition == False : #On ne place le bateau que s'il peut être placé
            if b == 0:
                Grille2_Navire_Verticale()
                #Appelle fonction changement BPB
                Check_IA_Ship() #fonction qui ckeck les cases pour éviter que les bateaux suivant y soient placés
            else:   
                Grille2_Navire_Horizontale()
                #Appelle fonction changement BPB
                Check_IA_Ship() #fonction qui ckeck les cases pour éviter que les bateaux suivant y soient placés                
            x = x + 1 #bateau suivant
        EchecPosition = False #Réinitialisation de l'echec de posistion
        NbE = NbE+1
        print("essaie n°" + str(NbE))
#FIN PARTIE FONCTION POSITIONNEMENT DES NAVIRES (début de la partie)
        
#//////////////////////////////////////////////////////////////////////////////        
#PARTIE FONCTIONS VERIFICATION POSITIONNEMENT JOUEUR
#FonctionS qui vérifie que le navire ne soit pas hors quadrillage ou chevauche
#un autre navire pour éviter les bug dans le "Grille1": 
#C'est la "Position Brute"

#/!\: Note sur les "CaseListe" (Important pour comprendre la gestion des Grilles de jeu par le Programme)
#Une CaseListe est sous la forme ([Coord, BPB, TPT]), avec:
#Coord: Tuple Coordonnées de la Case, fournie par le Dico "PlayerCase1" ou "PlayerCase2" (aussi appelé "GrillePlayer1" ou "GrillePlayer2")
#BPB: Variable "Bateau/Pas Bateau"
#TPT: Variable "Touché/Pas Touché" (présent uniquement pour la Grille1)

#/!\: La variable "EchecPosition" permet de préciser si le bateau est positionnable 
#(s'il a passer tout les test de cette partie des Fonctions)

#Fonction qui recherche l'indice d'une "CaseListe" à partir de ses Coordonnées
def Fonction_Search_Index_CaseListe_for_Grille1():
    #On globalise toutes les variables
    global Grille1
    global IndexCase
    global CasePlayer1
    j = 0 #On démarre à l'index 0 (A1)
    for j in range (len(Grille1)):
        if Grille1[j][0] == CasePlayer1[Coord]: #Grille1[j][0] = Coord de la "CaseListe"
            IndexCase = j #Index de la Case choisi dans la liste "Grille1"
            print("\n")
            print("IndexCase = " + str(IndexCase))
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            #La fin des différentes fonction e sera comme une réaction en chaîne qui fera revenir au programme principal 

#Fonction qui vérifie qu'un bateau n'est pas déjà présent aux emplacements (car un bateau  
#fait plus de 1 case) souhaité par l'intermédiaire de la variable BPB (qui sert à ça)
def Verif_VariableBPB_in_Grille1_for_H():
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global IndexCase
    global EchecPosition  
    i = 1 #On commence à la case 1 du bateau (car il n'a pas de case 0)
    #Boucle qui vérifie que le bateau n'est pas sur un emplacement déjà pris
    print("\n")
    print("Verif_VariableBPB_in_Grille1 (Case/Varibale)")
    while i <= NbCase:
        VariableBPB = Grille1[IndexCase][1] #Grille1[IndexCase][1] = BPB de la "CaseListe"
        print("Case " + str(i))        
        print(IndexCase)
        print(VariableBPB)
        if VariableBPB == 0: #on vérifie l'état de BPB
            if i < NbCase: #On passe à la case suivante s'il y en a une (évite entre autre les bug en T20...)
                i = i+1
                IndexCase = IndexCase+1 #Index suivant
                VariableBPB = Grille1[IndexCase][1] #Variable BPB de case suivante
            else:
                i = i+1
        else:
            print("bateau sur un emplacement déjà pris. \n Veuillez ressaisir")
            EchecPosition = True  
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            #La fin des différentes fonction e sera comme une réaction en chaîne qui fera revenir au programme principal

def Verif_VariableBPB_in_Grille1_for_V():
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global IndexCase
    global EchecPosition  
    i = 1 #On commence à la case 1 du bateau (car il n'a pas de case 0)
    #Boucle qui vérifie que le bateau n'est pas sur un emplacement déjà pris
    print("\n")
    print("Verif_VariableBPB_in_Grille1 (Case/Varibale)")
    while i <= NbCase:
        VariableBPB = Grille1[IndexCase][1] #Grille1[IndexCase][1] = BPB de la "CaseListe"
        print("Case " + str(i))
        print(IndexCase)
        print(VariableBPB)
        if VariableBPB == 0: #on vérifie l'état de BPB
            if i < NbCase: #On passe à la case suivante s'il y en a une (évite entre autre les bug en T20...)
                i = i+1
                IndexCase = IndexCase+20 #Index suivant
                VariableBPB = Grille1[IndexCase][1] #Variable BPB de case suivante
            else:
                i = i+1
        else:
            print("bateau sur un emplacement déjà pris. \n Veuillez ressaisir")
            EchecPosition = True  
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            #La fin des différentes fonction e sera comme une réaction en chaîne qui fera revenir au programme principal
            
#Fonctions Maître de la Partie: Vérifient que le bateau ne soit pas hors case ou sur une case déjà prise
#via l'utilisation de la Fonction "Verif_VariableBPB_in_Grille1"      
def Fonction_Verif_Position_Brute_for_V(): #Spécifique aux navires Verticaux
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global Case
    global IndexCase
    global Bat
    global Coord
    global CasePlayer1
    global EchecPosition
    global j
    i = 1
    #On Recherche d'abord l'index de la "CaseListe" de la case choisi (avec son index on accèdera facilement à la "CaseListe")
    Fonction_Search_Index_CaseListe_for_Grille1()
    #Les Tuple ne pouvant être modifié, on transforme le "Coord" en Liste pour travailler dessus       
    TupleCase = list(CasePlayer1[Coord])
    print("\n")
    print("Fonction_Verif_Position_Brute")
    print(IndexCase) 
    #Boucle qui vérifie que toutes les cases que prendra le bateau existent 
    #Va vérifier que les Colonnes concordent avec les cases existentes (la coordonné la plus basse est 485)      
    while i <= NbCase:
        print(TupleCase)
        if TupleCase[1] <= 485:
            i = i+1
            TupleCase[1] = TupleCase[1]+20 #Coordonnées suivante
        else:
            print("bateau hors quadrillage. \n Veuillez ressaisir")
            EchecPosition = True
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            #La fin des différentes fonction e sera comme une réaction en chaîne qui fera revenir au programme principal
    if EchecPosition == False:
        #Appel de la Fonction de vérifiation de la Variable BPB (dans le cas où ce dernier est bien sur la Grille)
        print("OK for Position Brute")
        Verif_VariableBPB_in_Grille1_for_V()

def Fonction_Verif_Position_Brute_for_H(): #Spécifique aux navires Horizontaux
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global Case
    global IndexCase
    global Bat
    global Coord
    global CasePlayer1
    global EchecPosition
    global j
    i = 1
    #On Recherche d'abord l'index de la "CaseListe" de la case choisi (avec son index on accèdera facilement à la "CaseListe")
    Fonction_Search_Index_CaseListe_for_Grille1()
    #Les Tuple ne pouvant être modifié, on transforme le "Coord" en Liste pour travailler dessus       
    TupleCase = list(CasePlayer1[Coord])
    print("\n")
    print("Fonction_Verif_Position_Brute")
    print(IndexCase)
    #Boucle qui vérifie que toutes les cases que prendra le bateau existent 
    #Va vérifier que les Lignes concordent avec les cases existentes (la coordonné la plus basse est 485)       
    while i <= NbCase:
        print(TupleCase) 
        if TupleCase[0] <= 485:
            i = i+1
            TupleCase[0] = TupleCase[0]+20 #Coordonnées suivante
        else:
            print("bateau hors quadrillage. \n Veuillez ressaisir")
            EchecPosition = True
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            #La fin des différentes fonction e sera comme une réaction en chaîne qui fera revenir au programme principal
    if EchecPosition == False:
        #Appel de la Fonction de vérifiation de la Variable BPB (dans le cas où ce dernier est bien sur la Grille)
        print("OK for Position Brute")
        Verif_VariableBPB_in_Grille1_for_H()        
#FIN PARTIE FONCTIONS VERIFICATION POSITIONNEMENT JOUEUR
        
        
#//////////////////////////////////////////////////////////////////////////////        
#PARTIE FONCTIONS VERIFICATION POSITIONNEMENT IA         
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
    print("Index = " + str(IndexCase)) #Test
    print("deuxieme coordonnee > 485 = mauvais positionnement")
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
    print("Index = " + str(IndexCase)) #Test
    print("premiere coordonnee > 985 = mauvais positionnement")
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


def Verif_VariableVPV_in_Grille2_for_V():
    #On globalise toutes les variables
    global batcase
    global Grille2
    global IndexCase
    global EchecPosition  
    i = 1 #On commence à la case 1 du bateau (car il n'a pas de case 0)
    #Boucle qui vérifie que le bateau n'est pas sur un emplacement déjà pris ou imprenable
    #VPV = varibale "Vérifié/Pas Vérifié" de la case => Pour l'IA correspont au ckeckage de la case après position du navire
    j = IndexCase #J permet de manipuler IndexCase sans le modifier lui même
    print("\n")
    print("Verif_VariableBPB_in_Grille2")
    while i <= batcase:
        VariableVPV = Grille2[j][3] #Grille2[IndexCase][3] = VPV de la "CaseListe"
        print("\n")        
        print("Case " + str(i))        
        print("Index = " +str(j))
        print("valeur VPV = " +str(VariableVPV))
        if VariableVPV == 0: #on vérifie l'état de VPV
            if i < batcase: #On passe à la case suivante s'il y en a une (évite entre autre les bug en T20...)
                i = i+1
                j = j+20 #Index suivant
                VariableVPV = Grille2[j][3] #Variable VPV de case suivante
            else:
                i = i+1
        else:
            EchecPosition = True  
            break                  


def Verif_VariableVPV_in_Grille2_for_H():
    #On globalise toutes les variables
    global batcase
    global Grille2
    global IndexCase
    global EchecPosition  
    i = 1 #On commence à la case 1 du bateau (car il n'a pas de case 0)
    #Boucle qui vérifie que le bateau n'est pas sur un emplacement déjà pris ou imprenable
    #VPV = varibale "Vérifié/Pas Vérifié" de la case => Pour l'IA correspont au ckeckage de la case après position du navire
    j = IndexCase #J permet de manipuler IndexCase sans le modifier lui même    
    print("\n")
    print("Verif_VariableVPV_in_Grille2 (Case/Varibale)")
    while i <= batcase:
        VariableVPV = Grille2[j][3] #Grille2[IndexCase][3] = VPV de la "CaseListe"
        print("\n")        
        print("Case " + str(i))        
        print("Index = " +str(j))
        print("valeur VPV = " +str(VariableVPV))
        if VariableVPV == 0: #on vérifie l'état de BPB
            if i < batcase: #On passe à la case suivante s'il y en a une (évite entre autre les bug en T20...)
                i = i+1
                j = j+1 #Index suivant
                VariableBPB = Grille2[j][3] #Variable VPV de case suivante
            else:
                i = i+1
        else:
            EchecPosition = True  
            break

#FIN PARTIE FONCTIONS VERIFICATION POSITIONNEMENT IA

#//////////////////////////////////////////////////////////////////////////////
#PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB) JOUEUR
#Fonctions qui détecte le Bateau posé et Change l'état de la variable "Bateau/pas Bateau" pour les cases nécessaire  
          
#Fonctions de changement de l'état "Bateau/pas Bateau" des autres cases du Navires
#Sous-Fonction appelées dans la Fonction "ListShip_for_Chgmt_State"    
def Grille1_Navire_Horizontale(): #Spécifique aux navires Horizontaux
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global IndexCaseDef
    i = 2 #On commence à la 2e Case (la première à déjà été faite)
    print("\n")
    print("Grille1_Navire_Horizontale")
    while i <= NbCase:
        #Récupération de la case adjecente à la précédente (vers la droite)
        IndexCaseDef = IndexCaseDef+1                     
        Case2 = Grille1[IndexCaseDef]
        print(IndexCaseDef)
        print(Case2)
        #Modification de l'état "Bateau/pas Bateau" de cette case
        Case2.remove(0)
        Case2.insert(1, 1)
        print(Case2)
        #Case suivante
        i = i+1
        
def Grille1_Navire_Verticale(): #Spécifique aux navires Verticaux
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global IndexCaseDef
    i = 2 #On commence à la 2e Case (la première à déjà été faite)
    print("\n")
    print("Grille1_Navire_Horizontale")
    while i <= NbCase:   
        #Récupération de la case adjecente à la précédente (vers le bas)
        IndexCaseDef = IndexCaseDef+20                     
        Case2 = Grille1[IndexCaseDef]
        print(IndexCaseDef)
        print(Case2)
        #Modification de l'état "Bateau/pas Bateau" de cette case
        Case2.remove(0)
        Case2.insert(1, 1)
        print(Case2)
        #Case suivante
        i = i+1 
  
def Chgmt_State_Case1(): #Fonction qui change l'état de la première case
    global Grille1
    global CasePlayer1
    global IndexCaseDef
    global Bat
    global Coord
    global EchecPosition
    #Récupération de la Case la plus à gauche ou la plus en haut
    IndexCaseDef = Grille1.index([CasePlayer1[Coord], 0, 0, 0])
    Case1 = Grille1[IndexCaseDef]
    print("\n")
    print("Chgmt_State_Case1")
    print(IndexCaseDef)
    print(Case1)
    #Modification de l'état "Bateau/pas Bateau" de cette case
    Case1.remove(0)
    Case1.insert(1, 1)
    print(Case1)

def ListShip_for_Chgmt_State(): 
#Fonction Maître de cette Partie: Gère la modification en fonction du navire choisi
#Utilise les sous-fonction définies au dessus 
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global CasePlayer1
    global BateauPlayer
    global IndexCase
    global Bat
    global Coord
    global EchecPosition
    global Nb2Case
    global Nb3Case
    global Nb4Case
    global Nb5Case
    global Nb6Case
    if Bat == "LitShip" or Bat == "Voilier": #bateau "2 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 2 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bâteau
            Grille1_Navire_Horizontale()
            Nb2Case = Nb2Case+1
        
    elif Bat == "LitShipV" or Bat == "VoilierV": #Bateau "2 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 2 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
            Nb2Case = Nb2Case+1
        
    elif Bat == "SM" or Bat == "MNB" or Bat == "MNR": #Sous-Marin (3 cases) ou autres navire "3 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 3 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
            Nb3Case = Nb3Case+1
        
    elif Bat == "SMV" or Bat == "MNBV" or Bat == "MNRV": #Sous-Marin (3 cases) ou autres navire "3 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 3 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
            Nb3Case = Nb3Case+1
        
    elif Bat == "CuirBase" or Bat == "Cuir2": #Bateau "4 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 4 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
            Nb4Case = Nb4Case+1
        
    elif Bat == "CuirBaseV" or Bat == "Cuir2V": #Bateau "4 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 4 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
            Nb4Case = Nb4Case+1                
        
    elif Bat == "PA": #Bateau "5 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 5 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
            Nb5Case = Nb5Case+1
        
    elif Bat == "PAV": #Bateau "5 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 5 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
            Nb5Case = Nb5Case+1

    elif Bat == "CuirSuper": #Bateau "6 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
            Nb6Case = Nb6Case+1
        
    elif Bat == "CuirSuperV": #Bateau "6 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
            Nb6Case = Nb6Case+1
    print("\n")
    print("Nombre de Navire 2 Cases: " + str(Nb2Case))
    print("Nombre de Navire 3 Cases: " + str(Nb3Case))
    print("Nombre de Navire 4 Cases: " + str(Nb4Case))
    print("Nombre de Navire 5 Cases: " + str(Nb5Case))
    print("Nombre de Navire 6 Cases: " + str(Nb6Case))
#FIN PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB) JOUEUR

#//////////////////////////////////////////////////////////////////////////////
#PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB) IA
def Grille2_Navire_Horizontale(): #Spécifique aux navires Horizontaux
    #On globalise toutes les variables
    global batcase
    global Grille2
    global IndexCase
    global case
    i = 2 #On commence à la 2e Case
    j = IndexCase #J permet de manipuler IndexCase sans le modifier lui même    
    print("\n")
    print("Grille2_Navire_Horizontale")
    print("index: " + str(j))
    case[1] = 1
    print("case après modification" + str(case))
    while i <= batcase:
        #Récupération de la case adjecente à la précédente (vers la droite)
        j = j+1                     
        case = Grille2[j]
        print("case suivante")
        print("index: " + str(j))
        print("case avant modif: " + str(case))        
        #Modification de l'état "Bateau/pas Bateau" de cette case
        case[1] = 1
        print("case " + str(i))
        print("case après modification" + str(case))
        #Case suivante
        i = i+1
        
def Grille2_Navire_Verticale(): #Spécifique aux navires Verticaux
    #On globalise toutes les variables
    global batcase
    global Grille2
    global IndexCase
    global case
    i = 2 #On commence à la 2e Case
    j = IndexCase #J permet de manipuler IndexCase sans le modifier lui même
    print("\n")
    print("Grille1_Navire_Horizontale")
    print("index: " + str(j))
    case[1] = 1
    print("case après modification" + str(case))
    while i <= batcase: 
        #Récupération de la case adjecente à la précédente (vers le bas)
        j = j+20                     
        case = Grille2[j]
        print("case suivante")
        print("index: " + str(j))
        print("case avant modif: " + str(case))
        #Modification de l'état "Bateau/pas Bateau" de cette case
        case[1] = 1
        print("case " + str(i))
        print("case après modification" + str(case))     
        #Case suivante
        i = i+1 
#FIN PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB) IA

#//////////////////////////////////////////////////////////////////////////////    
#PARTIE VERIFICATION FINALE JOUEUR
#Fonction Maître. Cette Fonction fait quatre actions importantes:
# - Elle trouve le premier bateau non vérifié
# - Elle détermine les cases qui existent autour du bateau (dessus, dessous, droite, gauche)
# - Elle vérifie les cases adjacentes à la case choisi et provoque un échec si un bateau se trouve en diagonal de la case, au dessus ou à gauche
#   (lié à la méthode utiliser pour trouver le bateau)
# - Elle détermine le sens du navire grâce à la vérification de la case juste en dessous et juste à droite
#   Si les deux cases possèdent un bateau, un échec se produit car un bateau ne peut pas être verticale et horizontal à la fois
def Verification_Final_Grille1():
    #On globalise les variables
    global Grille1
    global dessus
    global dessous
    global gauche
    global droite
    global TupleCoord
    global Echec
    global j
    j = 0
    TotalShip = 0 #Compte le nombre de bateaux déjà vérifié (par défaut aucun donc "0")
    Echec = False #Variable qui indique si le joueur à mal placé ses navires (False = aucun problème)
    while TotalShip != 10 and Echec == False: #On fait ça pour les dix bateaux
        print("TotalShip: " + str(TotalShip))
        for j in range (len(Grille1)): #On cherche la première case portant un bateau (qui sera alors à l'extrème gauche ou haut)
            if Grille1[j][1] == 1: #Grille1[j][1] = Variable BPB
                #Index = j #Index de la Case choisi dans la liste "Grille1"
                print("\n")
                print("IndexCase = " + str(j))
                if Grille1[j][3] == 0:
                    Grille1[j][3] = 1
                    print("1er case: ")
                    print(Grille1[j])
                    #Variable Bolléenne qui détermine si il existe des cases en dessous/dessus/droite/gauche 
                    #de la case choisi (on part du principe que "oui"), True = la (les) case(s) existe(nt)
                    dessus = True
                    dessous = True
                    droite = True
                    gauche = True
                    #Variable qui détermine le sens du navire (Horizontale/Verticale)
                    H = 0
                    V = 0
                    TupleCoord = list(Grille1[j][0])
                    #détermination des cases existante (quatre test)
                    #Si les test sont "Vrais", alors les cases en question n'existent pas
                    if j-1 < 0: #Y a-t-il une case à gauche ?
                        gauche = False
                    if TupleCoord[0]+20 > 485: #Y a-t-il une case à droite ?
                        droite = False
                    if j+20 > len(Grille1): #Y a-t-il une case en dessous ?
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
                    print("IndexTestgauche: " + str(j-1))
                    print("IndexTestdessous: " + str(j+20))
                    print("\n")
                    #FIN Partie TEST
                    
                    #début vérif variable BPB cases adjacentes
                    #On commence par vérifié que les cases que l'on va testé existent (à l'aide des variable dessus/ dessous/ droite/ gauche)
                    #On commence par les diagonales (qui entraîne un échec si un bateaux s'y trouve)
                    #et on note la présence de navire (s'il y en a) sur les lignes et colonnes
                    Grille1[j][3] = 1 #On concidère la case comme vérifié (même si elle le sera que par la suite)
                    #Travail sur les cases du dessus (si elles existent):
                    if dessus == True: #Cases supérieures
                        print("passage --> case dessus")
                        if droite == True: #Case supérieure droite (diagonale)
                            print("passage --> case dessus droite")
                            if Grille1[j-19][1] == 1: #Cette position entraîne automatiquement la discalification des positions
                                print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                                Echec = True
                                break
                            else:
                                Grille1[j-19][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
                        if gauche == True: #Case  supérieure gauche (diagonale)
                            print("passage --> case gauche")
                            if Grille1[j-21][1] == 1: #Cette position entraîne automatiquement la discalification des positions
                                print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                                Echec = True
                                break
                            else:
                                Grille1[j-21][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
                        if Grille1[j-20][1] == 1: #Case immédiatement au dessus 
                        #(on discalifie en cas de présence d'un bateau car la 1er case chois sera forcément la supérieur gauche)
                            print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                            Echec = True
                            break
                        else:
                            Grille1[j-20][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
                    #Travail sur les cases du dessous (si elles existent):        
                    if dessous == True: 
                        print("passage --> case dessous")
                        if droite == True: #Case inférieure droite (diagonale)
                            print("passage --> case dessous droite")
                            if Grille1[j+21][1] == 1: #Cette position entraîne automatiquement la discalification des positions
                                print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                                Echec = True
                                break
                            else:
                                Grille1[j+21][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
                        if gauche == True: #Case inférieure gauche (diagonale)
                            print("passage --> case dessous gauche")
                            if Grille1[j+19][1] == 1: #Cette position entraîne automatiquement la discalification des positions
                                print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                                Echec = True
                                break
                            else:
                                Grille1[j+19][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
                        if Grille1[j+20][1] == 1: #Case immédiatement au dessous 
                            Grille1[j+20][3] = 1  #On check la Case                          
                            V = V+1 #Si un bateau se trouve ici, c'est que le navire doit être vertical
                        else:
                            Grille1[j+20][3] = 1  #On check la Case
                    #Travail sur la case à gauche (si elle existe):          
                    if gauche == True:
                        print("passage --> case gauche")
                        if Grille1[j-1][1] == 1: #Case immédiatement à gauche 
                        #(on discalifie en cas de présence d'un bateau car la 1er case chois sera forcément la supérieur gauche)
                            print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                            Echec = True
                            break
                        else:
                            Grille1[j-1][3] = 1 #On n'oublie pas de checker la case dans le cas contraire 
                    #Travail sur la case à droite (si elle existe):        
                    if droite == True:
                        print("passage --> case droite")
                        if Grille1[j+1][1] == 1: #Case immédiatement à droite
                            Grille1[j+1][3] = 1  #On check la Case
                            H = H+1 #Si un bateau se trouve ici, c'est que le navire doit être horizontal
                        else:
                            Grille1[j+1][3] = 1  #On check la Case
                            
                    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
                    #Les nombreux test de variables servent à éviter des bugs liés à l'affichage des cases (au cas où elles n'existeraient pas)
                    print("\nFin Passage vérif PI")
                    print("ListeCases (dans l'ordre du dessin)")
                    if dessus == True:
                        if gauche == True:
                            print(Grille1[j-19])
                        print(Grille1[j-20])
                        if droite == True:
                            print(Grille1[j-21])
                    if droite == True:
                        print(Grille1[j-1])
                    if dessous == True:
                        if droite == True:
                            print(Grille1[j+19])
                        print(Grille1[j+20])
                        if gauche == True:
                            print(Grille1[j+21])
                    if gauche == True:
                        print(Grille1[j+1])
                    print("Horizontal = " + str(H))
                    print("Vertical = " +str(V))
                    print("\n")
                    #FIN Partie TEST
                    
                    #Détermination du type de navire (Horizontale/Verticale) à l'aide des variable H/V:
                    if H > 0 and V > 0: #Des lignes et colonnes existe = au moins deux bateaux collés
                        print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                        Echec = True
                        break                    
                    elif H > 0 and V == 0: #Le bateau est-il Horizontal ?
                        #La technique utilisé pourra être réutiliser pour la programme "Coulage des Navires" de l'IA
                        print("Verif_Final_PII_NavireH")                        
                        Verif_Final_PII_NavireH()
                        TotalShip = TotalShip+1
                        break
                    elif H == 0 and V > 0: #Le bateau est-il Verticale ?
                        #La technique utilisé pourra être réutiliser pour la programme "Coulage des Navires" de l'IA
                        print("Verif_Final_PII_NavireV")                        
                        Verif_Final_PII_NavireV()
                        TotalShip = TotalShip+1
                        break
    print("\n")
    print("FIN DU TEST DE VERIFICATION") #Utile à savoir
    print("\n")

#Dans les fonctions suivantes on vérifie la case suivante+1 car la case immédiatement suivante est déjà 
#vérifié et checker (dans la Fonction Maître)
def Verif_Final_PII_NavireH(): #Spécifique aux navires horizontaux
    #on globalise les variables
    global Grille1
    global dessus
    global dessous
    global droite
    global TupleCoord
    global Echec
    global j
    FinBateau = False #Indique si on est au bout du navire (par défaut à "Non", on commence la vérif)
    NbCase = 2 #On commence à la deuxième case
    while FinBateau == False: #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        print("\n")
        print("Case: " + str(NbCase))
        print("Index: " + str(j))
        if NbCase > 6: #Si le nombre de case testé excède 6 c'est qu'on passe sur un nouveau bateau: règles non respectés
            print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
            Echec = True
            break        
        elif TupleCoord[0]+20*NbCase <= 485: #Coordonnées de l'hypothétique case suivante +1 (on vérifie si elle existe)
        
            #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
            print("TupleAbsisse: " + str(TupleCoord[0]+20*NbCase))
            print("Case testé: ")
            print(Grille1[j+2])
            if dessus == True:
                print("case dessus: ")
                print(Grille1[j-18])
            if dessous == True:
                print("case dessous: ")
                print(Grille1[j+22])
            #FIN Partie TEST
            
            #La case suivante appartient t'elle au bateau ?
            if Grille1[j+2][1] == 1: #On vérifie si la case suivante+1 contient un bateau
                Grille1[j+2][3] = 1 #On check la Case
                if dessus == True: #On vérifie que la case au dessus existe...
                    if Grille1[j-18][1] == 1: #... et on regarde si un bateau si trouve
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j-18][3] = 1 #On n'oublie pas de checker la Case 
                if dessous == True:  #On vérifie que la case en dessous existe...
                    if Grille1[j+22][1] == 1: #... et on regarde si un bateau si trouve
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j+22][3] = 1 #On n'oublie pas de checker la Case
            #On refait la même action en prenant en compte que l'on est à la fin du navire dans le cas contraire         
            else:
                Grille1[j+2][3] = 1 #On check la Case
                if dessus == True: #On vérifie que la case au dessus existe...
                    if Grille1[j-18][1] == 1: #... et on regarde si un bateau si trouve (correspond à la diagonale de la dernière case du bateau)
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j-18][3] = 1 #On n'oublie pas de checker la Case
                if dessous == True: #On vérifie que la case en dessous existe...
                    if Grille1[j+22][1] == 1: #... et on regarde si un bateau si trouve (correspond à la diagonale de la dernière case du bateau)
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j+22][3] = 1 #On n'oublie pas de checker la Case
                FinBateau = True #On a tout vérifié et on est à la fin du bateau
                
            #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
            print("\nCase après ckeck")
            print("Case testé: ")
            print(Grille1[j+2])
            if dessus == True:
                print("case dessus: ")
                print(Grille1[j-18])
            if dessous == True:
                print("case dessous: ")
                print(Grille1[j+22])
            #FIN Partie TEST
            
            #Une fois tout les tests terminés...
            NbCase = NbCase+1 #Case suivante
            j = j+1 #Index suivant            
        else: #La case suivante n'existe pas: on est donc forcément à la fin du bateau
            FinBateau = True
    
    
def Verif_Final_PII_NavireV(): #Spécifique aux navires verticaux
    #On globalise les variables
    global Grille1
    global gauche
    global dessous
    global droite
    global TupleCoord
    global Echec
    global j
    FinBateau = False #Indique si on est au bout du navire (par défaut à "Non", on commence la vérif)
    NbCase = 2 #On commence à la deuxième case
    while FinBateau == False: #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        print("\n")
        print("Case: " + str(NbCase))
        print("Index: " + str(j))
        if NbCase > 6: #Si le nombre de case testé excède 6 c'est qu'on passe sur un nouveau bateau: règles non respectés
            print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
            Echec = True
            break        
        elif TupleCoord[1]+20*NbCase <= 485: #Coordonnées de l'hypothétique case suivante +1 (on vérifie si elle existe)
            
            #PARTIE TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
            print("TupleOrdonnee: " + str(TupleCoord[0]+20*NbCase))
            print("Case testé: ")
            print(Grille1[j+40])
            if gauche == True:
                print("case gauche: ")
                print(Grille1[j+39])
            if droite == True:
                print("case droite: ")
                print(Grille1[j+41])
            #FIN PARTIE TEST
            
            #La case suivante appartient t'elle au bateau ?
            if Grille1[j+40][1] == 1:  #On vérifie si la case suivante+1 contient un bateau
                Grille1[j+40][3] = 1 #On check la Case
                if gauche == True: #On vérifie que la case à gauche existe...
                    if Grille1[j+39][1] == 1: #... et on regarde si un bateau si trouve
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j+39][3] = 1 #On n'oublie pas de checker la Case
                if droite == True: #On vérifie que la case à droite existe...
                    if Grille1[j+41][1] == 1: #... et on regarde si un bateau si trouve
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j+41][3] = 1 #On n'oublie pas de checker la Case
                      
            #On refait la même action en prenant en compte que l'on est à la fin du navire dans le cas contraire         
            else:
                Grille1[j+40][3] = 1 #On check la Case
                if gauche == True: #On vérifie que la case à gauche existe...
                    if Grille1[j+39][1] == 1:  #... et on regarde si un bateau si trouve (correspond à la diagonale de la dernière case du bateau)
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j+39][3] = 1 #On n'oublie pas de checker la Case
                if droite == True: #On vérifie que la case à droite existe...
                    if Grille1[j+41][1] == 1: #... et on regarde si un bateau si trouve (correspond à la diagonale de la dernière case du bateau)
                       print("deux de vos navires se touches\nVeuillez recommencer la saisi de vos navires")
                       Echec = True
                       break
                    else:
                      Grille1[j+41][3] = 1 #On n'oublie pas de checker la Case
                FinBateau = True #On a tout vérifié et on est à la fin du bateau
            
            #PARTIE TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
            print("\nCase après ckeck")
            print("Case testé: ")
            print(Grille1[j+40])
            if gauche == True:
                print("case gauche: ")
                print(Grille1[j+39])
            if droite == True:
                print("case droite: ")
                print(Grille1[j+41])
            #FIN PARTIE TEST    
            
            #Une fois tout les tests terminés...
            NbCase = NbCase+1 #Case suivante
            j = j+20 #Index suivant 
            
        else: #La case suivante n'existe pas: on est donc forcément à la fin du bateau
            FinBateau = True

#//////////////////////////////////////////////////////////////////////////////
#Cette Fonction ne vérifie pas les placements. Elle est appelé par la Fonction "REINITIALISATION_PARTIE"
#se trouvant dans le Main_Programme", son utilité est de réinitialisé les Compteurs de Navires aisément
#sans avoir besoins de les importer (évite entre autres les bug lié à une non-définition des vriables
#dans le "Main_Programme")                    
def Reinitialisation_NbXCase(): 
    global Nb2Case
    global Nb3Case
    global Nb4Case
    global Nb5Case
    global Nb6Case
    Nb2Case = 0
    Nb3Case = 0
    Nb4Case = 0
    Nb5Case = 0
    Nb6Case = 0
#FIN PARTIE VERIFICATION FINALE
    
    
#////////////////////////////////////////////////////////////////////////////// 
#PARTIE CHECK CASE IA    
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
    j = IndexCase #J permet de manipuler IndexCase sans le modifier lui même
    print("\n")
    print("IndexCase = " + str(j))
    Grille2[j][3] = 1
    print("1er case: ")
    print(Grille2[j])
    #Variable Bolléenne qui détermine si il existe des cases en dessous/dessus/droite/gauche 
    #de la case choisi (on part du principe que "oui"), True = la (les) case(s) existe(nt)
    dessus = True
    dessous = True
    droite = True
    gauche = True
    #Variable qui détermine le sens du navire (Horizontale/Verticale)
    H = 0
    V = 0
    TupleCoord = list(Grille2[j][0])
    #détermination des cases existante (quatre test)
    #Si les test sont "Vrais", alors les cases en question n'existent pas
    if TupleCoord[0]-20 < 605: #Y a-t-il une case à gauche ?
        gauche = False
    if TupleCoord[0]+20 > 985: #Y a-t-il une case à droite ?
        droite = False
    if TupleCoord[1]+20 > 485: #Y a-t-il une case en dessous ?
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
    print("IndexTestgauche: " + str(j-1))
    print("IndexTestdessous: " + str(j+20))
    print("\n")
    #FIN Partie TEST
                    
    #Travail sur les cases du dessus (si elles existent):
    if dessus == True: #Cases supérieures
        print("passage --> case dessus")
        Grille2[j-20][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if droite == True: #Case supérieure droite (diagonale)
            print("passage --> case dessus droite")
            Grille2[j-19][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if gauche == True: #Case  supérieure gauche (diagonale)
            print("passage --> case gauche")
            Grille2[j-21][3] = 1 #On n'oublie pas de checker la case dans le cas contraire  
        
    #Travail sur les cases du dessous (si elles existent):        
    if dessous == True: 
        print("passage --> case dessous")
        if droite == True: #Case inférieure droite (diagonale)
            print("passage --> case dessous droite")
            Grille2[j+21][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if gauche == True: #Case inférieure gauche (diagonale)
            print("passage --> case dessous gauche")
            Grille2[j+19][3] = 1 #On n'oublie pas de checker la case dans le cas contraire
        if Grille2[j+20][1] == 1: #Case immédiatement au dessous 
            Grille2[j+20][3] = 1  #On check la Case                          
            V = V+1 #Si un bateau se trouve ici, c'est que le navire doit être vertical
        else:
            Grille2[j+20][3] = 1  #On check la Case
            
    #Travail sur la case à gauche (si elle existe):          
    if gauche == True:
        print("passage --> case gauche")
        Grille2[j-1][3] = 1 #On n'oublie pas de checker la case dans le cas contraire 
    #Travail sur la case à droite (si elle existe):        
    if droite == True:
        print("passage --> case droite")
        if Grille2[j+1][1] == 1: #Case immédiatement à droite
            Grille2[j+1][3] = 1  #On check la Case
            H = H+1 #Si un bateau se trouve ici, c'est que le navire doit être horizontal
        else:
            Grille2[j+1][3] = 1  #On check la Case
                        
    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
    #Les nombreux test de variables servent à éviter des bugs liés à l'affichage des cases (au cas où elles n'existeraient pas)
    print("\nFin Passage check PI")
    print("ListeCases (dans l'ordre du dessin)")
    if dessus == True:
        if gauche == True:
            print(Grille2[j-19])
        print(Grille2[j-20])
        if droite == True:
            print(Grille2[j-21])
    if droite == True:
        print(Grille2[j-1])
    if dessous == True:
        if droite == True:
            print(Grille2[j+19])
        print(Grille2[IndexCase+20])
        if gauche == True:
            print(Grille2[j+21])
    if gauche == True:
        print(Grille2[j+1])
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
    global IndexCase
    j = IndexCase #J permet de manipuler IndexCase sans le modifier lui même
    NbCase = 2 #On commence à la deuxième case
    for NbCase in range (batcase-1): #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        j = j+1
        print("\n")
        print("Case: " + str(NbCase))
        print("Index: " + str(j)) 

        #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
        print("TupleAbsisse: " + str(TupleCoord[0]+20*NbCase))
        print("Case testé: ")
        print(Grille2[j])
        if dessus == True:
            print("case dessus: ")
            print(Grille2[j-20])
        if dessous == True:
            print("case dessous: ")
            print(Grille2[j+20])
        #FIN Partie TEST
            
        #La case suivante appartient t'elle au bateau ?
        Grille2[j][3] = 1 #On check la Case
        if dessus == True: #On vérifie que la case au dessus existe...
            Grille2[j-20][3] = 1 #On n'oublie pas de checker la Case 
        if dessous == True:  #On vérifie que la case en dessous existe...
            Grille2[j+20][3] = 1 #On n'oublie pas de checker la Case
    #Partie qui se fait une fois toutes les cases du navires ckeckées (on va sur les celles juste après)
    TestCoord = list(Grille2[j][0])
    if TestCoord[0] <= 985: #Y a-t-il une case deux cases à droite ?
        j = j+1        
        Grille2[j][3] = 1 #On check la Case
        if dessus == True: #On vérifie que la case au dessus existe...
            Grille2[j-20][3] = 1 #On n'oublie pas de checker la Case 
        if dessous == True:  #On vérifie que la case en dessous existe...
            Grille2[j+20][3] = 1 #On n'oublie pas de checker la Case
                
    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
    print("\nCase après ckeck")
    print("Case testé: ")
    print(Grille2[j])
    if dessus == True:
        print("case dessus: ")
        print(Grille2[j-20])
    if dessous == True:
        print("case dessous: ")
        print(Grille2[j+20])
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
    global IndexCase
    j = IndexCase #J permet de manipuler IndexCase sans le modifier lui même
    NbCase = 2 #On commence à la deuxième case
    for NbCase in range (batcase-1): #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        j = j+20        
        print("\n")
        print("Case: " + str(NbCase))
        print("Index: " + str(j)) 

        #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
        print("TupleOrdonnee: " + str(TupleCoord[1]+20*NbCase))
        print("Case testé: ")
        print(Grille2[j])
        if gauche == True:
            print("case dessus: ")
            print(Grille2[j-1])
        if droite == True:
            print("case dessous: ")
            print(Grille2[j+1])
        #FIN Partie TEST
        
        Grille2[j][3] = 1 #On check la Case
        if gauche == True: #On vérifie que la case au dessus existe...
            Grille2[j-1][3] = 1 #On n'oublie pas de checker la Case 
        if droite == True:  #On vérifie que la case en dessous existe...
            Grille2[j+1][3] = 1 #On n'oublie pas de checker la Case
    #Partie qui se fait une fois toutes les cases du navires ckeckées (on va sur les celles juste après)
    if j+20 < len(Grille2): #Y a-t-il une case deux cases en dessous ?
        j = j+20
        Grille2[j][3] = 1 #On check la Case
        if gauche == True: #On vérifie que la case au dessus existe...
            Grille2[j-1][3] = 1 #On n'oublie pas de checker la Case 
        if droite == True:  #On vérifie que la case en dessous existe...
            Grille2[j+1][3] = 1 #On n'oublie pas de checker la Case
                
    #Partie TEST (la suppression de la partie devra se faire une fois celle-ci inutile)
    print("\nCase après ckeck")
    print("Case testé: ")
    print(Grille2[j])
    if gauche == True:
        print("case dessus: ")
        print(Grille2[j-1])
    if droite == True:
        print("case dessous: ")
        print(Grille2[j+1])
    #FIN Partie TEST
#FIN PARTIE CHECK CASE IA
#FIN PROGRAMME "FONCTION_SHIP"          