# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:11:16 2014

@author: isn
"""
#import Dico_Ship
import Dico_Grille2
from Fonction_Ship import Grille2
#import random
CasePlayer2 = Dico_Grille2.GrillePlayer2 #mit hors fonction car unutile de les refaire à chaque fois

def Tour_Joueur(fenetre, CarBleu, CarRouge, TextEAU, TextTOUCHE, TextCOULE, Jeu): #utilisation des arguments pour la fenetre et les carrées
    global IndexCible
    global Grille2
    global cible
    global Dico_Grille2
    global CasePlayer2
    Tir = False
    print("Choisir une cible")
    while Tir == False :
        cible = raw_input()
        if cible in CasePlayer2 : 
            Fonction_Search_Index_CaseListe_for_Grille2(cible)
            #Affichage de la Case
            TextCaseBrut = cible
            TextCase = Jeu.render(TextCaseBrut, 1, (0,0,0))
            fenetre.blit(TextCase, (625, 515))
            #Fin affichage de la case
            if Grille2[IndexCible][2] == 0 :
                VariableBPB = Grille2[IndexCible][1]
                if VariableBPB == 0 :
                    print("Dans l'eau")
                    fenetre.blit(CarBleu, Grille2[IndexCible][0])
                    fenetre.blit(TextEAU, (758, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    Grille2[IndexCible][2] = 1
                else :
                    print("Touche")
                    fenetre.blit(CarRouge, Grille2[IndexCible][0])
                    fenetre.blit(TextTOUCHE, (758, 530)) #Affichage du texte "Touché" sur le plateau
                Tir = True #je l'ai mis à True... il était à False
            else : #Ce n'est pas ce qu'il faut faire, le programme doit juste te dire que t'as touché une case
            #déjà touché... pas te faire recommencer gentillement ;)
                print("Case deja touchee, en choisir une autre")
        else : 
            print("Cette case n'existe pas, en choisir une autre")
        Tir = True
        
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
            