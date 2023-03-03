def max_chiffre(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        premier_chiffre = liste[0]
        max_chiffre_restant = max_chiffre(liste[1:])
        if premier_chiffre > max_chiffre_restant:
            return premier_chiffre
        else:
            return max_chiffre_restant
liste = [3, 7, 1, 9, 4, 2, 8]
print(max_chiffre(liste))
