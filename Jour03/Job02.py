class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Compte n°{self.__numero} de {self.__prenom} {self.__nom}")
    
    def afficherSolde(self):
        print(f"Solde du compte n°{self.__numero} : {self.__solde} euros")
    
    def versement(self, montant):
        self.__solde += montant
        print(f"{montant} euros ont été versés sur le compte n°{self.__numero}")
        self.afficherSolde()
    
    def retrait(self, montant):
        if self.__solde - montant >= -self.__decouvert:
            self.__solde -= montant
            print(f"{montant} euros ont été retirés du compte n°{self.__numero}")
            self.afficherSolde()
        else:
            print("Opération impossible : solde insuffisant")
    
    def agios(self, taux):
        if self.__solde < 0:
            montant_agios = -self.__solde * taux
            self.__solde -= montant_agios
            print(f"{montant_agios} euros d'agios ont été prélevés sur le compte n°{self.__numero}")
            self.afficherSolde()
    
    def virement(self, compte_dest, montant):
        if self.__solde - montant >= -self.__decouvert:
            self.__solde -= montant
            compte_dest.versement(montant)
            print(f"{montant} euros ont été virés du compte n°{self.__numero} vers le compte n°{compte_dest.get_numero()}")
        else:
            print("Opération impossible : solde insuffisant")
    
    def get_numero(self):
        return self.__numero
compte1 = CompteBancaire(123456, "Dupont", "Jean", 1000)

compte1.afficher()

compte1.afficherSolde()

compte1.versement(500)

compte1.retrait(200)

compte2 = CompteBancaire(654321, "Martin", "Sophie", -500, True)

compte2.afficherSolde()

compte1.virement(compte2, 500)

compte1.afficherSolde
