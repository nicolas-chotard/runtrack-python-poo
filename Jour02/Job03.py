class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")
    
    def vérification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.vérification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")
    
    def rendre(self):
        if not self.vérification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)

print(mon_livre.vérification())

mon_livre.emprunter()
print(mon_livre.vérification())

mon_livre.emprunter()

mon_livre.rendre()
print(mon_livre.vérification())

mon_livre.rendre() 
