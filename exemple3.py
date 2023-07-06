import os
# 1- Écrire en mode ajout

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

nomFichier = chemin2 + "monFichier.txt"
f =open(nomFichier, 'a')
f.write("\n ligne a ajouter")

f.write("\n")
for i in range(10):
    f.write(str(i) + "\n")

f.close()


