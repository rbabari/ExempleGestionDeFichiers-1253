import os
import csv
# 7- utiliser csv ?

chemin = "./dossier/"
nomFichier = chemin + "monFichier2.txt"

f = open(nomFichier, 'r')
r = csv.reader(f, delimiter=';')
nomChamps = ["prenom","nom","age","da"]
matrice = [] # est un tableau de tableaux ...

for ligne in r:
   matrice.append(ligne)
   for i in range(len(ligne)):
        print(nomChamps[i] + "=  "+ ligne[i])
   print("===========")


print(matrice[2][3])