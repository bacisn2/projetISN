# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:37:59 2014

@author: IG 158
"""

import pygame
from pygame.locals import *
import Dico_Grille1
import Dico_Ship
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 30) #Transparent pour l'affichage des Textes (version 30 px)
SuperFont = pygame.font.Font(None, 80) #Transparent pour l'affichage des Textes (version 80 px)

#Ini Fenêtre + Fond Blanc
fenetre = pygame.display.set_mode((1200, 900))
fond = pygame.image.load("Fond_Blanc_1200-900.jpg")
fenetre.blit(fond, (0,0))
pygame.display.flip()

#Ini Quadriallage (sans marquage)
Quad1 = pygame.image.load("The Quadrillage 2.jpg")
fenetre.blit(Quad1, (100,100))
fenetre.blit(Quad1, (600,100))
pygame.display.flip()

#Ini marquage Quadrillage
Ligne = pygame.image.load("Ligne_Tableau.jpg")
Colonne = pygame.image.load("Colonne_Tableau.jpg")
fenetre.blit(Ligne, (80,100))
fenetre.blit(Ligne, (580,100))
fenetre.blit(Colonne, (100,75))
fenetre.blit(Colonne, (600,75))
pygame.display.flip()

#OpenDicoCP = open('CasePlayer.txt', 'r')
#OpenDicoBP = open('BateauPlayer.txt', 'r')
#ReadDicoCP = OpenDicoCP.read()
#ReadDicoBP = OpenDicoBP.read()
CasePlayer1 = Dico_Grille1.GrillePlayer1
BateauPlayer = Dico_Ship.Ship1
Infinie = 1 #Fait tourner indéfiniment le programme
CountShip = 0

#Liste des commandes pour le début
TextD1 = "Appuyez sur 2, 3, 4, 5 pour placez un bateau predefini. Appuyez sur \"haut\" pour reinitialiser le plateau"
TextD2 = "Appuyez sur \"b\" pour placez un bateau (que vous choisirez) sur une case (que vous choisirez)"
TextD3 = "Appuyez sur \"haut\" pour supprimer ce message"
Instr1 = font.render(TextD1, 1, (0,0,0))
Instr2 = font.render(TextD2, 1, (0,0,0))
Instr3 = font.render(TextD3, 1, (0,0,0))
fenetre.blit(Instr1, (100,300))
fenetre.blit(Instr2, (100,335))
fenetre.blit(Instr3, (100,370))
pygame.display.flip()
          
while Infinie == 1:
    for event in pygame.event.get(): #Fait la liste des évènements possible (appuyer sur une touche, souris, etc...)
        if event.type == QUIT: #Quitte la partie quand on appuie sur "Quitter"
            Infinie = 0
            break
        if event.type == KEYDOWN and event.key == K_SPACE: #Test Espace
            Obj = "Espace"
            Esp = font.render(Obj, 1, (0,0,0))
            fenetre.blit(Esp, (200,500))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_ESCAPE: #Message Mystère
            Obj2 = "N'essayez pas de vous echapper..."
            Obj3 = "Vous etes prisonnier !!"
            Esp2 = font.render(Obj2, 1, (255,0,0))
            Esp3 = font.render(Obj3, 1, (255,0,0))
            fenetre.blit(Esp2, (800,500))
            fenetre.blit(Esp3, (800,525))
            pygame.display.flip()            
        if event.type == KEYDOWN and event.key == K_KP5: #Placement bateau 5 cases (K6)
            CountShip = CountShip + 1            
            Bat = pygame.image.load("bateau 23.jpg").convert_alpha()
            fenetre.blit(Bat, (205,305))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_KP2: #Placement bateau 2 cases (T19)
            CountShip = CountShip + 1            
            Bat = pygame.image.load("bateau 10.jpg").convert_alpha()
            fenetre.blit(Bat, (465,485))
            pygame.display.flip()            
        if event.type == KEYDOWN and event.key == K_KP4: #Placement du bateau 4 cases (A1)
            CountShip = CountShip + 1            
            Bat = pygame.image.load("bateau 22.jpg").convert_alpha()
            fenetre.blit(Bat, (105,105))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_KP3: #Placement du bateau 3 cases (J15)
            CountShip = CountShip + 1
            Bat = pygame.image.load("sous-marin 1 V.jpg").convert_alpha()
            fenetre.blit(Bat, (385,285))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_b:
            print("Entrez le bateau")
            Bat = raw_input()
            print("Entrez sa case")
            Coord = raw_input()
            if CountShip < 6:
                if Bat in BateauPlayer and Coord in CasePlayer1:
                    CountShip = CountShip + 1
                    NewBat = BateauPlayer[Bat]
                    fenetre.blit(NewBat, CasePlayer1[Coord])
                    pygame.display.flip()
                else:
                    print("Bateau ou Case inexistante \nVeuillez ressaisir après avoir appuyez sur \"b\"")  
            else:
                print("Nombre de navire max atteint")
        if event.type == KEYDOWN and event.key == K_UP: #réinitialisation du plateau
            CountShip = 0           
            fenetre.blit(fond, (0,0))
            fenetre.blit(Quad1, (100,100))
            fenetre.blit(Quad1, (600,100))
            fenetre.blit(Ligne, (80,100))
            fenetre.blit(Ligne, (580,100))
            fenetre.blit(Colonne, (100,75))
            fenetre.blit(Colonne, (600,75))
            pygame.display.flip()
