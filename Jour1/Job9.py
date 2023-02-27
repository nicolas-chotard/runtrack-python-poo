class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infoProduit = self.getInfoProduit()
        for info in infoProduit:
            print(f"{info} : {infoProduit[info]}")

    def modifierNom(self, nouveauNom):
        self.nom = nouveauNom

    def modifierPrixHT(self, nouveauPrixHT):
        self.prixHT = nouveauPrixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getInfoProduit(self):
        infoProduit = {
            "Nom du produit": self.nom,
            "Prix HT": f"{self.prixHT} €",
            "Taux de TVA": f"{self.TVA}%",
            "Prix TTC": f"{self.CalculerPrixTTC()} €"
        }
        return infoProduit

produit1 = Produit("Televiseur", 800, 30)
produit1.afficher()

produit2 = Produit("Ordinateur", 1200, 20)
produit2.afficher()
