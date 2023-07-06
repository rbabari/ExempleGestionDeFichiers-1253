import os
# 1- Écrire dans un sous repertoire

chemin = "C:\\Users\\" + os.getlogin() +"\\PycharmProjects\\ExempleGestionDeFichiers\\"
#  / sur linux au lieu \\
nomFichier = chemin + "monFichier.txt"
print(nomFichier)
# Chemins relatif
# . dossier actuel
# .. dossier parent
chemin2 = "./dossier/"

print("==>" + os.getcwd())
if not os.path.exists(chemin2):
    os.mkdir(chemin2)

nomFichier = chemin2 + "monFichier3.txt"
f =open(nomFichier, 'w')
contenu = f.write("Bonjour.....")
f.close()


