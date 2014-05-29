# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:08:28 2014

@author: mickael
"""

import random
#On import les dicos des phrases dites par l'IA
from DicoTexte import TexteJoueurEau
from DicoTexte import TexteJoueurImpact
from DicoTexte import TexteJoueurCoul
from DicoTexte import TexteJoueurNul
from DicoTexte import TexteIAEau
from DicoTexte import TexteIAImpact
from DicoTexte import TexteIACoul

import pygame    
from pygame.locals import *

def TexteJoueurEauF(fenetre, font) :
    a = random.randint(1, 5) #Variable aléatoire pour le choix de la phrase
    PhraseBrut = TexteJoueurEau[a] #Affecte la phrase choisis dans le dico à une variable
    Phrase = font.render(PhraseBrut, 1, (0,0,0)) #Choix de la taille du texte (font:30px) et la couleur (trois 0 pour noir)
    fenetre.blit(Phrase, (100, 30)) #Placement du texte à tel coordonées
    pygame.display.flip() #Rafraichit le plateau de jeu pour afficher le texte

def TexteJoueurImpactF(fenetre, font) :
    a = random.randint(1, 4)
    PhraseBrut = TexteJoueurImpact[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteJoueurCoulF(fenetre, font) :
    a = random.randint(1, 3)
    PhraseBrut = TexteJoueurCoul[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteJoueurNulF(fenetre, font) :
    a = random.randint(1, 3)
    PhraseBrut = TexteJoueurNul[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteIAEauF(fenetre, font) :
    a = random.randint(1, 3)
    PhraseBrut = TexteIAEau[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteIAImpactF(fenetre, font) :
    a = random.randint(1, 3)
    PhraseBrut = TexteIAImpact[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteIACoulF(fenetre, font) :
    a = random.randint(1, 3)
    PhraseBrut = TexteIACoul[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()