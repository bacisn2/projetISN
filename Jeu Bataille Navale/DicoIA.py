# -*- coding: utf-8 -*-
"""
Created on Sun May 18 15:25:12 2014

@author: IG 158
"""

DicoLettre = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T"}

def Create_Dico_CaseIA():
    global DicoLettre
    global Dico_IA
    x = 105 #absisse
    y = 85 #ordonné
    z = 1 #Numéro case
    i = 1 #compteur Nb de cases
    List_IA = [] #liste à remplir
    for i in range (1, 21): #pour toute la Grille
        x = 105 #on revient à la première colonne
        y = y+20 #ligne suivante
        z = 1 #chiffre correspondant à l'abisse
        lettre = DicoLettre[i] #lettre correspondant à la coordonné
        while z < 21: #pour le 20 premières cases
            xy = (x, y) #création du tuple
            #print(xy)
            case = lettre+str(z) #création du code chiffre lettre
            #print(case)
            List_IA.append(((xy), case)) #ajout à la liste
            z = z+1 #nombre suivant
            x = x+20 #colonne suivante
    Dico_IA = dict(List_IA) #convertion en dictionnaire
    #print(Dico_IA)
 

#Create_Dico_CaseIA()       
#print(DicoIA) 
#raw_input("fin")
          