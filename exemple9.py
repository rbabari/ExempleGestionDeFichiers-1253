import os
import csv
import pandas as pd
# 7- utiliser csv ? mettre dans un dictionnaire

chemin = "./dossier/"
nomFichier = chemin + "monFichier2.txt"
nomChamps = ["prenom","nom","age","da"]
f = open(nomFichier, 'r')

resultat = pd.read_csv(nomFichier,delimiter=';')

print(resultat.values[2][3])