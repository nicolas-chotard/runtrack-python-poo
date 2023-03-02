class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Age :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvelAge):
        self.age = nouvelAge

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee='Français'):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    def afficherMatiereEnseignee(self):
        print("Matière enseignée :", self.matiereEnseignee)

personne1 = Personne()
personne1.afficherAge()

eleve1 = Eleve()
eleve1.affichageAge()


Professeur1 = Professeur()
Professeur1.enseigner()
Professeur1.afficherMatiereEnseignee()