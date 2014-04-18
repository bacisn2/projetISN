# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:47:41 2014

@author: IG 158
"""

# Liste des fonctions utile pour le programme de recherche de navire de l'IA

#import Fonction_Ship
from random import *
from Fonction_Ship import Grille1
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

def Define_List_Case_and_Strategie():
    global Grille1
    global CaseIA
    global Choice
    global A_Z
    global Z_A
    global Random
    #variable locale utile
    x = 0
    #Variable Stratégie IA
    A_Z = False
    Z_A = False
    Random = False
    #Liste des cases que l'IA choisira)
    CaseIA = []
    #Les boucles permettent d'ajouter les bonnes cases dans la liste "CaseIA", 
    #une case sur deux n'est pas exactement la bonne définition
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
    for x in range(100, 20):
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
    #Détermination de la stratégie
    x = randint(1,3) #stratégie aléatoire
    print("choix strategie = " + str(x))
    if x == 1: #choix: du début vers la fin
        A_Z = True
        print("Strategie A a Z")
    elif x == 2: #choix: de la fin vers le début
        Z_A = True
        print("Strategie Z a A")
    else: #choix: aléatoire, sans procédé propre
        Random = True
        print("Strategie Case Aleatoire")
    Choice = 0 #Initialisation "choix de la case"
        
def Search_Ship(fenetre, CasePlayer1, RondBleu, CroixRouge, TextEAU, TextTOUCHE, TextCOULE, A_Z, Z_A, Random): #On utilise certaines variables du Main
    global CaseIA
    #global A_Z
    #global Z_A
    #global Random
    global Choice
    Tour = False #Ini du Tour
    while Tour == False: #Le tour est-il terminé ?
        if A_Z == True: #Si Stratégie "Début vers Fin"
            #Détermination de la case
            IndexCible = Choice 
            Cible = CaseIA[IndexCible]
            print("cible = " + str(Cible))
            #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
            if Cible[2] == 0:
                Cible[2] = 1 #La case est maintenant touché
                #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                #Il y a-t-il un bateau sur la case touché ?
                if Cible[1] == 0: 
                    #On affiche dans l'eau et on place un carrée bleu
                    print("dans l'eau") 
                    fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                    fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                else:
                    #On affiche touché et on place un carrée rouge
                    print("touche")
                    fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                    fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                    #appelle fonction attaque
                Tour = True #Fin du Tour de l'IA
        elif Z_A == True: #Si Stratégie "Fin vers Début"
            #Détermination de la case
            IndexCible = (-Choice)-1 # ==> Depuis la fin, ex: si Choice = 1, IndexCase = (-1)-1 = -2 (avant dernière case)
            Cible = CaseIA[IndexCible]
            print("cible = " + str(Cible))
            #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
            if Cible[2] == 0:
                Cible[2] = 1 #La case est maintenant touché
                #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                #Il y a-t-il un bateau sur la case touché ?
                if Cible[1] == 0:
                    #On affiche dans l'eau et on place un carrée bleu
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                    fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                else:
                    #On affiche touché et on place un carrée rouge
                    print("touche")
                    fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                    fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                    #appelle fonction attaque
                Tour = True #Fin du Tour de l'IA
        elif Random == True: #Si Stratégie "Case Aléatoire"
            #Détermination de la case
            IndexCible = randint(0,len(CaseIA)) #==> Une case au hasard dans la liste
            Cible = CaseIA[IndexCible]
            print("cible = " + str(Cible))
            #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
            if Cible[2] == 0:
                Cible[2] = 1 #La case est maintenant touché
                #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                #Il y a-t-il un bateau sur la case touché ?
                if Cible[1] == 0:
                    #On affiche dans l'eau et on place un carrée bleu
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                    fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                else:
                    #On affiche touché et on place un carrée rouge
                    print("touche")
                    fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                    fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                    #appelle fonction attaque      
                Tour = True #Fin du Tour de l'IA
        Choice = Choice+1 #On passe à la case suivante (en cas de succès ou échec)