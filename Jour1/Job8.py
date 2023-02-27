class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def afficherInfos(self):
        print("Cercle de rayon", self.rayon)
    
    def circonference(self):
        return 2 * 3.14159 * self.rayon
    
    def aire(self):
        return 3.14159 * (self.rayon ** 2)
    
    def diametre(self):
        return 2 * self.rayon
cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print("Circonférence :", cercle1.circonference())
print("Diamètre :", cercle1.diametre())
print("Aire :", cercle1.aire())


cercle2.afficherInfos()
print("Circonférence :", cercle2.circonference())
print("Diamètre :", cercle2.diametre())
print("Aire :", cercle2.aire())