class Animal:

    def __init__(self):
        self.age = 1
        self.nom = ""

    
    def vieillir(self):
        self.age += 1

    
    def nommer(self, nouveau_nom):
        self.nom = nouveau_nom
        

mon_animal = Animal()
print("Âge initial de l'animal : ", mon_animal.age)

mon_animal.vieillir()
print("Âge de l'animal après vieillissement : ", mon_animal.age)

mon_animal.nommer("Luna")
print("Nom de l'animal : ", mon_animal.nom)