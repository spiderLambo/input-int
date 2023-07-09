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


rep = 22
rep = inputInt(rep, "2")
print(rep, type(rep))
