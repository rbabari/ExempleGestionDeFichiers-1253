import os
# 5- Lire depuis un fichier ligne par ligne avec readline
# CSV permet de representer nos enregistrement dans un tableau excel
# Etudiant : champs_nom | champs_prenom | champs_age | champs_da
#enregistrement_1 | nabil | agsous | 21 | 1234342
#enregistrement_2 | bachir | haji | 21 | 1234342
#enregistrement_3 | gael | eeee | 21 | 1234342
#enregistrement_4 | erika | qqeq | 21 | 1234342

tabLignes = []

chemin = "./dossier/"
nomFichier = chemin + "monFichier.txt"

if os.path.isfile(nomFichier):
    print("fichier existe")
    f = open(nomFichier, 'r')
    while 1:
        ligne = f.readline()
        if ligne == "":
            break
        tabLignes.append(ligne)
f.close()

print("==>>> " + tabLignes[0])
print(tabLignes[1])
print(tabLignes[2])


