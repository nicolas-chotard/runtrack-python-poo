def longueur(chaine):
    if chaine == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])
chaine = "Bonjour, monde !"
print("La longueur de la chaîne est :", longueur(chaine))
