# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:11:16 2014

@author: isn
"""
#import Dico_Ship
import Dico_Grille2
#from Texte_IA import *
from Fonction_Ship import Grille2
#import random
import random
from Phrases_IA import *
CasePlayer2 = Dico_Grille2.GrillePlayer2 #mit hors de la fonction car unutile de les refaire à chaque fois
NbCoul = 0

def Tour_Joueur(fenetre, CarBleu, CarRouge, TextEAU, TextTOUCHE, TextCOULE, Jeu): 
    #utilisation des arguments pour la fenetre et les carrées
    global IndexCible
    global Grille2
    global cible
    global Dico_Grille2
    global CasePlayer2
    global NbCoul
    #print("NbCoul debut TourJoueur = " + str(NbCoul)) #Inutile à ce stade
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
                    print("DANS L'EAU")
                    fenetre.blit(CarBleu, Grille2[IndexCible][0])
                    fenetre.blit(TextEAU, (758, 530)) #Affichage du texte "Dans l'eau" sur le plateau
                    #a = random.randint(1, 3)
                    #if a == 1 :
                        #TexteJoueurEau()
                else :
                    print("TOUCHE")
                    fenetre.blit(CarRouge, Grille2[IndexCible][0])
                    fenetre.blit(TextTOUCHE, (758, 530)) #Affichage du texte "Touché" sur le plateau
                    Coulage(Grille2, IndexCible, fenetre, TextCOULE)
                    #print("NbCoul in TourJoueur = " + str(NbCoul)) #inutile à ce stade
                Tir = True 
            else : 
                print("CASE DEJA TOUCHE, TIR PERDU")
                Tir = True
        else : 
            print("CETTE CASE N'EXISTE PAS, EN CHOISIR UNE AUTRE")
        
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

def Coulage(Grille2, IndexCible, fenetre, TextCOULE):
    global NbCoul
    liste = [] #Liste des index des cases qui vont devoir être vérifiées (touché ou non)
    x = 0 #Variable pour le parcourt de la liste des index
    z = 0 #Variable du nombre de case avec bateau qui sont touchées
    #Début des vérifications case par case si il y a un bateau ou non
    #De un en un pour les cases horizontales
    #De vingt en vingt pour les cases verticales
    CoordCible = list(Grille2[IndexCible][0]) #Transforme les coordonnées de l'IndexCible en liste pour être exploitées
    if CoordCible[0] != 605 : #Vérifie la colonne de l'IndexCible
        if Grille2[IndexCible-1][1] == 1 : #Vérification si il y a un bateaux
            a = IndexCible-1 #Variable de l'index de la case
            liste.append(a) #Rajout de cette variable dans la liste des index
            if CoordCible[0] != 625 :
                if Grille2[IndexCible-2][1] == 1 :
                    b = IndexCible-2
                    liste.append(b)
                    if CoordCible[0] != 645 :
                        if Grille2[IndexCible-3][1] == 1 :
                            c = IndexCible-3
                            liste.append(c)
                            if CoordCible[0] != 665 :
                                if Grille2[IndexCible-4][1] == 1 :
                                    d = IndexCible-4
                                    liste.append(d)
                                    if CoordCible[0] != 685 :
                                        if Grille2[IndexCible-5][1] == 1 :
                                            e = IndexCible-5
                                            liste.append(e)
    if CoordCible[0] != 985 :
        if Grille2[IndexCible+1][1] == 1 :
            a = IndexCible+1
            liste.append(a)
            if CoordCible[0] != 965 :
                if Grille2[IndexCible+2][1] == 1 :
                    b = IndexCible+2
                    liste.append(b)
                    if CoordCible[0] != 945 :
                        if Grille2[IndexCible+3][1] == 1 :
                            c = IndexCible+3
                            liste.append(c)
                            if CoordCible[0] != 925 :
                                if Grille2[IndexCible+4][1] == 1 :
                                    d = IndexCible+4
                                    liste.append(d)
                                    if CoordCible[0] != 905 :
                                        if Grille2[IndexCible+5][1] == 1 :
                                            e = IndexCible+5
                                            liste.append(e)
    if CoordCible[1] != 105 : #Teste de la ligne pour CoordCible[1]
        if Grille2[IndexCible-20][1] == 1 :
            a = IndexCible-20
            liste.append(a)
            if CoordCible[1] != 125 :
                if Grille2[IndexCible-40][1] == 1 :
                    b = IndexCible-40
                    liste.append(b)
                    if CoordCible[1] != 145 :
                        if Grille2[IndexCible-60][1] == 1 :
                            c = IndexCible-60
                            liste.append(c)
                            if CoordCible[1] != 165 :
                                if Grille2[IndexCible-80][1] == 1 :
                                    d = IndexCible-80
                                    liste.append(d)
                                    if CoordCible[1] != 185 :
                                        if Grille2[IndexCible-100][1] == 1 :
                                            e = IndexCible-100
                                            liste.append(e)
    if CoordCible[1] != 485 :
        if Grille2[IndexCible+20][1] == 1 :
            a = IndexCible+20
            liste.append(a)
            if CoordCible[1] != 465 :
                if Grille2[IndexCible+40][1] == 1 :
                    b = IndexCible+40
                    liste.append(b)
                    if CoordCible[1] != 445 :
                        if Grille2[IndexCible+60][1] == 1 :
                            c = IndexCible+60
                            liste.append(c)
                            if CoordCible[1] != 425 :
                                if Grille2[IndexCible+80][1] == 1 :
                                    d = IndexCible+80
                                    liste.append(d)
                                    if CoordCible[1] != 405 :
                                        if Grille2[IndexCible+100][1] == 1 :
                                            e = IndexCible+100
                                            liste.append(e)
    #Début des vérifications case par case si il y a un bateau ou non
    print("liste index coulage : " + str(liste)) #print pour test
    while x < len(liste) : #Boucle avec incrémentation de x jusqu'au nombre d'élément dans la liste
        if Grille2[liste[x]][2] == 1 : #Vérification si la case a été touchée ou non
            z = z + 1 #Incrémentation de la variable du nombre de case avec bateau qui sont touchées
        x = x + 1 #Incrémentation de x pour le parcourt de la boucle
    if x == z : #Si le nombre de case avec bateau qui sont touchée est égal au nombre de case devant être vérifiée
        print("COULE") #print pour test
        #print("NbCoul avant rajout :" + str(NbCoul)) #print pour test. Inutile à savoir
        NbCoul = NbCoul + 1
        fenetre.blit(TextCOULE, (914, 530)) #Affichage du texte "Touché" sur le plateau
        print("Le nombre de bateau coule est de " + str(NbCoul))            
