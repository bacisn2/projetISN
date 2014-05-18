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
Reference = [] #Case la plus à droite en haut, la case référence du bateau
FirstCase = 0 #Index Première case touché, on y revient si on s'est trompé de sens


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
    #print("Liste Case IA:") #Désactivé pour inutilité à ce stade
    #print(CaseIA) #Désactivé pour inutilité à ce stade
    #Détermination de la stratégie
    x = randint(1,3) #stratégie aléatoire
    print("choix strategie = " + str(x))
    if x == 1: #choix: du début vers la fin
        A_Z = True
        #print("Strategie A a Z") #Le joueur n'a pas à savoir ceci
    elif x == 2: #choix: de la fin vers le début
        Z_A = True
        #print("Strategie Z a A") #Le joueur n'a pas à savoir ceci
    else: #choix: aléatoire, sans procédé propre
        Random = True
        #print("Strategie Case Aleatoire") #Le joueur n'a pas à savoir ceci
    Choice = 0 #Initialisation "choix de la case"
        
def Search_Ship(fenetre, CasePlayer1, RondBleu, CroixRouge, TextEAU, TextTOUCHE, TextCOULE, A_Z, Z_A, Random, Dico_IA): #On utilise certaines variables du Main
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
    global Reference
    global FirstCase
    #global IndexIntermforAttaque
    print("In Tour IA")
    print("NbAttaque = " + str(NbAttaque))
    Tour = False #Ini du Tour
    Choice = 0 #On prend en compte que la stratégie peut avoir changé entre temps, la réinitialisation de "Choice" s'impose donc
    if InAttaque == True: #l'IA essaie-t-il maintenant de couler un navire ?
        #IndexCible = IndexIntermforAttaque
        Attaque_Base_IA(Tour, Grille1, fenetre, CroixRouge, RondBleu, TextTOUCHE, TextEAU, TextCOULE, Dico_IA)
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
                    Code = Dico_IA[Cible[0]]
                    print(Code)
                    CaseIA[IndexCible][2] = 1 #La case est maintenant touché
                    #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                    #Il y a-t-il un bateau sur la case touché ?
                    if Cible[1] == 0: 
                        #On affiche dans l'eau et on place un carrée bleu
                        print("DANS L'EAU")
                        fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    else:
                        #On affiche touché et on place un carrée rouge
                        print("TOUCHE")
                        print("IndexCible in CaseIA = " + str(IndexCible))
                        fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        IndexCible = Grille1.index(Cible)
                        print("IndexCible in Grille1 = " + str(IndexCible))
                        #appelle fonction attaque
                        InAttaque = True
                        NbAttaque = NbAttaque + 1
                        Reference = Cible #On considère qu'on a touché la case de référence (ceci pourras être démenti par la suite)
                        FirstCase = IndexCible #Voici la première case touché (ne change plus jusqu'au prochain navire)
                    Tour = True #Fin du Tour de l'IA
            elif Z_A == True: #Si Stratégie "Fin vers Début"
                #Détermination de la case
                IndexCible = (-Choice)-1 # ==> Depuis la fin, ex: si Choice = 1, IndexCible = (-1)-1 = -2 (avant dernière case)
                Cible = CaseIA[IndexCible]
                print("cible = " + str(Cible))
                #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
                if Cible[2] == 0:
                    Code = Dico_IA[Cible[0]]
                    print(Code)
                    CaseIA[IndexCible][2] = 1 #La case est maintenant touché
                    #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                    #Il y a-t-il un bateau sur la case touché ?
                    if Cible[1] == 0:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("DANS L'EAU")
                        fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    else:
                        #On affiche touché et on place un carrée rouge
                        print("TOUCHE")
                        print("IndexCible in CaseIA = " + str(IndexCible))
                        fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        IndexCible = Grille1.index(Cible)
                        print("IndexCible in Grille1 = " + str(IndexCible))
                        #appelle fonction attaque
                        InAttaque = True
                        NbAttaque = NbAttaque + 1
                        Reference = Cible #On considère qu'on a touché la case de référence (ceci pourras être démenti par la suite)
                        FirstCase = IndexCible #Voici la première case touché (ne change plus jusqu'au prochain navire)
                    Tour = True #Fin du Tour de l'IA
            elif Random == True: #Si Stratégie "Case Aléatoire"
                #Détermination de la case
                IndexCible = randint(0, (len(CaseIA)-1)) #==> Une case au hasard dans la liste
                Cible = CaseIA[IndexCible]
                print("cible = " + str(Cible))
                #Test de la case: A-t-elle déjà été touché ? (inclus, "est-t-elle à côté d'un bateau coulé ?")
                if Cible[2] == 0:
                    Code = Dico_IA[Cible[0]]
                    print(Code)
                    CaseIA[IndexCible][2] = 1 #La case est maintenant touché
                    #print [c for c,Cible[0] in CasePlayer1.items() if CasePlayer1[c]==Cible[0]]
                    #Il y a-t-il un bateau sur la case touché ?
                    if Cible[1] == 0:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("DANS L'EAU")
                        fenetre.blit(RondBleu, CaseIA[IndexCible][0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    else:
                        #On affiche touché et on place un carrée rouge
                        print("TOUCHE")
                        print("IndexCible in CaseIA = " + str(IndexCible))
                        fenetre.blit(CroixRouge, CaseIA[IndexCible][0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        IndexCible = Grille1.index(Cible)
                        print("IndexCible in Grille1 = " + str(IndexCible))
                        #appelle fonction attaque
                        InAttaque = True
                        NbAttaque = NbAttaque + 1
                        Reference = Cible #On considère qu'on a touché la case de référence (ceci pourras être démenti par la suite)
                        FirstCase = IndexCible #Voici la première case touché (ne change plus jusqu'au prochain navire)
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
    global Reference
    global FirstCase
    print("In Attaque_Base")
    print("haut: " + str(haut))
    print("droite: " + str(droite))
    print("gauche: " + str(gauche))
    print("bas: " + str(bas))
    print("NbAttaque in start Tour = " + str(NbAttaque))
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
                        print("IndexCase = " + str(IndexCible+1))
                        print("Case: " + str(CaseCible))
                        print("Bateau ?: " + str(CaseCible[1]))
                        Code = Dico_IA[CaseCible[0]]
                        print(Code)
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("TOUCHE")
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            droite = True #Le bateau continue bien sur la droite (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            IndexCible = IndexCible+1
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("DANS L'EAU")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
                            break
            elif NewCible == 2:
                if list(Grille1[IndexCible][0])[0]-1 >= 105: #Il y a-t-il une case à gauche ?
                    CaseCible = Grille1[IndexCible-1] #case à gauche
                    if CaseCible[2] == 0: #La case a-t-elle été touché ?
                        Grille1[IndexCible-1][2] = 1 #On tir sur la case
                        print("IndexCase = " + str(IndexCible-1))
                        print("Case: " + str(CaseCible))
                        print("Bateau ?: " + str(CaseCible[1]))
                        Code = Dico_IA[CaseCible[0]]
                        print(Code)
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("TOUCHE")
                            Reference = CaseCible #Nouvelle case la plus à gauche: Nouvelle Référence
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            gauche = True #Le bateau continue bien sur la gauche (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            IndexCible = IndexCible-1
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("DANS L'EAU")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
                            break
            elif NewCible == 3:
                if list(Grille1[IndexCible][0])[1]-20 >= 105: #Il y a-t-il une case en haut ?
                    CaseCible = Grille1[IndexCible-20] #case en haut
                    if CaseCible[2] == 0: #La case a-t-elle été touché ?
                        Grille1[IndexCible-20][2] = 1 #On tir sur la case
                        print("IndexCase = " + str(IndexCible-20))
                        print("Case: " + str(CaseCible))
                        print("Bateau ?: " + str(CaseCible[1]))
                        Code = Dico_IA[CaseCible[0]]
                        print(Code)
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("TOUCHE")
                            Reference = CaseCible #Nouvelle case la plus en haut: Nouvelle Référence
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            haut = True #Le bateau continue bien vers le haut (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            IndexCible = IndexCible-20
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("DANS L'EAU")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
                            break
            elif NewCible == 4:
                if list(Grille1[IndexCible][0])[1]+20 <= 485: #Il y a-t-il une case en bas ?
                    CaseCible = Grille1[IndexCible+20] #case en bas
                    if CaseCible[2] == 0: #La case a-t-elle été touché ?
                        Grille1[IndexCible+20][2] = 1 #On tir sur la case
                        print("IndexCase = " + str(IndexCible+20))
                        print("Case: " + str(CaseCible))
                        print("Bateau ? : " + str(CaseCible[1]))
                        Code = Dico_IA[CaseCible[0]]
                        print(Code)
                        if CaseCible[1] == 1: #Il y a-t-il un bateau sur cette case ?
                            #On affiche touché et on place un carrée rouge
                            print("TOUCHE")
                            fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                            fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                            bas = True #Le bateau continue bien vers le bas (utile pour le tour suivant)
                            NbAttaque = NbAttaque +1
                            IndexCible = IndexCible+20
                            Tour = True
                        else:
                            #On affiche dans l'eau et on place un carrée bleu
                            print("DANS L'EAU")
                            fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                            fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                            Tour = True
                            break 
            #Appelle fonction Nombre de Case
            CountNbCoulIANavire(Grille1, IndexCible)                
            if NbAttaque == NbCoulIANavire:
                InAttaque = False
                print("COULE")
                fenetre.blit(TextCOULE, (414, 530)) #Affichage du texte "Coulé" sur le plateau
                Fonction_Ckeck_Coulage_Fin()
                NbCoulIA = NbCoulIA+1 #+1 navire coulé, la victoire est proche... 
    else:
        #Appelle fonction suivante
        Attaque_Avancee_IA(Tour, Grille1, fenetre, CroixRouge, RondBleu, TextTOUCHE, TextEAU, TextCOULE)
    print("NbAttaque in End Tour = " + str(NbAttaque))

def Attaque_Avancee_IA(Tour, Grille1, fenetre, CroixRouge, RondBleu, TextTOUCHE, TextEAU, TextCOULE):
    global droite
    global gauche
    global haut
    global bas
    global NbAttaque
    global InAttaque
    global NbCoulIA
    global NbCoulIANavire
    global IndexCible
    global Reference
    global FirstCase
    print("In Attaque Avancee")
    print("haut: " + str(haut))
    print("droite: " + str(droite))
    print("gauche: " + str(gauche))
    print("bas: " + str(bas))
    print("IndexCible base = " +str(IndexCible))
    while Tour == False:
        if droite == True: #Le bateau continue-t-il à droite ?
            if list(Grille1[IndexCible][0])[0]+20 <= 485: #Il y a-t-il une case à droite ?
                CaseCible =  Grille1[IndexCible+1]
                if CaseCible[2] == 0:
                    Grille1[IndexCible+1][2] = 1 #On touche la case
                    print("IndexCase = " + str(IndexCible+1))
                    print("Case: " + str(CaseCible))
                    print("Bateau ?: " + str(CaseCible[1]))
                    Code = Dico_IA[CaseCible[0]]
                    print(Code)
                    if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                        #On affiche touché et on place un carrée rouge
                        print("TOUCHE")
                        fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        NbAttaque = NbAttaque +1
                        IndexCible = IndexCible +1 #cible prochain tour
                        Tour = True
                    else:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("DANS L'EAU")
                        fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                        #Plus de bateau à droite: on continue à gauche pour le prochain tour
                        droite = False
                        gauche = True
                        IndexCible = FirstCase #On revient à la première case
                        Tour = True
                else:
                    IndexCible = FirstCase #Déjà touché ? Alors c'était dans l'eau
                    droite = False
                    gauche = True
            else: #Plus de case à droite: le bateau continue donc à gauche
                droite = False
                gauche = True 
                IndexCible = FirstCase #On revient à la première case
        elif gauche == True: #Le bateau continue-t-il à gauche ?
            if list(Grille1[IndexCible][0])[0]-20 >= 105: #Il y a-t-il une case à gauche ?
                CaseCible =  Grille1[IndexCible-1]
                if CaseCible[2] == 0:
                    Grille1[IndexCible-1][2] = 1 #On touche la case
                    print("IndexCase = " + str(IndexCible-1))
                    print("Case: " + str(CaseCible))
                    print("Bateau ?: " + str(CaseCible[1]))
                    Code = Dico_IA[CaseCible[0]]
                    print(Code)
                    if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                        #On affiche touché et on place un carrée rouge
                        print("TOUCHE")
                        fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        NbAttaque = NbAttaque +1
                        IndexCible = IndexCible -1
                        Reference = CaseCible
                        Tour = True
                    else:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("DANS L'EAU")
                        fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                        #Plus de bateau à droite: on continue à gauche pour le prochain tour
                        droite = True
                        gauche = False
                        IndexCible = FirstCase #On revient à la première case
                        Tour = True
                else:
                    IndexCible = FirstCase #Déjà touché ? Alors c'était dans l'eau
                    droite = True
                    gauche = False
            else: #Plus de case à gauche: le bateau continue donc à droite
                droite = True
                gauche = False
                IndexCible = FirstCase #On revient à la première case
        elif haut == True: #Le bateau continue-t-il en haut ?
            if list(Grille1[IndexCible][0])[1]-20 >= 105: #Il y a-t-il une case en haut ?
                CaseCible =  Grille1[IndexCible-20]
                if CaseCible[2] == 0:
                    Grille1[IndexCible-20][2] = 1 #On touche la case
                    print("IndexCase = " + str(IndexCible-20))
                    print("Case: " + str(CaseCible))
                    print("Bateau ?: " + str(CaseCible[1]))
                    Code = Dico_IA[CaseCible[0]]
                    print(Code)
                    if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                        #On affiche touché et on place un carrée rouge
                        print("TOUCHE")
                        fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        NbAttaque = NbAttaque +1
                        IndexCible = IndexCible -20
                        Reference = CaseCible
                        Tour = True
                    else:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("DANS L'EAU")
                        fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                        #Plus de bateau à droite: on continue à gauche pour le prochain tour
                        bas = True
                        haut = False
                        IndexCible = FirstCase #On revient à la première case
                        Tour = True
                else:
                    IndexCible = FirstCase #Déjà touché ? Alors c'était dans l'eau
                    bas = True
                    haut = False
            else: #Plus de case en haut: le bateau continue donc en bas
                bas = True
                haut = False
                IndexCible = FirstCase #On revient à la première case
        elif bas == True: #Le bateau continue-t-il en bas ?
            if list(Grille1[IndexCible][0])[1]+20 <= 485: #Il y a-t-il une case en haut ?
                CaseCible =  Grille1[IndexCible+20]
                if CaseCible[2] == 0: #La case est-elle déjà touché ?
                    Grille1[IndexCible+20][2] = 1 #On touche la case
                    print("IndexCase = " + str(IndexCible+20))
                    print("Case: " + str(CaseCible))
                    print("Bateau ?: " + str(CaseCible[1]))
                    Code = Dico_IA[CaseCible[0]]
                    print(Code)
                    if CaseCible[1] == 1: #Il y a-t-il un bateau ?
                        #On affiche touché et on place un carrée rouge
                        print("TOUCHE")
                        fenetre.blit(CroixRouge, CaseCible[0]) #Placement croix
                        fenetre.blit(TextTOUCHE, (258, 530)) #Affichage du texte "Touché" sur le plateau
                        NbAttaque = NbAttaque +1
                        IndexCible = IndexCible +20
                        Tour = True
                    else:
                        #On affiche dans l'eau et on place un carrée bleu
                        print("DANS L'EAU")
                        fenetre.blit(RondBleu, CaseCible[0])  #Placement rond
                        fenetre.blit(TextEAU, (258, 530)) #Affichage du texte "Dans l'eau" sur le plateau 
                        #Plus de bateau à droite: on continue à gauche pour le prochain tour
                        haut = True
                        bas = False
                        IndexCible = FirstCase #On revient à la première case
                        Tour = True
                else:
                   IndexCible = FirstCase #Déjà touché ? Alors c'était dans l'eau 
                   haut = True
                   bas = False
            else: #Plus de case en bas: le bateau continue donc en haut
                haut = True
                bas = False
                IndexCible = FirstCase #On revient à la première case
    if NbAttaque == NbCoulIANavire:
        InAttaque = False
        print("COULE")
        fenetre.blit(TextCOULE, (414, 530)) #Affichage du texte "Touché" sur le plateau
        Fonction_Ckeck_Coulage_Fin() #pour considérer comme touché toutes les cases adjacentes au navires
        NbCoulIA = NbCoulIA+1 #+ 1 navire coulé, la victoire est proche...

def CountNbCoulIANavire(Grille1, IndexCible): #Fonction qui ressort le nombre de case du navire touché (d'après la fonction "coulage" de Mickaël)
    global NbCoulIANavire
    liste = [] #Liste des index des cases qui vont devoir être vérifiées (touché ou non)
    #Début des vérifications case par case si il y a un bateau ou non
    #De un en un pour les cases horizontales
    #De vingt en vingt pour les cases verticales
    CoordCible = list(Grille1[IndexCible][0]) #Transforme les coordonnées de l'IndexCible en liste pour être exploitées
    if CoordCible[0] != 605 : #Vérifie la colonne de l'IndexCible
        if Grille1[IndexCible-1][1] == 1 : #Vérification si il y a un bateaux
            a = IndexCible-1 #Variable de l'index de la case
            liste.append(a) #Rajout de cette variable dans la liste des index
            if CoordCible[0] != 625 :
                if Grille1[IndexCible-2][1] == 1 :
                    b = IndexCible-2
                    liste.append(b)
                    if CoordCible[0] != 645 :
                        if Grille1[IndexCible-3][1] == 1 :
                            c = IndexCible-3
                            liste.append(c)
                            if CoordCible[0] != 665 :
                                if Grille1[IndexCible-4][1] == 1 :
                                    d = IndexCible-4
                                    liste.append(d)
                                    if CoordCible[0] != 685 :
                                        if Grille1[IndexCible-5][1] == 1 :
                                            e = IndexCible-5
                                            liste.append(e)
    if CoordCible[0] != 985 :
        if Grille1[IndexCible+1][1] == 1 :
            a = IndexCible+1
            liste.append(a)
            if CoordCible[0] != 965 :
                if Grille1[IndexCible+2][1] == 1 :
                    b = IndexCible+2
                    liste.append(b)
                    if CoordCible[0] != 945 :
                        if Grille1[IndexCible+3][1] == 1 :
                            c = IndexCible+3
                            liste.append(c)
                            if CoordCible[0] != 925 :
                                if Grille1[IndexCible+4][1] == 1 :
                                    d = IndexCible+4
                                    liste.append(d)
                                    if CoordCible[0] != 905 :
                                        if Grille1[IndexCible+5][1] == 1 :
                                            e = IndexCible+5
                                            liste.append(e)
    if CoordCible[1] != 105 : #Teste de la ligne pour CoordCible[1]
        if Grille1[IndexCible-20][1] == 1 :
            a = IndexCible-20
            liste.append(a)
            if CoordCible[1] != 125 :
                if Grille1[IndexCible-40][1] == 1 :
                    b = IndexCible-40
                    liste.append(b)
                    if CoordCible[1] != 145 :
                        if Grille1[IndexCible-60][1] == 1 :
                            c = IndexCible-60
                            liste.append(c)
                            if CoordCible[1] != 165 :
                                if Grille1[IndexCible-80][1] == 1 :
                                    d = IndexCible-80
                                    liste.append(d)
                                    if CoordCible[1] != 185 :
                                        if Grille1[IndexCible-100][1] == 1 :
                                            e = IndexCible-100
                                            liste.append(e)
    if CoordCible[1] != 485 :
        if Grille1[IndexCible+20][1] == 1 :
            a = IndexCible+20
            liste.append(a)
            if CoordCible[1] != 465 :
                if Grille1[IndexCible+40][1] == 1 :
                    b = IndexCible+40
                    liste.append(b)
                    if CoordCible[1] != 445 :
                        if Grille1[IndexCible+60][1] == 1 :
                            c = IndexCible+60
                            liste.append(c)
                            if CoordCible[1] != 425 :
                                if Grille1[IndexCible+80][1] == 1 :
                                    d = IndexCible+80
                                    liste.append(d)
                                    if CoordCible[1] != 405 :
                                        if Grille1[IndexCible+100][1] == 1 :
                                            e = IndexCible+100
                                            liste.append(e)
    #print("liste index coulage: " + str(liste)) #print pour test. Désactivé car trop avantageant pour le joueur   
    NbCoulIANavire = len(liste)+1 #le nombre de case est égale au nombre de terme de la liste + 1 pour la case de référence 
    #print(" Navire de " + str(NbCoulIANavire) + " cases") #Désactivé car trop avantageant pour le joueur    

def Fonction_Ckeck_Coulage_Fin():
    #On globalise les variables
    global Grille1
    global bas
    global haut
    global gauche
    global droite
    global NbCoulIANavire
    global Reference
    j = Grille1.index(Reference) #J permet de manipuler IndexCase sans le modifier lui même
    print("DEBUT CHECK COULAGE DU NAVIRE")
    print("IndexCase = " + str(j))
    print("1er case: " + str(Reference))
    #Variable Bolléenne qui détermine si il existe des cases en dessous/dessus/droite/gauche 
    #de la case choisi (on part du principe que "oui"), True = la (les) case(s) existe(nt)
    #Variable qui détermine le sens du navire (Horizontale/Verticale)
    TupleCoord = list(Grille1[j][0])
    case_dessus = True
    case_dessous = True
    case_gauche = True
    case_droite = True
    #détermination des cases existante (quatre test)
    #Si les test sont "Vrais", alors les cases en question n'existent pas
    if TupleCoord[0]-20 < 105: #Y a-t-il une case à gauche ?
        case_gauche = False
    if TupleCoord[0]+20 > 485: #Y a-t-il une case à droite ?
        case_droite = False
    if TupleCoord[1]+20 > 485: #Y a-t-il une case en dessous ?
        case_dessous = False
    if TupleCoord[1]-20 < 105: #Y a-t-il une case au dessus ?
        case_dessus = False
                    
    #Travail sur les cases du dessus (si elles existent):
    if case_dessus == True: #Cases supérieures
        print("passage --> case dessus")
        Grille1[j-20][2] = 1 #On touche la case
        if case_droite == True: #Case supérieure droite (diagonale)
            print("passage --> case dessus droite")
            Grille1[j-19][2] = 1 #On touche la case
        if case_gauche == True: #Case  supérieure gauche (diagonale)
            print("passage --> case gauche")
            Grille1[j-21][2] = 1 #On touche la case 
        
    #Travail sur les cases du dessous (si elles existent):        
    if case_dessous == True: 
        print("passage --> case dessous")
        if case_droite == True: #Case inférieure droite (diagonale)
            print("passage --> case dessous droite")
            Grille1[j+21][2] = 1 #On touche la case
        if case_gauche == True: #Case inférieure gauche (diagonale)
            print("passage --> case dessous gauche")
            Grille1[j+19][2] = 1 #On touche la case
        if Grille1[j+20][1] == 1: #Case immédiatement au dessous 
            Grille1[j+20][2] = 1  #On touche la case                          
            
    #Travail sur la case à gauche (si elle existe):          
    if case_gauche == True:
        print("passage --> case gauche")
        Grille1[j-1][2] = 1 #On touche la case
    #Travail sur la case à droite (si elle existe):        
    if case_droite == True:
        print("passage --> case droite")
        if Grille1[j+1][1] == 1: #Case immédiatement à droite
            Grille1[j+1][2] = 1  #On touche la case                        
                
    #Détermination du type de navire (Horizontale/Verticale) à l'aide des variable H/V:                   
    if droite == True or gauche == True: #Le bateau est-il Horizontal ?
        #La technique utilisé pourra être réutiliser pour la programme "Coulage des Navires" de l'IA
        print("Check_Coulage_NavireH")                        
        Check_Coulage_NavireH(j, case_dessus, case_dessous)
    elif bas == True or haut == True: #Le bateau est-il Verticale ?
        #La technique utilisé pourra être réutiliser pour la programme "Coulage des Navires" de l'IA
        print("Check_Coulage_NavireV")                        
        Check_Coulage_NavireV(j, case_gauche, case_droite)
    print("FIN CHECK COULAGE DU NAVIRE") #Utile à savoir
    
def Check_Coulage_NavireH(j, case_dessus, case_dessous): #Spécifique aux navires horizontaux
    #on globalise les variables
    global Grille1
    global droite
    global gauche
    global Reference
    global NbCoulIANavire
    x = 1
    for x in range (NbCoulIANavire-1): #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        j = j+1
        print("Case: " + str(Grille1[j]))
        print("Index: " + str(j))             
        #La case suivante appartient t'elle au bateau ?
        Grille1[j][2] = 1 #On check la Case
        if case_dessus == True: #On vérifie que la case au dessus existe...
            Grille1[j-20][2] = 1 #On n'oublie pas de checker la Case 
        if case_dessous == True:  #On vérifie que la case en dessous existe...
            Grille1[j+20][2] = 1 #On n'oublie pas de checker la Case
    #Partie qui se fait une fois toutes les cases du navires ckeckées (on va sur les celles juste après)
    if list(Grille1[j+1][0])[0] <= 485: #Y a-t-il une case deux cases à droite ?
        j = j+1        
        Grille1[j][2] = 1 #On check la Case
        if case_dessus == True: #On vérifie que la case au dessus existe...
            Grille1[j-20][2] = 1 #On n'oublie pas de checker la Case 
        if case_dessous == True:  #On vérifie que la case en dessous existe...
            Grille1[j+20][2] = 1 #On n'oublie pas de checker la Case
    
def Check_Coulage_NavireV(j, case_gauche, case_droite): #Spécifique aux navires verticaux
    #on globalise les variables
    global Grille1
    global bas
    global haut
    global Echec
    global Reference
    global NbCoulIANavire
    x = 1
    for x in range (NbCoulIANavire-1): #La boucle tourne tant que l'on est pas arrivé à la fin du bateau
        j = j+20        
        print("Case: " + str(Grille1[j]))
        print("Index: " + str(j)) 
        Grille1[j][2] = 1 #On check la Case
        if case_gauche == True: #On vérifie que la case au dessus existe...
            Grille1[j-1][2] = 1 #On n'oublie pas de checker la Case 
        if case_droite == True:  #On vérifie que la case en dessous existe...
            Grille1[j+1][2] = 1 #On n'oublie pas de checker la Case
    #Partie qui se fait une fois toutes les cases du navires ckeckées (on va sur les celles juste après)
    if j+20 < len(Grille1): #Y a-t-il une case deux cases en dessous ?
        j = j+20
        Grille1[j][2] = 1 #On check la Case
        if case_gauche == True: #On vérifie que la case au dessus existe...
            Grille1[j-1][2] = 1 #On n'oublie pas de checker la Case 
        if case_droite == True:  #On vérifie que la case en dessous existe...
            Grille1[j+1][2] = 1 #On n'oublie pas de checker la Case