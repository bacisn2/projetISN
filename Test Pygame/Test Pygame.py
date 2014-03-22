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

#OpenDicoCP = open('CasePlayer.txt', 'r')
#OpenDicoBP = open('BateauPlayer.txt', 'r')
#ReadDicoCP = OpenDicoCP.read()
#ReadDicoBP = OpenDicoBP.read()
#CasePlayer1 = {"A1":(105,105), "A2":(125,105), "A3":(145,105), "A4":(165,105), "A5":(185,105), "A6":(205,105), "A7":(225,105), "A8":(245,105), "A9":(265,105), "A10":(285,105), "A11":(305,105), "A12":(325,105), "A13":(345,105), "A14":(365,105), "A15":(385,105), "A16":(405,105), "A17":(425,105), "A18":(445,105), "A19":(465,105), "A20":(485,105), "B1":(105,125), "B2":(125,125), "B3":(145,125), "B4":(165,125), "B5":(185,125), "B6":(205,125), "B7":(225,125),"B8":(245,125), "B9":(265,125),  "B10":(285,125),  "B11":(305,125),  "B12":(325,125),  "B13":(345,125),  "B14":(365,125),  "B15":(385,125),  "B16":(405,125),  "B17":(425,125),  "B18":(445,125),  "B19":(465,125),  "B20":(485,125),  "C1":(105,145), "C2":(125,145), "C3":(145,145), "C4":(165,145),  "C5":(185,145),  "C6":(205,145),  "C7":(225,145),  "C8":(245,145),  "C9":(265,145),  "C10":(285,145),  "C11":(305,145), "C12":(325,145), "C13":(345,145), "C14":(365,145), "C15":(385,145), "C16":(405,145), "C17":(425,145), "C18":(445,145), "C19":(465,145), "C20":(485,145), "D1":(105,165), "D2":(125,165), "D3":(145,165), "D4":(165,165), "D5":(185,165), "D6":(205,165), "D7":(225,165), "D8":(245,165), "D9":(265,165), "D10":(285,165), "D11":(305,165), "D12":(325,165), "D13":(345,165), "D14":(365,165), "D15":(385,165), "D16":(405,165), "D17":(425,165), "D18":(445,165), "D19":(465,165), "D20":(485,165), "E1":(105,185), "E2":(125,185), "E3":(145,185), "E4":(165,185), "E5":(185,185), "E6":(205,185), "E7":(225,185), "E8":(245,185),"E9":(265,185), "E10":(285,185),  "E11":(305,185),  "E12":(325,185),  "E13":(345,185),  "E14":(365,185),  "E15":(385,185),  "E16":(405,185),  "E17":(425,185),  "E18":(445,185),  "E19":(465,185),  "E20":(485,185), "F1":(105,205), "F2":(125,205), "F3":(145,205), "F4":(165,205),  "F5":(185,205),  "F6":(205,205),  "F7":(225,205),  "F8":(245,205),  "F9":(265,205),  "F10":(285,205), "F11":(305,205), "F12":(325,205), "F13":(345,205), "F14":(365,205), "F15":(385,205), "F16":(405,205), "F17":(425,205), "F18":(445,205), "F19":(465,205),  "F20":(485,205), "G1":(105,225), "G2":(125,225), "G3":(145,225), "G4":(165,225), "G5":(185,225), "G6":(205,225), "G7":(225,225), "G8":(245,225), "G9":(265,225), "G10":(285,225), "G11":(305,225), "G12":(325,225), "G13":(345,225), "G14":(365,225), "G15":(385,225), "G16":(405,225), "G17":(425,225), "G18":(445,225), "G19":(465,225), "G20":(485,225), "H1":(105,245), "H2":(125,245), "H3":(145,245), "H4":(165,245), "H5":(185,245), "H6":(205,245), "H7":(225,245), "H8":(245,245), "H9":(265,245),"H10":(285,245), "H11":(305,245),  "H12":(325,245),  "H13":(345,245),  "H14":(365,245),  "H15":(385,245),  "H16":(405,245),  "H17":(425,245),  "H18":(445,245),  "H19":(465,245),  "H20":(485,245), "I1":(105,265), "I2":(125,265), "I3":(145,265), "I4":(165,265),  "I5":(185,265),  "I6":(205,265),  "I7":(225,265),  "I8":(245,265),  "I9":(265,265), "I10":(285,265), "I11":(305,265), "I12":(325,265), "I13":(345,265), "I14":(365,265), "I15":(385,265), "I16":(405,265), "I17":(425,265), "I18":(445,265), "I19":(465,265),  "I20":(485,265), "J1":(105,285), "J2":(125,285), "J3":(145,285), "J4":(165,285), "J5":(185,285), "J6":(205,285), "J7":(225,285), "J8":(245,285), "J9":(265,285), "J10":(285,285), "J11":(305,285), "J12":(325,285), "J13":(345,285), "J14":(365,285), "J15":(385,285), "J16":(405,285), "J17":(425,285), "J18":(445,285), "J19":(465,285), "J20":(485,285), "K1":(105,305), "K2":(125,305), "K3":(145,305), "K4":(165,305), "K5":(185,305), "K6":(205,305), "K7":(225,305), "K8":(245,305), "K9":(265,305), "K10":(285,305), "K11":(305,305), "K12":(325,305),  "K13":(345,305),  "K14":(365,305),  "K15":(385,305),  "K16":(405,305),  "K17":(425,305),  "K18":(445,305),  "K19":(465,305),  "K20":(485,305), "L1":(105,325), "L2":(125,325), "L3":(145,325), "L4":(165,325),  "L5":(185,325),  "L6":(205,325),  "L7":(225,325),  "L8":(245,325), "L9":(265,325), "L10":(285,325), "L11":(305,325), "L12":(325,325), "L13":(345,325),  "L14":(365,325), "L15":(385,325), "L16":(405,325), "L17":(425,325), "L18":(445,325), "L19":(465,325),  "L20":(485,325), "M1":(105,345), "M2":(125,345), "M3":(145,345), "M4":(165,345),  "M5":(185,345),  "M6":(205,345), "M7":(225,345), "M8":(245,345), "M9":(265,345), "M10":(285,345), "M11":(305,345), "M12":(325,345), "M13":(345,345), "M14":(365,345), "M15":(385,345), "M16":(405,345), "M17":(425,345), "M18":(445,345), "M19":(465,345),  "M20":(485,345), "N1":(105,365), "N2":(125,365), "N3":(145,365), "N4":(165,365), "N5":(185,365), "N6":(205,365), "N7":(225,365), "N8":(245,365), "N9":(265,365), "N10":(285,365), "N11":(305,365), "N12":(325,365), "N13":(345,365),  "N14":(365,365),  "N15":(385,365),  "N16":(405,365),  "N17":(425,365),  "N18":(445,365),  "N19":(465,365),  "N20":(485,365), "O1":(105,385), "O2":(125,385), "O3":(145,385), "O4":(165,385),  "O5":(185,385),  "O6":(205,385),  "O7":(225,385), "O8":(245,385),  "O9":(265,385),  "O10":(285,385), "O11":(305,385), "O12":(325,385), "O13":(345,385), "O14":(365,385), "O15":(385,385), "O16":(405,385), "O17":(425,385), "O18":(445,385),  "O19":(465,385), "O20":(485,385), "P1":(105,405), "P2":(125,405), "P3":(145,405), "P4":(165,405), "P5":(185,405), "P6":(205,405), "P7":(225,405), "P8":(245,405), "P9":(265,405), "P10":(285,405), "P11":(305,405), "P12":(325,405), "P13":(345,405), "P14":(365,405), "P15":(385,405), "P16":(405,405), "P17":(425,405), "P18":(445,405), "P19":(465,405), "P20":(485,405), "Q1":(105,425), "Q2":(125,425), "Q3":(145,425), "Q4":(165,425),  "Q5":(185,425), "Q6":(205,425),  "Q7":(225,425), "Q8":(245,425), "Q9":(265,425), "Q10":(285,425), "Q11":(305,425), "Q12":(325,425), "Q13":(345,425), "Q14":(365,425),  "Q15":(385,425),  "Q16":(405,425),  "Q17":(425,425),  "Q18":(445,425),  "Q19":(465,425),  "Q20":(485,425), "R1":(105,445), "R2":(125,445), "R3":(145,445), "R4":(165,445),  "R5":(185,445),  "R6":(205,445), "R7":(225,445), "R8":(245,445), "R9":(265,445), "R10":(285,445), "R11":(305,445), "R12":(325,445), "R13":(345,445), "R14":(365,445), "R15":(385,445), "R16":(405,445), "R17":(425,445), "R18":(445,445), "R19":(465,445), "R20":(485,445), "S1":(105,465), "S2":(125,465), "S3":(145,465), "S4":(165,465), "S5":(185,465), "S6":(205,465), "S7":(225,465), "S8":(245,465), "S9":(265,465), "S10":(285,465), "S11":(305,465), "S12":(325,465), "S13":(345,465), "S14":(365,465), "S15":(385,465), "S16":(405,465), "S17":(425,465), "S18":(445,465), "S19":(465,465), "S20":(485,465), "T1":(105,485), "T2":(125,485), "T3":(145,485), "T4":(165,485), "T5":(185,485), "T6":(205,485), "T7":(225,485),  "T8":(245,485), "T9":(265,485), "T10":(285,485), "T11":(305,485), "T12":(325,485), "T13":(345,485), "T14":(365,485), "T15":(385,485),  "T16":(405,485),  "T17":(425,485),  "T18":(445,485),  "T19":(465,485),  "T20":(485,485)}
BateauPlayer = {"LitShip":pygame.image.load("bateau 10.jpg").convert_alpha(), "LitShipV":pygame.image.load("bateau 10 V.jpg").convert_alpha(),"SMV":pygame.image.load("sous-marin 1 V.jpg").convert_alpha(), "SM":pygame.image.load("sous-marin 1.jpg").convert_alpha(), "CuirBase":pygame.image.load("bateau 22.jpg").convert_alpha(), "CuirBaseV":pygame.image.load("bateau 22 V.jpg").convert_alpha(), "CuirSuper":pygame.image.load("bateau 25.jpg").convert_alpha(), "CuirSuperV":pygame.image.load("bateau 25 V.jpg").convert_alpha(), "Cuir2":pygame.image.load("bateau 26.jpg").convert_alpha(), "Cuir2V":pygame.image.load("bateau 26 V.jpg").convert_alpha(), "PA":pygame.image.load("bateau 23.jpg").convert_alpha(), "PAV":pygame.image.load("bateau 23 V.jpg").convert_alpha()}
CasePlayer1 = {}
execfile(CasePlayer.txt, CasePlayer1)
print(CasePlayer1)

Infinie = 1 #Fait tourner indéfiniment le programme
CountShip = 0

#Liste des commandes pour le début
TextD1 = "Appuyez sur 2, 3, 4, 5 pour placez un bateau predefini. Appuyez sur \"haut\" pour reinitialiser le plateau"
TextD2 = "Appuyez sur \"b\" pour placez un bateau (que vous choisirez) sur une case (que vous choisirez)"
TextD3 = "Appuyez sur \"haut\" pour supprimer ce message"
Instr1 = font.render(TextD1, 1, (150,200,100))
Instr2 = font.render(TextD2, 1, (150,200,100))
Instr3 = font.render(TextD3, 1, (150,200,100))
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
            Bat = pygame.image.load("Bateau 4 (sous-marin 1) V.jpg").convert_alpha()
            fenetre.blit(Bat, (385,285))
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_b:
            print("Entrez le bateau")
            Bat = raw_input()
            print("Entrez sa case")
            Coord = raw_input()
            if Bat in BateauPlayer and Coord in CasePlayer1 and CountShip <= 10:
                CountShip = CountShip + 1
                NewBat = BateauPlayer[Bat]
                fenetre.blit(NewBat, CasePlayer1[Coord])
                pygame.display.flip()
            else:
                print("Bateau ou Case inexistante \nVeuillez ressaisir après avoir appuyez sur \"b\"")                
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
