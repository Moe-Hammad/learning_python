liste = []
weiter = input("Willst du was hinzufügen? Tippe y :")
while weiter == "y":
    liste.append(input("Was willst du hinzufügen!"))
    weiter = input("Mehr?")

print(liste)
