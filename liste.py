############# Liste
leere_liste = ["Apfel", "Birne", "Orange", "Zitrone"]
print(leere_liste)
leere_liste.append("Trauben")
print(leere_liste)
leere_liste.insert(0, "Pflaume")
print(leere_liste)
leere_liste.remove("Apfel")
print(leere_liste)
leere_liste.pop()
print(leere_liste)
del leere_liste[0]
print(leere_liste)
#################################
andereliste = ["Apfel", "Birne", "Orange", "Zitrone"]
print(len(andereliste))
print(andereliste[: len(andereliste) + 1])

zListe = ["Apfel", "Birne", "Orange", "Zitrone", ["arabisch", "spanisch"]]
