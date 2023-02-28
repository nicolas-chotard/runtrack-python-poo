class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    def get_marque(self):
        return self._marque

    def set_marque(self, marque):
        self._marque = marque

    def get_modele(self):
        return self._modele

    def set_modele(self, modele):
        self._modele = modele

    def get_annee(self):
        return self._annee

    def set_annee(self, annee):
        self._annee = annee

    def get_kilometrage(self):
        return self._kilometrage

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    def get_en_marche(self):
        return self._en_marche

    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide, il faut faire le plein avant de démarrer.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    def get_reservoir(self):
        return self._reservoir

    def _verifier_plein(self):
        if self._reservoir > 5:
            return True
        else:
            return False

ma_voiture = Voiture("Renault", "Clio", 2010, 150000)

ma_voiture.set_kilometrage(160000)
ma_voiture.set_annee(2012)

ma_voiture.demarrer()

ma_voiture.arreter()
