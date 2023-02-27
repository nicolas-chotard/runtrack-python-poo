class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Coordonnées du point :",self.x, self.y)

    def afficherX(self):
        print("La coordonnée x du point est : ",self.x)

    def afficherY(self):
        print("La coordonnée y du point est : ",self.y)

    def changerX(self, nouvelle_x):
        self.x = nouvelle_x

    def changerY(self, nouvelle_y):
        self.y = nouvelle_y

p = Point(2, 3)
p.afficherLesPoints()
p.changerX(2)
p.afficherX()
p.changerY(3)
p.afficherY()
