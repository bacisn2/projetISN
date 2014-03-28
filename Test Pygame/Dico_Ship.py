# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 14:23:50 2014

@author: IG 158
"""

#Initialisation de Pygame (pour le pygame.image.load)
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
#obligé d'initialiser une fenêtre pour faire fonctionner le pygame.image.load
fenetre = pygame.display.set_mode((1200, 900)) 

#Dico Liste Bateaux (for Player 1)
Ship1 = {"LitShip":pygame.image.load("bateau 10.jpg").convert_alpha(), "LitShipV":pygame.image.load("bateau 10 V.jpg").convert_alpha(),"SMV":pygame.image.load("sous-marin 1 V.jpg").convert_alpha(), "SM":pygame.image.load("sous-marin 1.jpg").convert_alpha(), "CuirBase":pygame.image.load("bateau 22.jpg").convert_alpha(), "CuirBaseV":pygame.image.load("bateau 22 V.jpg").convert_alpha(), "CuirSuper":pygame.image.load("bateau 25.jpg").convert_alpha(), "CuirSuperV":pygame.image.load("bateau 25 V.jpg").convert_alpha(), "Cuir2":pygame.image.load("bateau 26.jpg").convert_alpha(), "Cuir2V":pygame.image.load("bateau 26 V.jpg").convert_alpha(), "PA":pygame.image.load("bateau 23.jpg").convert_alpha(), "PAV":pygame.image.load("bateau 23 V.jpg").convert_alpha(), "Voilier":pygame.image.load("bateau 27.jpg").convert_alpha(), "VoilierV":pygame.image.load("bateau 27 V.jpg").convert_alpha(), "MNB":pygame.image.load("bateau 28B.jpg"), "MNR":pygame.image.load("bateau 28R.jpg"), "MNBV":pygame.image.load("bateau 28B V.jpg"), "MNRV":pygame.image.load("bateau 28R V.jpg")}

#Dico Liste Bateaux (for IA)
