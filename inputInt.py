def inputInt(a, b):
    p = True
    while p:
        print(b)
        a = input()
        try:
            int(a)
            p = False
        except:
            print("choisir un nombre entier")
    return int(a)


def inputFloat(a, b):
    p = True
    while p:
        print(b)
        a = input()
        try:
            float(a)
            p = False
        except:
            print("choisir un nombre")
    return float(a)
