# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:08:28 2014

@author: mickael
"""

import random
#On import les dicos des phrases dites par l'IA
from DicoTexte import TexteJoueurEau
from DicoTexte import TexteJoueurImpact
from DicoTexte import TexteIAEau
from DicoTexte import TexteIAImpact
from DicoTexte import TexteJoueurNul
import pygame    
from pygame.locals import *
from Main_Programme import *

def TexteJoueurEau() :
    global fenetre
    global font
    a = random.randint(1, 5) #Variable aléatoire pour le choix de la phrase
    PhraseBrut = TexteJoueurEau[a] #Affecte la phrase choisis dans le dico à une variable
    Phrase = font.render(PhraseBrut, 1, (0,0,0)) #Choix de la taille du texte (font:30px) et la couleur (trois 0 pour noir)
    fenetre.blit(Phrase, (100, 30)) #Placement du texte à tel coordonées
    pygame.display.flip() #Rafraichit le plateau de jeu pour afficher le texte

def TexteJoueurImpact() :
    global fenetre
    global font
    a = random.randint(1, 4)
    PhraseBrut = TexteJoueurImpact[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteJoueurNul() :
    global fenetre
    global font
    a = random.randint(1, 3)
    PhraseBrut = TexteJoueurNul[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteIAEau() :
    global fenetre
    global font
    a = random.randint(1, 3)
    PhraseBrut = TexteIAEau[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    
def TexteIAImpact() :
    global fenetre
    global font
    a = random.randint(1, 3)
    PhraseBrut = TexteIAImpact[a]
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
    