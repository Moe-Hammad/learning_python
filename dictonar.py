####### Schlüssel (unique) und Wert.
leeres_dict = {}

einkaufs_dict = {"artikelname": "Banane", "Preis": 2, "Ablauf": 2024}

print(einkaufs_dict)

print(einkaufs_dict["Preis"])
print(einkaufs_dict.keys())
print(einkaufs_dict.values())
einkaufs_dict["Preis"] = 3
einkaufs_dict["Neu"] = True
print(einkaufs_dict)
einkaufs_dict.pop("Neu")
print(einkaufs_dict)

# durschlauefen

for i in einkaufs_dict:
    print(i, einkaufs_dict[i])
