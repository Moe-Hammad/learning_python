############################################
# String Slicing
x = "Hallo Welt!!"
# String Slicing -- for Schleife bis 5, wenn nicht angegben wird an erster Stelle dann geht fängt er vorne an.
# anderesherum bis zum Schluss
print(x[:5])

print(x[6:10])

############################################

y = "Das ist ein Satz und ich werde herausfinden wie lang der ist."
print(len(y))
print("Die Variable y ist",len(y), "lang")

############################################
# Überschreiben von einem String

a = "H" + x[1:]
print("A ist" , a)
print(a * 10)
############################################
# String Funktion
print(x.upper())
print(x.lower())
print(x.split())
print(x.find("Welt"))
print(x[x.find("Welt"):])
############################################
