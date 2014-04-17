# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:11:16 2014

@author: isn
"""

def TourJoueur():
    global IndexCible
    global grille2
    global cible
    global Dico_Grille2
    global CasePlayer2
    Tir = False
    CasePlayer2 = Dico_Grille2.GrillePlayer2
    print("Choisir une cible")
    while Tir == False :
        cible = raw_input()
        if cible in CasePlayer2 : 
            Fonction_Search_Index_CaseListe_for_Grille2()
            if Grille2[IndexCible][2] == 0 :
                VariableBPB = Grille2[IndexCible][1]
                if VariableBPB == 0 :
                    print("Dans l'eau")
                    fenetre.blit(CarBleu, Grille2[IndexCible][0])
                    Grille2[IndexCible][2] = 1
                else :
                    print("Bateau Touché")
                    fenetre.blit(CarRouge, Grille2[IndexCible][0])
                Tir = True
            else :
                print("Case déjà touché, en choisir une autre")
        else : 
            print("Cette case n'éxiste pas, en choisir une autre")
        pygame.display.flip()
        Tir = False
        
def Fonction_Search_Index_CaseListe_for_Grille2():
    #On globalise toutes les variables
    global Grille2
    global IndexCible
    global CasePlayer2
    j = 0 #On démarre à l'index 0 (A1)
    for j in range (len(Grille2)):
        if Grille2[j][0] == CasePlayer2[Coord]: #Grille2[j][0] = Coord de la "CaseListe"
            IndexCible = j #Index de la Case choisi dans la liste "Grille2"
            print("\n")
            print("IndexCase = " + str(IndexCase))
            break #si on sort du quadrillage, rien de sert de continuer, on quitte la fonction
            