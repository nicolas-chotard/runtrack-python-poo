class Operation:
    def __init__(self, nb1, nb2):
        self.nombre1 = nb1
        self.nombre2 = nb2

    def addition(self):
        
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", resultat)

operation1 = Operation(12, 3) 
operation1.addition()


