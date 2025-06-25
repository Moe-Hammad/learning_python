liste = []
beenden = False
while beenden != True:
    opt = input("Was willst du machen? show, delete, add, finish?")
    if opt == "add":
        liste.append(input("Welches Item :"))
    elif opt == "delete":
        print(liste)
        liste.remove(input("Welches Item soll gelöscht werden?"))
        print(liste)
    elif opt == "show":
        print(liste)
    elif opt == "finish":
        beenden = True
    else:
        print("Falsche Eingabe")

print(liste)
