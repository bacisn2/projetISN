# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:11:16 2014

@author: isn
"""
#import Dico_Ship
import Dico_Grille2
from Coulage import *
from Fonction_Ship import Grille2
#import random
CasePlayer2 = Dico_Grille2.GrillePlayer2 #mit hors fonction car unutile de les refaire à chaque fois

def Tour_Joueur(fenetre, CarBleu, CarRouge, TextEAU, TextTOUCHE, TextCOULE, Jeu, NbCoul): 
#utilisation des arguments pour la fenetre et les carrées
    global IndexCible
    global Grille2
    global cible
    global Dico_Grille2
    global CasePlayer2
    Tir = False #Variable limitant le nombre de tir à un
    print("Choisir une cible")
    while Tir == False : 
        cible = raw_input() #Le joueur entre la case qu'il veut cibler
        if cible in CasePlayer2 : #Vérification de l'éxistance de la case
            Fonction_Search_Index_CaseListe_for_Grille2(cible)
            #Affichage de la Case
            TextCaseBrut = cible
            TextCase = Jeu.render(TextCaseBrut, 1, (0,0,0))
            fenetre.blit(TextCase, (625, 515))
            #Fin affichage de la case
            if Grille2[IndexCible][2] == 0 : #Vérification si la case n'a pas déjà été touchée
                Grille2[IndexCible][2] = 1 #La case passe de "non touchée" (=0) à touchée (=1)
                VariableBPB = Grille2[IndexCible][1] #Variable de la présence d'un bateau ou pas
                if VariableBPB == 0 : #Si il n'y a pas de bateau
                    print("Dans l'eau")
                    fenetre.blit(CarBleu, Grille2[IndexCible][0])
                    fenetre.blit(TextEAU, (758, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                else :
                    print("Touche")
                    fenetre.blit(CarRouge, Grille2[IndexCible][0])
                    fenetre.blit(TextTOUCHE, (758, 530)) #Affichage du texte "Touché" sur le plateau
                    Coulage(Grille2, IndexCible, NbCoul)
                Tir = True 
            else : 
                print("Case deja touchee, tir perdue")
                Tir = True
        else : 
            print("Cette case n'existe pas, en choisir une autre")
        
def Fonction_Search_Index_CaseListe_for_Grille2(cible):
    #On globalise toutes les variables
    global Grille2
    global IndexCible
    global CasePlayer2
    j = 0 #On démarre à l'index 0 (A1)
    for j in range (len(Grille2)):
        if Grille2[j][0] == CasePlayer2[cible]: #Grille2[j][0] = Coord de la "CaseListe"
            IndexCible = j #Index de la Case choisi dans la liste "Grille2"
            print("IndexCase = " + str(IndexCible)) #
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            