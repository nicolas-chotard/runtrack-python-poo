class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("J'ai", self.age, "ans.")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans.")


class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer.")

personne1 = Personne()

eleve1 = Eleve()

eleve1.affichageAge()

eleve1.modifierAge(15)

eleve1.bonjour()
eleve1.allerEnCours()

professeur1 = Professeur(age=40, matiereEnseignee="Mathématiques")

professeur1.bonjour()
professeur1.enseigner()
