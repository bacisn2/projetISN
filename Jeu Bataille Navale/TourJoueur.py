# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:11:16 2014

@author: isn
"""
#import Dico_Ship
import Dico_Grille2
#from Coulage import *
from Fonction_Ship import Grille2
#import random
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
    print("NbCoul debut TourJoueur = " + str(NbCoul))
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
                    Coulage(Grille2, IndexCible)#, NbCoulInterm
                    print("NbCoul in TourJoueur = " + str(NbCoul))
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

def Coulage(Grille2, IndexCible):#, NbCoulInterm) :
    global NbCoul
    liste = [] #Liste des index des cases qui vont devoir être vérifiées (touché ou non)
    x = 0 #Variable pour le parcourt de la liste des index
    z = 0 #Variable du nombre de case avec bateau qui sont touchées
    #Début des vérifications case par case si il y a un bateau ou non
    #De un en un pour les cases horizontales
    #De vingt en vingt pour les cases verticales
    if Grille2[IndexCible-1][1] == 1 : #Vérification si il y a un bateaux
        a = IndexCible-1 #Variable de l'index de la case
        liste.append(a) #Rajout de cette variable dans la liste des index
        if Grille2[IndexCible-2][1] == 1 :
            b = IndexCible-2
            liste.append(b)
            if Grille2[IndexCible-3][1] == 1 :
                c = IndexCible-3
                liste.append(c)
                if Grille2[IndexCible-4][1] == 1 :
                    d = IndexCible-4
                    liste.append(d)
                    if Grille2[IndexCible-5][1] == 1 :
                        e = IndexCible-5
                        liste.append(e)
    if Grille2[IndexCible+1][1] == 1 :
        a = IndexCible+1
        liste.append(a)
        if Grille2[IndexCible+2][1] == 1 :
            b = IndexCible+2
            liste.append(b)
            if Grille2[IndexCible+3][1] == 1 :
                c = IndexCible+3
                liste.append(c)
                if Grille2[IndexCible+4][1] == 1 :
                    d = IndexCible+4
                    liste.append(d)
                    if Grille2[IndexCible+5][1] == 1 :
                        e = IndexCible+5
                        liste.append(e)
    if Grille2[IndexCible-20][1] == 1 :
        a = IndexCible-20
        liste.append(a)
        if Grille2[IndexCible-40][1] == 1 :
            b = IndexCible-40
            liste.append(b)
            if Grille2[IndexCible-60][1] == 1 :
                c = IndexCible-60
                liste.append(c)
                if Grille2[IndexCible-80][1] == 1 :
                    d = IndexCible-80
                    liste.append(d)
                    if Grille2[IndexCible-100][1] == 1 :
                        e = IndexCible-100
                        liste.append(e)
    if Grille2[IndexCible+20][1] == 1 :
        a = IndexCible+20
        liste.append(a)
        if Grille2[IndexCible+40][1] == 1 :
            b = IndexCible+40
            liste.append(b)
            if Grille2[IndexCible+60][1] == 1 :
                c = IndexCible+60
                liste.append(c)
                if Grille2[IndexCible+80][1] == 1 :
                    d = IndexCible+80
                    liste.append(d)
                    if Grille2[IndexCible+100][1] == 1 :
                        e = IndexCible+100
                        liste.append(e)
    #Début des vérifications case par case si il y a un bateau ou non
    print "liste index coulage :" #print pour test
    print liste #print pour test
    while x < len(liste) : #Boucle avec incrémentation de x jusqu'au nombre d'élément dans la liste
        if Grille2[liste[x]][2] == 1 : #Vérification si la case a été touchée ou non
            z = z + 1 #Incrémentation de la variable du nombre de case avec bateau qui sont touchées
        x = x + 1 #Incrémentation de x pour le parcourt de la boucle
    if x == z : #Si le nombre de case avec bateau qui sont touchée est égal au nombre de case devant être vérifiée
        print "Coule" #print pour test
        print "NbCoul avant rajout :" + str(NbCoul) #print pour test
        NbCoul = NbCoul + 1
        print "Le nombre de bateau coule est de " + str(NbCoul)            