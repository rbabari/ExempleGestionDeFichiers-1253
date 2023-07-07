vaRefaire = True
while vaRefaire:
    vaRefaire = False
    a = input("svp nombre strictement positif : ")
    try:
        a_num = int(a)
        try:
            resultat = 1000 / a_num
        except:
            print(" :( division par zéro")
            vaRefaire = True
    except:
        print(": ( format non accepté")
        vaRefaire = True

print(resultat)



