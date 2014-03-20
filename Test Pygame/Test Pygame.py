# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:37:59 2014

@author: IG 158
"""

import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 30)
SuperFont = pygame.font.Font(None, 80)

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
    for event in pygame.event.get():
        if event.type == QUIT:
            Infinie = 0
    if event.type == KEYDOWN and event.key == K_SPACE:
        Obj = "Espace"
        Esp = font.render(Obj, 1, (0,0,0))
        fenetre.blit(Esp, (100,400))
        pygame.display.flip()
    if event.type == KEYDOWN and event.key == K_LEFT:
        Bat = pygame.image.load("bateau.jpeg").convert_alpha()
        fenetre.blit(Bat, (300,150))
        pygame.display.flip()
    if event.type == KEYDOWN and event.key == K_RIGHT:
        fenetre.blit(fond, (0,0))
        fenetre.blit(Quad1, (50,50))
        fenetre.blit(Quad2, (450,50))
        pygame.display.flip()
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        Obj2 = "N'essayez pas de vous echapper..."
        Obj3 = "Vous etes prisonnier !!"
        Esp2 = font.render(Obj2, 1, (255,0,0))
        Esp3 = font.render(Obj3, 1, (255,0,0))
        fenetre.blit(Esp2, (400,400))
        fenetre.blit(Esp3, (400,425))
        pygame.display.flip()

