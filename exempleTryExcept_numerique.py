a = input("donne un nombre strictement positif : ")
try:
    a_num = int(a)
    try:
        resultat = 4 / a_num
    except:
        print("division par zéro")
except:
    print("format non accepté")



