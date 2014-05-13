# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:47:41 2014

@author: IG 158
"""

# Liste des fonctions utile pour le programme de recherche de navire de l'IA

#import Fonction_Ship
from random import *
from Fonction_Ship import Grille1
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
NbCoulIA = 0
#IndexIntermforAttaque = 0 #variable global intermédiaire permettant de récupérer la variable IndexCible une fois dans la fonction Attaque
IndexCible = 0
InAttaque = False
NbAttaque = 0
#Ini variable direction bateau (pour fonction d'attaque)
droite = False
gauche = False
haut = False
bas = False


def Define_List_Case_and_Strategie():
    global Grille1
    global CaseIA
    global Choice
    global A_Z
    global Z_A
    global Random
    #variable locale utile
    x = 0
    #Variable Stratégie IA
    A_Z = False
    Z_A = False
    Random = False
    #Liste des cases que l'IA choisira)
    CaseIA = []
    #Les boucles permettent d'ajouter les bonnes cases dans la liste "CaseIA", 
    #une case sur deux n'est pas exactement la bonne définition
    for x in range(0, 20):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(20, 40):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(40, 60):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(60, 80):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(80, 100):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(100, 20):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(120, 140):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(140, 160):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(160, 180):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(180, 200):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(200, 220):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(220, 240):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(240, 260):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(260, 280):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(280, 300):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(300, 320):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(320, 340):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(340, 360):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    for x in range(360, 380):
        if x % 2 == 0:
            CaseIA.append(Grille1[x])
    for x in range(380, 400):
        if x % 2 == 1:
            CaseIA.append(Grille1[x])
    print("Liste Case IA:")
    print(CaseIA)
    print("\n")
    #Détermination de la stratégie
    x = randint(1,3) #stratégie aléatoire
    print("choix strategie = " + str(x))
    if x == 1: #choix: du début vers la fin
        A_Z = True
        print("Strategie A a Z")
    elif x == 2: #choix: de la fin vers le début
        Z_A = True
        print("Strategie Z a A")
    else: #choix: aléatoire, sans procédé propre
        Random = True
        print("Strategie Case Aleatoire")
    Choice = 0 #Initialisation "choix de la case"
        
def Search_Ship(fenetre, CasePlayer1, RondBleu, CroixRouge, TextEAU, TextTOUCHE, TextCOULE, A_Z, Z_A, Random): #On utilise certaines variables du Main
    global CaseIA
    global Choice
    global InAttaque
    global NbCoulIA
    global droite
    global gauche
    global haut
    global bas
    global NbAttaque
    global IndexCible
    #global IndexIntermforAttaque
    print("\nIn Tour IA")
    print("NbAttaque = " + str(NbAttaque))
    Tour = False #Ini du Tour
    Choice = 0 #On prend en compte que la stratégie peut avoir changé entre temps, la réinitialisation de "Choice" s'impose donc
    if InAttaque == True: #l'IA essaie-t-il maintenant de couler un navire ?
        #IndexCible = IndexIntermforAttaque
        Attaque_Base_IA(Tour, Grille1, fenetre, CroixRouge, RondBleu, TextTOUCHE, TextEAU, TextCOULE)
    else: #Alors il en recherche un
        print("\nIn Search Ship")
        while Tour == False: #Le tour est-il terminé ?
            #réini de l'attaque (une fois dans cette boucle, toute attaque est terminé)
            NbAttaque = 0
            droite = False
            gauche = False
            haut = False
            bas = False
            if A_Z == True: #Si Stratégie "Début vers Fin"
                #Détermination de la case
                IndexCible = Choice 
                Cible = CaseIA[IndexCible]
                print("cible = " + str(Cible))
                #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
                if Cible[2] == 0:
                    CaseIA[IndexCible][2] = 1 #La case est maintenant touché
                    #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                    #Il y a-t-il un bateau sur la case touché ?
                    if Cible[1] == 0: 
                        #On affiche dans l'eau et on place un carrée bleu
                        print("dans l'eau") 
                        fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    else:
                        #On affiche touché et on place un carrée rouge
                        print("touche")
                        fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        #appelle fonction attaque
                        InAttaque = True
                        NbAttaque = NbAttaque + 1
                        #IndexIntermforAttaque = IndexCible
                    Tour = True #Fin du Tour de l'IA
            elif Z_A == True: #Si Stratégie "Fin vers Début"
                #Détermination de la case
                IndexCible = (-Choice)-1 # ==> Depuis la fin, ex: si Choice = 1, IndexCible = (-1)-1 = -2 (avant dernière case)
                Cible = CaseIA[IndexCible]
                print("cible = " + str(Cible))
                #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
                if Cible[2] == 0:
                    CaseIA[IndexCible][2] = 1 #La case est maintenant touché
                    #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                    #Il y a-t-il un bateau sur la case touché ?
                    if Cible[1] == 0:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("dans l'eau")
                        fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    else:
                        #On affiche touché et on place un carrée rouge
                        print("touche")
                        fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        #appelle fonction attaque
                        InAttaque = True
                        NbAttaque = NbAttaque + 1
                        #IndexIntermforAttaque = IndexCible
                    Tour = True #Fin du Tour de l'IA
            elif Random == True: #Si Stratégie "Case Aléatoire"
                #Détermination de la case
                IndexCible = randint(0, (len(CaseIA)-1)) #==> Une case au hasard dans la liste
                Cible = CaseIA[IndexCible]
                print("cible = " + str(Cible))
                #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
                if Cible[2] == 0:
                    CaseIA[IndexCible][2] = 1 #La case est maintenant touché
                    #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                    #Il y a-t-il un bateau sur la case touché ?
                    if Cible[1] == 0:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("dans l'eau")
                        fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    else:
                        #On affiche touché et on place un carrée rouge
                        print("touche")
                        fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        #appelle fonction attaque
                        InAttaque = True
                        NbAttaque = NbAttaque + 1
                        #IndexIntermforAttaque = IndexCible
                    Tour = True #Fin du Tour de l'IA
            Choice = Choice+1 #On passe à la case suivante (en cas d'échec)
    print("NbCoulIA in TourIA = " + str(NbCoulIA))
        
def Attaque_Base_IA(Tour, Grille1, fenetre, CroixRouge, RondBleu, TextTOUCHE, TextEAU, TextCOULE):
    global droite
    global gauche
    global haut
    global bas
    global NbAttaque
    global InAttaque
    global NbCoulIA
    global NbCoulIANavire
    global IndexCible
    print("\nIn Attaque_Base")
    print("\nhaut: " + str(haut))
    print("droite: " + str(droite))
    print("gauche: " + str(gauche))
    print("bas: " + str(bas) + "\n")
    print("NbAttaque = " + str(NbAttaque))
    if NbAttaque == 1: #Ne se fait qu'au début, recherche du sens du navire par un second tir
        while Tour == False: #Prend en compte le fait qu'une des 4 cases potentielles peut avoir été déjà touché
            NewCible = randint(1, 4) #choix aléatoire: Où attaquer maintenant ?
            print("NewCible = " + str(NewCible))
            print("IndexCible = " +str(IndexCible))
            if NewCible == 1:
                if list(Grille1[IndexCible][0])[0]+1 <= 485: #Il y a-t-il une case à droite ?
                    CaseCible = Grille1[IndexCible+1] #case à droite
                    if CaseCible[2] == 0: #La case a-t-elle été touché ?
                        Grille1[IndexCible+1][2] = 1 #On tir sur la case
                        print("IndexCase = " + str(IndexCible+20))
                        print("Case: " + str(CaseCible))
                        print("Bateau ?: " + str(CaseCible[1]))
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("touche")
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            droite = True #Le bateau continue bien sur la droite (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("dans l'eau")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
            elif NewCible == 2:
                if list(Grille1[IndexCible][0])[0]-1 >= 105: #Il y a-t-il une case à gauche ?
                    CaseCible = Grille1[IndexCible-1] #case à gauche
                    if CaseCible[2] == 0: #La case a-t-elle été touché ?
                        Grille1[IndexCible-1][2] = 1 #On tir sur la case
                        print("IndexCase = " + str(IndexCible+20))
                        print("Case: " + str(CaseCible))
                        print("Bateau ?: " + str(CaseCible[1]))
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("touche")
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            gauche = True #Le bateau continue bien sur la gauche (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("dans l'eau")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
            elif NewCible == 3:
                if list(Grille1[IndexCible][0])[1]-20 >= 105: #Il y a-t-il une case en haut ?
                    CaseCible = Grille1[IndexCible-20] #case en haut
                    if CaseCible[2] == 0: #La case a-t-elle été touché ?
                        Grille1[IndexCible-20][2] = 1 #On tir sur la case
                        print("IndexCase = " + str(IndexCible+20))
                        print("Case: " + str(CaseCible))
                        print("Bateau ?: " + str(CaseCible[1]))
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("touche")
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            haut = True #Le bateau continue bien vers le haut (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("dans l'eau")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
            elif NewCible == 4:
                if list(Grille1[IndexCible][0])[1]+20 <= 485: #Il y a-t-il une case en bas ?
                    CaseCible = Grille1[IndexCible+20] #case en bas
                    if CaseCible[2] == 0: #La case a-t-elle été touché ?
                        Grille1[IndexCible+20][2] = 1 #On tir sur la case
                        print("IndexCase = " + str(IndexCible+20))
                        print("Case: " + str(CaseCible))
                        print("Bateau ? : " + str(CaseCible[1]))
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("touche")
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            bas = True #Le bateau continue bien vers le bas (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("dans l'eau")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
            #Appelle fonction Nombre de Case
            NbCoulIANavire = 3
            if NbAttaque == NbCoulIANavire:
                InAttaque = False
                print("coule")
                fenetre.blit(TextCOULE, (414, 530)) #Affichage du texte "Coulé" sur le plateau
                NbCoulIA = NbCoulIA+1  
            
    else:
        #Appelle fonction suivante
        Attaque_Avancee_IA(Tour, Grille1, fenetre, CroixRouge, RondBleu, TextTOUCHE, TextEAU, TextCOULE)
    IndexCible = IndexCible+1 #Index suivant pour prochain tour (il s'agit en fait de la case touché ce tour)

def Attaque_Avancee_IA(Tour, Grille1, fenetre, CroixRouge, RondBleu, TextTOUCHE, TextEAU, TextCOULE):
    global droite
    global gauche
    global haut
    global bas
    global NbAttaque 
    global InAttaque
    global NbCoulIA
    global IndexCible
    print("\nIn Attaque Avancee")
    print("\nhaut: " + str(haut))
    print("droite: " + str(droite))
    print("gauche: " + str(gauche))
    print("bas: " + str(bas) + "\n")
    print("IndexCible = " +str(IndexCible))
    while Tour == False:
        if droite == True: #Le bateau continue-t-il à droite ?
            if list(Grille1[IndexCible][0])[0]+20 <= 485: #Il y a-t-il une case à droite ?
                CaseCible =  Grille1[IndexCible+1]
                Grille1[IndexCible+1][2] = 1 #On touche la case
                print("IndexCase = " + str(IndexCible+20))
                print("Case: " + str(CaseCible))
                print("Bateau ?: " + str(CaseCible[1]))
                if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                    #On affiche touché et on place un carrée rouge
                    print("touche")
                    fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                    fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                    NbAttaque = NbAttaque +1
                    Tour = True
                else:
                    #On affiche dans l'eau et on place un carrée bleu
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                    fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                    #Plus de bateau à droite: on continue à gauche pour le prochain tour
                    droite = False
                    gauche = True
                    Tour = True
            else: #Plus de case à droite: le bateau continue donc à gauche
                droite = False
                gauche = True 
        if gauche == True: #Le bateau continue-t-il à gauche ?
            if list(Grille1[IndexCible][0])[0]-20 >= 105: #Il y a-t-il une case à gauche ?
                CaseCible =  Grille1[IndexCible-1]
                Grille1[IndexCible-1][2] = 1 #On touche la case
                print("IndexCase = " + str(IndexCible+20))
                print("Case: " + str(CaseCible))
                print("Bateau ?: " + str(CaseCible[1]))
                if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                    #On affiche touché et on place un carrée rouge
                    print("touche")
                    fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                    fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                    NbAttaque = NbAttaque +1
                    Tour = True
                else:
                    #On affiche dans l'eau et on place un carrée bleu
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                    fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                    #Plus de bateau à droite: on continue à gauche pour le prochain tour
                    droite = True
                    gauche = False
                    Tour = True
            else: #Plus de case à gauche: le bateau continue donc à droite
                droite = True
                gauche = False 
        if haut == True: #Le bateau continue-t-il en haut ?
            if list(Grille1[IndexCible][0])[1]-20 >= 105: #Il y a-t-il une case en haut ?
                CaseCible =  Grille1[IndexCible-20]
                Grille1[IndexCible+20][2] = 1 #On touche la case
                print("IndexCase = " + str(IndexCible+20))
                print("Case: " + str(CaseCible))
                print("Bateau ?: " + str(CaseCible[1]))
                if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                    #On affiche touché et on place un carrée rouge
                    print("touche")
                    fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                    fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                    NbAttaque = NbAttaque +1
                    Tour = True
                else:
                    #On affiche dans l'eau et on place un carrée bleu
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                    fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                    #Plus de bateau à droite: on continue à gauche pour le prochain tour
                    bas = True
                    haut = False
                    Tour = True
            else: #Plus de case à gauche: le bateau continue donc à droite
                bas = True
                haut = False
        if bas == True: #Le bateau continue-t-il en bas ?
            if list(Grille1[IndexCible][0])[1]+20 <= 485: #Il y a-t-il une case en haut ?
                CaseCible =  Grille1[IndexCible+20]
                Grille1[IndexCible+20][2] = 1 #On touche la case
                print("IndexCase = " + str(IndexCible+20))
                print("Case: " + str(CaseCible))
                print("Bateau ?: " + str(CaseCible[1]))
                if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                    #On affiche touché et on place un carrée rouge
                    print("touche")
                    fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                    fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                    NbAttaque = NbAttaque +1
                    Tour = True
                else:
                    #On affiche dans l'eau et on place un carrée bleu
                    print("dans l'eau")
                    fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                    fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                    #Plus de bateau à droite: on continue à gauche pour le prochain tour
                    haut = True
                    bas = False
                    Tour = True
            else: #Plus de case à gauche: le bateau continue donc à droite
                haut = True
                bas = False
    if NbAttaque == NbCoulIANavire:
        InAttaque = False
        print("coule")
        fenetre.blit(TextCOULE, (414, 530)) #Affichage du texte "Touché" sur le plateau
        NbCoulIA = NbCoulIA+1
    IndexCible = IndexCible+1 #Index suivant pour prochain tour (il s'agit en fait de la case touché ce tour)
        