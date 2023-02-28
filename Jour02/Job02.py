class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
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
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)
print(mon_livre.get_titre())
print(mon_livre.get_auteur())
print(mon_livre.get_nb_pages())

mon_livre.set_titre("Les Misérables")
mon_livre.set_auteur("Victor Hugo")
mon_livre.set_nb_pages(1500)
print(mon_livre.get_titre())
print(mon_livre.get_auteur())
print(mon_livre.get_nb_pages())

mon_livre.set_nb_pages(-10) 
print(mon_livre.get_nb_pages()) 