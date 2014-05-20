# -*- coding: utf-8 -*-
"""
Created on Sun May 18 15:25:12 2014

@author: IG 158
"""

#Dico permettant d'avoir accès au vingt lettres des codes (A à T) et éviter de les inclure
#directement dans la boucle
DicoLettre = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T"}

def Create_Dico_CaseIA():
    global DicoLettre #On récupère le dictionnaire de lettre
    global Dico_IA #Le Dictionnaire final ne sert pas que pour cette fonction, il est donc globalisé
    x = 105 #absisse
    y = 85 #ordonnée (-1 car incrémenté dès le début de la boucle)
    z = 1 #Numéro de la case
    i = 1 #compteur Nombre de cases
    List_IA = [] #liste intermédiaire à remplir
    for i in range (1, 21): #pour toute la Grille
        x = 105 #on revient à la première colonne
        y = y+20 #ligne suivante
        z = 1 #chiffre correspondant à l'abisse
        lettre = DicoLettre[i] #lettre correspondant à la coordonné
        while z < 21: #pour le 20 premières cases
            xy = (x, y) #création du tuple
            case = lettre + str(z) #création du code lettre chiffre
            List_IA.append((xy, case)) #ajout à la liste sous forme: (Tuple, code)
            z = z+1 #nombre suivant
            x = x+20 #colonne suivante
    Dico_IA = dict(List_IA) #convertion en dictionnaire
    # transforme un argument de type (x, y) en x:y, le premier terme devient la clée et le second la valeur
 

#Create_Dico_CaseIA()       
#print(DicoIA) 
#raw_input("fin")
          