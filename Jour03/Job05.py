import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, autre_personnage):
        degats = random.randint(5, 20)
        print(f"{self.nom} attaque {autre_personnage.nom} et lui inflige {degats} points de dégâts !")
        autre_personnage.vie -= degats
    
    def est_en_vie(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisirNiveau(self):
        niveaux = {
            "facile": (100, 50),
            "normal": (80, 60),
            "difficile": (60, 70)
        }
        while self.niveau not in niveaux:
            self.niveau = input("Choisissez votre niveau (facile, normal ou difficile) : ").lower()
        self.points_vie_joueur, self.points_vie_ennemi = niveaux[self.niveau]
    
    def lancerJeu(self):
        joueur = Personnage("Joueur", self.points_vie_joueur)
        ennemi = Personnage("Ennemi", self.points_vie_ennemi)
        print(f"Un ennemi ({self.niveau}) apparaît !")
        print(f"{joueur.nom} a {joueur.vie} points de vie.")
        print(f"{ennemi.nom} a {ennemi.vie} points de vie.")
        print("Que la bataille commence !")
        while joueur.est_en_vie() and ennemi.est_en_vie():
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)
            print(f"{joueur.nom} a {joueur.vie} points de vie.")
            print(f"{ennemi.nom} a {ennemi.vie} points de vie.")
        if joueur.est_en_vie():
            print(f"{joueur.nom} a gagné !")
        else:
            print(f"{ennemi.nom} a gagné !")

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
