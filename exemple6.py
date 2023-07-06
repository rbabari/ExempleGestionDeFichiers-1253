import os
# 6- Lire depuis un fichier ligne par ligne avec readlines
tabLignes = []

chemin = "./dossier/"
nomFichier = chemin + "monFichier.txt"

if os.path.isfile(nomFichier):
    print("fichier existe")
    f = open(nomFichier, 'r')
    tabLignes = f.readlines()
# print(tabLignes)

for ligne in tabLignes:
    print(ligne, end='\b')  # \b pour supprimer le dernier caractère
print("nombre de lignes : ", len(tabLignes))


f.close()




