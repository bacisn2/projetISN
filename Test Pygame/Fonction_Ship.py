# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 17:21:26 2014

@author: IG 158
"""

#Listes des Fonctions utile pour le jeu (seront importer dans la partie "IMPORTATION" du programme principal)
#IMPORTATION DES DICOS
import Dico_Ship
import Dico_Grille1

#PARTIE FONCTIONS D'INITIALISATION
#Fonctions d'Initialisation des Grilles
def IniListeCaseGrille1():
    global Grille1
    Grille1 = []
    x = 105 #Première coordonnées possible en "X"
    y = 85  #Première coordonnées possible en "Y" -1 (car elle est augmenté dès le début de la boucle)
    b = 0   #Variable BPB par défaut ("Pas de bateau")
    t = 0   #Variable TPT par défaut ("Pas Touché")
    c = 1   #Compteur de lignes
    for c in range (20):
       l = 1  #Compteur de colonne
       y = y+20 #Ligne suivante
       x = 105 #On revient à la 1er colonne
       while l <= 20:
           Case = [(x, y), b, t] #Forme de la "CaseListe"
           Grille1.append(Case) #Ajout de la "CaseListe" dans "Grille1"
           x = x+20 #Colonne suivante (pour les coordonnées)
           l = l+1  #Colonne suivante (pour la boucle) 
    
def IniListeCaseGrille2():
    global Grille2
    Grille2 = []
    x = 605 #Première coordonnées possible en "X"
    y = 85  #Première coordonnées possible en "Y" -1 (car elle est augmenté dès le début de la boucle)
    b = 0   #Variable BPB par défaut ("Pas de bateau")
    #t = 0  #Variable TPT par défaut ("Pas Touché")
    c = 1   #Compteur de lignes
    for c in range (20):
       l = 1  #Compteur de colonne
       y = y+20 #Ligne suivante
       x = 605 #On revient à la 1er colonne
       while l <= 20:
           Case = [(x, y), b]  #Forme de la "CaseListe"
           Grille2.append(Case) #Ajout de la "CaseListe" dans "Grille2"
           x = x+20 #Colonne suivante (pour les coordonnées)
           l = l+1  #Colonne suivante (pour la boucle)         
#FIN PARTIE FONCTIONS D'INITIALISATION

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
#FIN PARTIE FONCTION POSITIONNEMENT DES NAVIRES (début de la partie)
        
        
#PARTIE FONCTIONS VERIFICATION POSITIONNEMENT
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

#/!\: CETTE FONCTION EST PROVISOIREMENT DESACTIVE POUR FLUIDIFIER LE PROGRAMME
#def Fonction_Search_Index_CaseListe_for_Grille2():
#    global Grille1
#    global IndexCase
#    global CasePlayer1
#    j = 0 #On démarre à l'index 0 (A1)
#    for j in range (len(Grille1)):
#        if Grille2[j][0] == CasePlayer1[Coord]: #Grille1[j][0] = Coord de la "CaseListe"
#            IndexCase = j #Index de la Case choisi dans la liste "Grille2"
#            break   

#Fonction qui vérifie qu'un bateau n'est pas déjà présent aux emplacements (car un bateau  
#fait plus de 1 case) souhaité par l'intermédiaire de la variable BPB (qui sert à ça)
def Verif_VariableBPB_in_Grille1_for_H():
    #On globalise toutes les variables
    global NbCase
    global Grille1
    global IndexCase
    global EchecPosition  
    i = 1 #On commence à la case 1 du bateau (car il n'a pas de case 0)
    VariableBPB = Grille1[IndexCase][1] #Grille1[IndexCase][1] = Coord de la "CaseListe"
    #Boucle qui vérifie que le bateau n'est pas sur un emplacement déjà pris
    print("\n")
    print("Verif_VariableBPB_in_Grille1 (Case/Varibale)")
    while i <= NbCase:
        print(IndexCase)
        print(VariableBPB)
        print("case suivante")
        if VariableBPB == 0:
            i = i+1
            IndexCase = IndexCase+1 #Index suivant
            VariableBPB = Grille1[IndexCase][1] #Variable BPB de case suivante
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
    VariableBPB = Grille1[IndexCase][1] #Grille1[IndexCase][1] = Coord de la "CaseListe"
    #Boucle qui vérifie que le bateau n'est pas sur un emplacement déjà pris
    print("\n")
    print("Verif_VariableBPB_in_Grille1 (Case/Varibale)")
    while i <= NbCase:
        print(IndexCase)
        print(VariableBPB)
        print("case suivante")
        if VariableBPB == 0:
            i = i+1
            IndexCase = IndexCase+20 #Index suivant
            VariableBPB = Grille1[IndexCase][1] #Variable BPB de case suivante
        else:
            print("bateau sur un emplacement déjà pris. \n Veuillez ressaisir")
            EchecPosition = True  
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            #La fin des différentes fonction e sera comme une réaction en chaîne qui fera revenir au programme principal
            
#/!\: CETTE FONCTION EST PROVISOIREMENT DESACTIVE POUR FLUIDIFIER LE PROGRAMME 
#def Verif_VariableBPB_in_Grille2():
#    global NbCase
#    global Grille2
#    global IndexCase
#    global EchecPosition
#    i = 1
#    VariableBPB = Grille2[IndexCase][1]
#    while i <= NbCase:
#        if VariableBPB == 0:
#            i = i+1
#            IndexCase = IndexCase+20
#        else:
#            print("bateau sur un emplacement déjà pris. \n Veuillez ressaisir")
#            EchecPosition = True  
#            break

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
#FIN PARTIE FONCTIONS VERIFICATION POSITIONNEMENT
        
        

#PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB)
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
    IndexCaseDef = Grille1.index([CasePlayer1[Coord], 0, 0])
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
    if Bat == "LitShip" or Bat == "Voiler": #bateau "2 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 2 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bâteau
            Grille1_Navire_Horizontale() 
        
    elif Bat == "LitShipV" or Bat == "VoilerV": #Bateau "2 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 2 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
        
    elif Bat == "SM" or Bat == "MNB" or Bat == "MNR": #Sous-Marin (3 cases) ou autres navire "3 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 3 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
        
    elif Bat == "SMV" or Bat == "MNBV" or Bat == "MNRV": #Sous-Marin (3 cases) ou autres navire "3 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 3 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()
        
    elif Bat == "CuirBase" or Bat == "Cuir2": #Bateau "4 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 4 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
        
    elif Bat == "CuirBaseV" or Bat == "Cuir2V": #Bateau "4 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 4 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()                
        
    elif Bat == "PA": #Bateau "5 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 5 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
        
    elif Bat == "PAV": #Bateau "5 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 5 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale() 

    elif Bat == "CuirSuper": #Bateau "6 cases" horizontale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_H()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Horizontale()
        
    elif Bat == "CuirSuperV": #Bateau "6 cases" verticale
        #Prologue: Appelle de la Fonction vérif quadrillage & autres navires
        NbCase = 6 #Nombre de case du navire (sert pour les fonctions suivantes)
        Fonction_Verif_Position_Brute_for_V()
        if EchecPosition == False: #Ne place le bateau que s'il est "Posissionnable"
            #Appelle la Fonction qui change l'état de la 1er Case
            Chgmt_State_Case1()
            #Appelle la fonction qui gérera la modifiaction de l'état des autres cases du bateau 
            Grille1_Navire_Verticale()  
#FIN PARTIE CHANGEMENT DE L'ETAT DE LA VARIABLE "BATEAU/PAS BATEAU" (BPB)             
#FIN PARTIE FONCTION POSITIONNEMENT DES NAVIRES 