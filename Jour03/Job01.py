class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population
        
    def ajouter_population(self):
        self.population += 1
        
class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville
        
    def ajouter_population(self):
        self.ville.ajouter_population()

ville_paris = Ville("Paris", 1000000)
print("Nombre d'habitants de Paris :", ville_paris.population)

ville_marseille = Ville("Marseille", 861635)
print("Nombre d'habitants de Marseille :", ville_marseille.population)

john = Personne("John", 45, ville_paris)
john.ajouter_population()

myrtille = Personne("Myrtille", 4, ville_paris)
myrtille.ajouter_population()

chloe = Personne("Chloé", 18, ville_marseille)
chloe.ajouter_population()

print("Nombre d'habitants de Paris après l'arrivée de John et Myrtille :", ville_paris.population)
print("Nombre d'habitants de Marseille après l'arrivée de Chloé :", ville_marseille.population)
