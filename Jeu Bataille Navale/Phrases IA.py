# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:08:28 2014

@author: mickael
"""

from pygame.locals import *

def TexteIA(fenetre, font) :
    import pygame    
    PhraseBrut = "Je t'ai trouve et tu ne pourras m'echapper car tu es a ma merci"
    Phrase = font.render(PhraseBrut, 1, (0,0,0))
    fenetre.blit(Phrase, (100, 30))
    pygame.display.flip()
