vaRefaire = True
while vaRefaire:
    vaRefaire = False
    a = input("svp nombre strictement positif : ")
    try:
        a_num = int(a)
        resultat = 1000 / a_num
    except ZeroDivisionError as e:
        print("message : ", e)
        print(type(e))
        vaRefaire = True
    except ValueError as e:
        print("message : ", e)
        print(type(e))
        vaRefaire = True
    except Exception as e:
        print("message : ", e)
        print(type(e))
        vaRefaire = True

print(resultat)



