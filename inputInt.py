def input_int(question, nombre_de_lignes=2):
    p,b = True,True
    while p:
        while b:
            if nombre_de_lignes == 1:
                a,b = input(question),False
            elif nombre_de_lignes == 2:
                print(question)
                a,b = input(),False
            else:
                print("Le deuxième parametre est invalide")
                b = False
                input()
                exit()
        try:
            return int(a)
            p = False
        except:
            print("Choisir un nombre entier")
            b = True


def input_float(question, nombre_de_lignes=2):
    p,b = True,True
    while p:
        while b:
            if nombre_de_lignes == 1:
                a,b = input(question),False
            elif nombre_de_lignes == 2:
                print(question)
                a,b = input(),False
            else:
                print("Le deuxième parametre est invalide")
                b = False
                input()
                exit()
        try:
            return float(a)
            p = False
        except:
            print("Choisir un nombre")
            b = True