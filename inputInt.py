def input_int(question, nombre_de_lignes=2):
    p = True
    b = True
    while p:
        while b:
            if nombre_de_lignes == 1:
                a = input(question)
                b = False
            elif nombre_de_lignes == 2:
                print(question)
                a = input()
                b = False
            else:
                print("Le deusieme parametre est invalide")
        try:
            int(a)
            p = False
        except:
            print("Choisir un nombre entier")
    return int(a)


def input_float(question, nombre_de_lignes=2):
    p = True
    b = True
    while p:
        while b:
            if nombre_de_lignes == 1:
                a = input(question)
                b = False
            elif nombre_de_lignes == 2:
                print(question)
                a = input()
                b = False
            else:
                print("Le deusieme parametre est invalide")
        try:
            float(a)
            p = False
        except:
            print("Choisir un nombre entier")
    return float(a)