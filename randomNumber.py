from random import randint

zahl = randint(1, 100)
user = 0
while zahl != user:
    user = int(input("Errate die Zahl von 1 - 100: "))
    if zahl < user:
        print("Die Zahl ist kleiner!")
    elif zahl > user:
        print("Die Zahl ist größer!")
    else:
        print("Du hast gewonnen")
        break
