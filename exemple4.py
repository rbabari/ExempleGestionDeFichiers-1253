import os
# 4- Lire depuis un fichier

chemin2 = "./dossier/"

nomFichier = chemin2 + "monFichier.txt"

if os.path.isfile(nomFichier):
    print("fichier existe")
    f = open(nomFichier, 'r')
    contenu = f.read()
    print("Le contenu du fichier est : \n", contenu)


