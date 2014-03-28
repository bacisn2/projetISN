# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:37:59 2014

@author: IG 158
"""
#NOTE A L'ATTENTION DU PROFESSEUR D'ISN:
#Certains "print" (dans ce programme ou les sous programmes) n'affiche pas des textes 
#mais des variables. Ils me servent à vérifier le bon fonctionnement du programme 
#(notamment l'état de la variable "Bateau/pas Bateau" invisible sur le plateau de jeu)

#NOTE UTILE SUR LA GESTION DES COORDONNEES (SUROUT POUR MICKAËL !):
#Le Tuple de Coordonnées de la case (ex: (105, 105) pour A1) est géré différemment par
# pygame que par notre esprit. Nous assossions la lettre puis le chiffre, le programme
#fait l'inverse: dans (105, 105), le premier 105 est le chiffre et le second est la 
#lettre. Ce Tuple ne se lit donc pas (A, 1) mais (1, A), l'ordi dit donc 1A ;)

#PARTIE IMPORTATION PROGRAMME UTILE
#Importation de début (Pygame + Dicos + Fonction_Ship)
import pygame
from pygame.locals import *
#import Dico_Grille2 #(inutilisé à ce jour... Le sera prochainement)
from Fonction_Ship import *
import Dico_Grille1
import Dico_Ship
#FIN PARTIE IMPORTATION PROGRAMME UTILE 
#(NB: d'autres importation seront faîtes quand le programme sera plus avancée)

#PARTIE INITIALISATION DU JEU
#Ini Pygame + fond pour les textes
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 30) #Transparent pour l'affichage des Textes (version 30 px)
SuperFont = pygame.font.Font(None, 80) #Transparent pour l'affichage des Textes (version 80 px)

#Ini des Grilles (on joue les fonctions puis on importe les grilles créees ainsi)
IniListeCaseGrille1()
IniListeCaseGrille2()
from Fonction_Ship import Grille1
from Fonction_Ship import Grille2
    
#Ini Fenêtre + Fond Blanc
#Crée une fenêtre de 1200*900 pixel pour le Jeu
fenetre = pygame.display.set_mode((1200, 900))
#Charge l'image
fond = pygame.image.load("Fond_Blanc_1200-900.jpg")
#Positionne l'image
fenetre.blit(fond, (0,0))
#Rafraichit le Plateau de Jeu
pygame.display.flip()

#Ini Quadriallage (sans marquage)
#Charge l'image
Quad1 = pygame.image.load("The Quadrillage 2.jpg")
#Positionne les images
fenetre.blit(Quad1, (100,100))
fenetre.blit(Quad1, (600,100))
#Rafraichit le Plateau de Jeu
pygame.display.flip()

#Ini marquage Quadrillage
#Charge les images
Ligne = pygame.image.load("Ligne_Tableau.jpg")
Colonne = pygame.image.load("Colonne_Tableau.jpg")
#Positionne les images
fenetre.blit(Ligne, (80,100))
fenetre.blit(Ligne, (580,100))
fenetre.blit(Colonne, (100,75))
fenetre.blit(Colonne, (600,75))
#Rafraichit le Plateau de Jeu
pygame.display.flip()

#Importation Dicos + Initialisation Compteurs
CasePlayer1 = Dico_Grille1.GrillePlayer1
BateauPlayer = Dico_Ship.Ship1
Infinie = 1 #Fait tourner indéfiniment le programme
CountShip = 0 #Compteur Navires

#Liste des commandes pour le début
#Création des Textes
TextD1 = "Appuyez sur 2, 3, 4, 5 pour placez un bateau predefini. Appuyez sur \"haut\" pour reinitialiser le plateau"
TextD2 = "Appuyez sur \"b\" pour placez un bateau (que vous choisirez) sur une case (que vous choisirez)"
TextD3 = "Appuyez sur \"haut\" pour supprimer ce message"
#Chargement des Textes
Instr1 = font.render(TextD1, 1, (0,0,0))
Instr2 = font.render(TextD2, 1, (0,0,0))
Instr3 = font.render(TextD3, 1, (0,0,0))
#Placement des Textes sur le Plateau de Jeu
fenetre.blit(Instr1, (100,300))
fenetre.blit(Instr2, (100,335))
fenetre.blit(Instr3, (100,370))
#Raifraichissement du Plateau de Jeu
pygame.display.flip()
#FIN PARTIE INITIALISATION DU JEU

#MAIN PROGRAMME         
while Infinie == 1:
    for event in pygame.event.get(): #Fait la liste des évènements possible (appuyer sur une touche, souris, etc...)
        if event.type == QUIT: #Quitte la partie quand on appuie sur "Quitter" (sous Windows 8 avec Python 2.6.6)
            Infinie = 0 #Fin de la Boucle (FIN MAIN PROGRAMME)
        if event.type == KEYDOWN and event.key == K_SPACE: #Test Espace
            #Dans l'ordre: Création, Chargement, Positionnement du texte et Rafraichissement du Plateau de Jeu
            Obj = "Espace"
            Esp = font.render(Obj, 1, (0,0,0))
            fenetre.blit(Esp, (200,500))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_ESCAPE: #Message Mystère
            #Création des Textes
            Obj2 = "N'essayez pas de vous echapper..."
            Obj3 = "Vous etes prisonnier !!"
            #Chargement des Textes
            Esp2 = font.render(Obj2, 1, (255,0,0))
            Esp3 = font.render(Obj3, 1, (255,0,0))
            #Placement des Textes
            fenetre.blit(Esp2, (800,500))
            fenetre.blit(Esp3, (800,525))
            #Rafraichissement du Plateau de Jeu
            pygame.display.flip()   
            
#PARTIE OBSOLETE 
        #la variable "Bateau/pas Bateau" n'est pas prise en compte pour ces positionnement
        #if event.type == KEYDOWN and event.key == K_KP5: #Placement bateau 5 cases (K6)
        #    CountShip = CountShip + 1            
        #    Bat = pygame.image.load("bateau 23.jpg").convert_alpha()
        #    fenetre.blit(Bat, (205,305))
        #    pygame.display.flip()
        #if event.type == KEYDOWN and event.key == K_KP2: #Placement bateau 2 cases (T19)
        #    CountShip = CountShip + 1            
        #    Bat = pygame.image.load("bateau 10.jpg").convert_alpha()
        #    fenetre.blit(Bat, (465,485))
        #    pygame.display.flip()            
        #if event.type == KEYDOWN and event.key == K_KP4: #Placement du bateau 4 cases (A1)
        #    CountShip = CountShip + 1            
        #    Bat = pygame.image.load("bateau 22.jpg").convert_alpha()
        #    fenetre.blit(Bat, (105,105))
        #    pygame.display.flip()
        #if event.type == KEYDOWN and event.key == K_KP3: #Placement du bateau 3 cases (J15)
        #    CountShip = CountShip + 1
        #    Bat = pygame.image.load("sous-marin 1 V.jpg").convert_alpha()
        #    fenetre.blit(Bat, (385,285))
        #    pygame.display.flip()
#FIN PARTIE OBSOLETE
            
        #Placement du bateau sur la Grille de Gauche
        if event.type == KEYDOWN and event.key == K_b:
            #Vérifie s'il y a déjà le nombre max de bateau en jeu
            if CountShip < 6: 
                #Appelle de la Fonction de position du Navire
                #Cette Fonction appelera une sous-fontion qui à son tour 
                #appelera deux sous-fonctions (choix entre les deux)
                Grille1_Pos_Navire() 
                #Positionnement du Navire souhaiter (image)
                from Fonction_Ship import Bat
                from Fonction_Ship import Coord
                from Fonction_Ship import EchecPosition
                if EchecPosition == False:
                    CountShip = CountShip + 1 #+ 1 bateau
                    NewBat = BateauPlayer[Bat] #Chargement de la Case
                    fenetre.blit(NewBat, CasePlayer1[Coord]) #Placement de l'image du bateau
                    pygame.display.flip() #Rafraichissement du Plateau de Jeu
                    print(Grille1)
            else:
                print("Nombre de navire max atteint")
        #réinitialisation du plateau
        if event.type == KEYDOWN and event.key == K_UP: 
            #réinitialisation du nombre de bateau en jeu
            CountShip = 0          
            #Réinitialisation des Grilles
            IniListeCaseGrille1()
            IniListeCaseGrille2()
            from Fonction_Ship import Grille1
            from Fonction_Ship import Grille2
            #Réinitialisation du Plateau de Jeu
            fenetre.blit(fond, (0,0))
            fenetre.blit(Quad1, (100,100))
            fenetre.blit(Quad1, (600,100))
            fenetre.blit(Ligne, (80,100))
            fenetre.blit(Ligne, (580,100))
            fenetre.blit(Colonne, (100,75))
            fenetre.blit(Colonne, (600,75))
            pygame.display.flip()
#FIN MAIN PROGRAMME