try:
    # accès à une partie critique d'un code
    f = open("file.txt")
    try:
        f.write("ecrire une phrase")
    except:
        print("L'ecriture na pas fonctioné")
    finally:
        f.close()
except:
    print("L'ouverture du fichier n'a pas fonctionnée")


print("Fin du programme")