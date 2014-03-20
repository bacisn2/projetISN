# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:37:59 2014

@author: IG 158
"""

import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 30) #Transparent pour l'afiichage des Textes (version 30 px)
SuperFont = pygame.font.Font(None, 80) #Transparent pour l'afiichage des Textes (version 80 px)

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

Infinie = 1 #Fait tourner indéfiniment le programme

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
            Bat = pygame.image.load("bateau 23.jpg").convert_alpha()
            fenetre.blit(Bat, (205,305))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_KP2: #Placement bateau 2 cases (T19)
            Bat = pygame.image.load("bateau 10.jpg").convert_alpha()
            fenetre.blit(Bat, (465,485))
            pygame.display.flip()            
        if event.type == KEYDOWN and event.key == K_KP4: #Placement du bateau 4 cases (A1)
            Bat = pygame.image.load("bateau 22.jpg").convert_alpha()
            fenetre.blit(Bat, (105,105))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_KP3: #Placement du bateau 3 cases (J15)
            Bat = pygame.image.load("Bateau 4 (sous-marin 1) V.jpg").convert_alpha()
            fenetre.blit(Bat, (385,285))
            pygame.display.flip()            
        if event.type == KEYDOWN and event.key == K_UP: #réinitialisation du plateau
            fenetre.blit(fond, (0,0))
            fenetre.blit(Quad1, (100,100))
            fenetre.blit(Quad1, (600,100))
            fenetre.blit(Ligne, (80,100))
            fenetre.blit(Ligne, (580,100))
            fenetre.blit(Colonne, (100,75))
            fenetre.blit(Colonne, (600,75))
            pygame.display.flip()
