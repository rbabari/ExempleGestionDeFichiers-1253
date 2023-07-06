import os
import csv
# 7- utiliser csv ? mettre dans un dictionnaire

chemin = "./dossier/"
nomFichier = chemin + "monFichier2.txt"
nomChamps = ["prenom","nom","age","da"]
f = open(nomFichier, 'r')
r = csv.DictReader(f, delimiter=';')

for ligne in r:
   print(ligne)

f.close()