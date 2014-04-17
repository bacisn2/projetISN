# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:47:41 2014

@author: IG 158
"""

# Liste des fonctions utile pour le programme de recherche de navire de l'IA

import Fonction_Ship
from random import *
from Fonction_Ship import Grille1
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
#obligé d'initialiser une fenêtre pour faire fonctionner le pygame.image.load
#fenetre = pygame.display.set_mode((1200, 900)) 

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
    Choice = 0
        
def Search_Ship(fenetre, CasePlayer1):
    global CaseIA
    global A_Z
    global Z_A
    global Random
    global Choice
    Tour = False
    while Tour == False:
        if A_Z == True:
            Cible = CaseIA[Choice]
            print("cible = " + str(Cible))
            if Cible[2] == 0:
                Cible[2] = 1
                #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                if Cible[1] == 0:
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseIA[x][0])  #Placement rond
                else:
                    print("touche")
                    fenetre.blit(CroixRouge, CaseIA[x][0]) #Placement croix
                    #appelle fonction attaque
        elif Z_A == True:
            Cible = CaseIA[(-Choice)-1]
            print("cible = " + str(Cible))
            if Cible[2] == 0:
                Cible[2] = 1
                #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                if Cible[1] == 0:
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseIA[x][0])  #Placement rond
                else:
                    print("touche")
                    fenetre.blit(CroixRouge, CaseIA[x][0]) #Placement croix
                    #appelle fonction attaque
        elif Random == True:
            Cible = CaseIA[randint(0,len(CaseIA))]
            print("cible = " + str(Cible))
            if Cible[2] == 0:
                Cible[2] = 1
                #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                if Cible[1] == 0:
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseIA[x][0])  #Placement rond
                else:
                    print("touche")
                    fenetre.blit(CroixRouge, CaseIA[x][0]) #Placement croix
                    #appelle fonction attaque        
    Choice = Choice+1












    