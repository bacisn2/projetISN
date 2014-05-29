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
Ship1 = {"LitShip":pygame.image.load("Petit-Navire.png").convert_alpha(), "LitShipV":pygame.image.load("Petit-Navire V.png").convert_alpha(),"SMV":pygame.image.load("sous-marin 1 V.png").convert_alpha(), "SM":pygame.image.load("sous-marin 1.png").convert_alpha(), "CuirBase":pygame.image.load("Cuirasse-Base.png").convert_alpha(), "CuirBaseV":pygame.image.load("Cuirasse-Base V.png").convert_alpha(), "CuirSuper":pygame.image.load("Super Cuirasse 1.png").convert_alpha(), "CuirSuperV":pygame.image.load("Super Cuirasse 1 V.png").convert_alpha(), "Cuir2":pygame.image.load("Cuirasse 2.png").convert_alpha(), "Cuir2V":pygame.image.load("Cuirasse 2 V.png").convert_alpha(), "PA":pygame.image.load("Porte Avion 1.png").convert_alpha(), "PAV":pygame.image.load("Porte Avion 1 V.png").convert_alpha(), "Voilier":pygame.image.load("Voilier.png").convert_alpha(), "VoilierV":pygame.image.load("Voilier V.png").convert_alpha(), "MNB":pygame.image.load("bateau 28B.jpg").convert_alpha(), "MNR":pygame.image.load("bateau 28R.jpg").convert_alpha(), "MNBV":pygame.image.load("bateau 28B V.jpg").convert_alpha(), "MNRV":pygame.image.load("bateau 28R V.jpg").convert_alpha(), "Special":pygame.image.load("Navire 23.png").convert_alpha(), "PA2":pygame.image.load("Porte Avion 2.png").convert_alpha(), "PA2V":pygame.image.load("Porte Avion 2 V.png").convert_alpha(), "SuperCuir":pygame.image.load("Super Cuirasse 2.png").convert_alpha(), "SuperCuirV":pygame.image.load("Super Cuirasse 2 V.png").convert_alpha(), "Destroyer":pygame.image.load("Destroyer.png").convert_alpha(), "DestroyerV":pygame.image.load("Destroyer V.png").convert_alpha(), "Yacht":pygame.image.load("Yacht_1.png").convert_alpha(), "YachtV":pygame.image.load("Yacht_1V.png").convert_alpha(), "Yacht2":pygame.image.load("Yacht_2.png").convert_alpha(), "Yacht2V":pygame.image.load("Yacht_2V.png").convert_alpha()}

#Dico Liste Bateaux (for IA)
