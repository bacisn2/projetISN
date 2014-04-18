# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 17:37:59 2014

@author: IG 158
"""
#NOTE A L'ATTENTION DU PROFESSEUR D'ISN:
#Certains "print" (dans ce programme ou les sous programmes) n'affiche pas des textes 
#mais des variables. Ils me servent à vérifier le bon fonctionnement du programme 
#(notamment l'état de la variable "Bateau/pas Bateau" invisible sur le plateau de jeu)

#NOTE UTILE SUR LES GRILLES DE JEU:
#Chaque Grille fait 400*400 px et chaque case fait 20*20 px. La première Grille est
#émargé à 100 px en haut et 100 px à droite et la deuxième Grille est émargé à 100 px
#en haut et 600 px à gauche, les coordonnées des cases de ces Grilles doient donc tenir
#compte de ces marges. Les bateaux font moins de 20 px de haut (ou de large pour les
#verticaux) et sont donc placé à 5 px de marge du coin supérieur gauche de la case.

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
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
#obligé d'initialiser une fenêtre pour faire fonctionner le pygame.image.load
fenetre = pygame.display.set_mode((1200, 900)) 
#FONCTION REINITIALISATION:
def REINITIALISATION_PARTIE():
    global CountShip
    global EchecVerifFinal
    global Grille1
    global Grille2
    global TourJoueur
    global TourIA
    global Initialisation
    #réinitialisation des variables de début utile
    Reinitialisation_NbXCase()
    CountShip = 0
    EchecVerifFinal = False
    TourJoueur = False
    TourIA = False
    Initialisation = True           
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
    #Placement des Textes sur le Plateau de Jeu
    fenetre.blit(Instr1, (100,580))
    fenetre.blit(Instr2, (100,595))
    fenetre.blit(Instr3, (450,595))
    fenetre.blit(Instr4, (100,610))
    fenetre.blit(Instr5, (450,610))
    fenetre.blit(Instr6, (100,625))
    fenetre.blit(Instr7, (450,625))
    fenetre.blit(Instr8, (100,640))
    fenetre.blit(Instr9, (450,640))
    fenetre.blit(Instr10, (100,655))
    fenetre.blit(Instr11, (100,670))
    pygame.display.flip()
#FIN FONCTION REINITIALISATION


#FONCTION TEST POSITION IA
#Fonction qui affiche la position des navires de l'IA une fois son placement terminé
#Son but a uniquement un test, elle sera supprimée sur la version final
def Fonction_Test_Pose_IA():
    global Grille2
    i = 0
    for i in range (400): #on test toutes les cases une part une
        if Grille2[i][1] == 1: #test présence d'un navire
          fenetre.blit(CarRouge, Grille2[i][0])  #Placement carrée rouge
        else:
          fenetre.blit(CarBleu, Grille2[i][0])  #Placement carrée bleu
    pygame.display.flip() #on rafarîchit le plateau pour afficher les carrées

def testcroix_rond():
    global CaseIA
    x = 0
    for x in range (len(CaseIA)): #permet de tester la liste de cases de l'IA
        if CaseIA[x][1] == 1: #test présence d'un navire
            fenetre.blit(CroixRouge, CaseIA[x][0])  #Placement croix
        else:
          fenetre.blit(RondBleu, CaseIA[x][0])  #Placement rond
    pygame.display.flip() #on rafarîchit le plateau pour afficher les carrées
#FIN FONCTION TEST POSITION IA

     
#PARTIE INItIALISATION DU JEU
#Ini Pygame + fond pour les textes
pygame.init()
pygame.font.init()
Info = pygame.font.Font(None, 20) #Transparent pour l'affichage des Textes (version 15 px)
font = pygame.font.Font(None, 30) #Transparent pour l'affichage des Textes (version 30 px)
SuperFont = pygame.font.Font(None, 80) #Transparent pour l'affichage des Textes (version 80 px)

#Ini des Grilles (on joue les fonctions puis on importe les grilles créees ainsi)
IniListeCaseGrille1()
IniListeCaseGrille2()
from Fonction_Ship import Grille1
from Fonction_Ship import Grille2
    
#Ini Fenêtre + Fond Blanc
#Crée une fenêtre de 1200*900 pixel pour le Jeu
fenetre = pygame.display.set_mode((1200, 700))
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

#Chargement des carrées et croix pour le jeu (mais aucun placement pour le moment)
CarRouge = pygame.image.load("Carree_Rouge.png")
CarBleu = pygame.image.load("Carree_Bleu.png")
RondBleu = pygame.image.load("rond.png").convert_alpha()
CroixRouge = pygame.image.load("Croix.png").convert_alpha()

#Importation Dicos + Initialisation Compteurs
CasePlayer1 = Dico_Grille1.GrillePlayer1
BateauPlayer = Dico_Ship.Ship1
Infinie = 1 #Fait tourner indéfiniment le programme
CountShip = 0 #Compteur Navires
EchecVerifFinal = False
Initialisation = True
TourJoueur = False
TourIA = False

#Liste des commandes pour le début
#Création des Textes
TextD1 = "Il y a 9 navires possibles, chacun possede un code propre que voici pour facilite leur saisi:"
TextD2 = "Voilier (2 cases) --> Code: \"Voilier\""
TextD3 = "Destroyer (2 cases) --> Code: \"LitShip\""
TextD4 = "Sous-Marin (3 cases) --> Code: \"SM\""
TextD5 = "Mini-Navire version Bleue (3 cases) --> Code: \"MNB\""
TextD6 = "Mini-Navire version Rouge (3 cases) --> Code: \"MNR\""
TextD7 = "Cuirasse Standard (4 cases) --> Code: \"CuirBase\""
TextD8 = "Cuirasse Version 2 (4 cases) --> Code: \"Cuir2\""
TextD9 = "Porte Avion (5 cases) --> Code: \"PA\""
TextD10 = "Super Cuirasse (6 cases) --> Code: \"CuirSuper\""
TextD11 = "Ces codes placent vos bateaux de maniere horizontal, pour les placer verticalement, rajouter \"V\" apres les codes ci-dessus"
#Chargement des Textes
Instr1 = Info.render(TextD1, 1, (0,0,0))
Instr2 = Info.render(TextD2, 1, (0,0,0))
Instr3 = Info.render(TextD3, 1, (0,0,0))
Instr4 = Info.render(TextD4, 1, (0,0,0))
Instr5 = Info.render(TextD5, 1, (0,0,0))
Instr6 = Info.render(TextD6, 1, (0,0,0))
Instr7 = Info.render(TextD7, 1, (0,0,0))
Instr8 = Info.render(TextD8, 1, (0,0,0))
Instr9 = Info.render(TextD9, 1, (0,0,0))
Instr10 = Info.render(TextD10, 1, (0,0,0))
Instr11 = Info.render(TextD11, 1, (0,0,0))
#Placement des Textes sur le Plateau de Jeu
fenetre.blit(Instr1, (100,580))
fenetre.blit(Instr2, (100,595))
fenetre.blit(Instr3, (450,595))
fenetre.blit(Instr4, (100,610))
fenetre.blit(Instr5, (450,610))
fenetre.blit(Instr6, (100,625))
fenetre.blit(Instr7, (450,625))
fenetre.blit(Instr8, (100,640))
fenetre.blit(Instr9, (450,640))
fenetre.blit(Instr10, (100,655))
fenetre.blit(Instr11, (100,670))
#Raifraichissement du Plateau de Jeu
pygame.display.flip()
#FIN PARTIE INITIALISATION DU JEU

#MAIN PROGRAMME
from Search_Ship_IA import *         
while Infinie == 1:
    for event in pygame.event.get(): #Fait la liste des évènements possible (appuyer sur une touche, souris, etc...)
        if event.type == QUIT: #Quitte la partie quand on appuie sur "Quitter" (bug sous Windows 8 avec Python 2.7)
            Infinie = 0 #Fin de la Boucle (FIN MAIN PROGRAMME)
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
            
        #Placement navire (joueur puis IA) + vérification position joueur
        if event.type == KEYDOWN and event.key == K_SPACE and Initialisation == True:
            #Placement des bateau en jeu
            if CountShip < 10:
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
                    #print("\n")
                    #print("Nouvelle Grille1")
                    #print(Grille1)
                    print("Nombre de Bateaux: " + str(CountShip))
                    print("Appuyez sur \"b\" pour placer un nouveau navire ou \nlancer la verification de votre positionnement")
                    print("\n")
            else: #Une fois les dix navires posés
                from Fonction_Ship import Nb2Case
                from Fonction_Ship import Nb3Case
                from Fonction_Ship import Nb4Case
                from Fonction_Ship import Nb5Case
                from Fonction_Ship import Nb6Case
                if Nb2Case == 3 and Nb3Case == 3 and Nb4Case == 2 and Nb5Case == 1 and Nb6Case == 1:
                    print("OK pour la liste de navires")
                    EchecVerifFinal = False
                    Verification_Final_Grille1()
                    from Fonction_Ship import Echec
                    if Echec == True:
                        EchecVerifFinal = True
                    else: #Passage au placement de l'IA
                        print("Verifiction termine, aucun probleme detecte, \nl'IA pose ses navires et la partie peut commencer")
                        print("\nPositionnement des navires de l'IA en cours. \nMerci de patientez quelques instants...")
                        IA_Pose_Bat()#Appelle Fonction IA_Pose_Bat
                        Initialisation = False #Empêche le replacement des navires de l'IA une fois la partie lancée
                        Fonction_Test_Pose_IA() #Appelle Fonction test (suppression pour la version finale)
                        Define_List_Case_and_Strategie() #création CaseIA + choix stratégie (= fin Initialisation)
                        print("\nPlacement de l'IA terminé, c'est à vous de commencer")
                        Initialisation = False
                        TourIA = True
                else:
                    print("Vous n'avez pas respecte la liste de navire requit\nVeuillez recommencer")
                    EchecVerifFinal = True
        
        #Tours de jeu
        if TourIA == True: #Tour de l'IA
            from Search_Ship_IA import CaseIA
            #testcroix_rond() #test CaseIA + affichage croix et rond
            Search_Ship(fenetre, CasePlayer1)            
            #Passage tour du Joueur
            TourIA = False
            TourJoueur = True
            raw_input("Tour Suivant ?")
            
        if TourJoueur == True: #Tour du Joueur
            #Passage tour de l'IA
            TourIA = True
            TourJoueur = False    
            
        #réinitialisation du plateau
        if event.type == KEYDOWN and event.key == K_UP :
            #Demande de confirmation
            RealQuit = raw_input("Vous-vous vraiment reinitialiser la partie ? (o/n): ")
            if RealQuit == "o":          
                REINITIALISATION_PARTIE()
                #Message Réinitialisation
                print("Reinitialisation de la partie")
            else:
                print("Reinitialisation annulee")
        if EchecVerifFinal == True:
            REINITIALISATION_PARTIE()
            print("Appuyez sur \"b\" pour recommencer la saisi")
#FIN MAIN PROGRAMME
raw_input() #attend une action du joueur pour fermé le programme (nécessaire sous Python 2.7 pour éviter les sorties trop brutales)