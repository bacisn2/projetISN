# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:37:59 2014

@author: IG 158
"""

import pygame
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((800, 500))
fond = pygame.image.load("Fond_Blanc.png")
fenetre.blit(fond, (0,0))
pygame.display.flip()

Quad1 = pygame.image.load("quadrillage 3.png")
fenetre.blit(Quad1, (50,50))
pygame.display.flip()

Quad2 = pygame.image.load("quadrillage 3.png")
fenetre.blit(Quad2, (450,50))
pygame.display.flip()

Infinie = 1

while Infinie == 1:
    Infinie

