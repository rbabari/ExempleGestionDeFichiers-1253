import os
# 1- Écrire dans un fichier

chemin = "C:\\Users\\" + os.getlogin() +"\\PycharmProjects\\ExempleGestionDeFichiers\\"
#  / sur linux au lieu \\
nomFichier = chemin + "monFichier.txt"
print(nomFichier)
f =open(nomFichier, 'w')
contenu = f.write("Bonjour...")
f.close()


