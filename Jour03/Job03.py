class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
    
    def __repr__(self):
        return f"{self.titre} - {self.description} - {self.statut}"
    
    def marquer_comme_finie(self):
        self.statut = "terminée"


class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouter_tache(self, tache):
        self.taches.append(tache)
    
    def supprimer_tache(self, tache):
        self.taches.remove(tache)
    
    def marquer_comme_finie(self, tache):
        tache.marquer_comme_finie()
    
    def afficher_liste(self):
        for tache in self.taches:
            print(tache)
    
    def filter_liste(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

tache1 = Tache("Faire les courses", "Acheter du pain et du lait")
tache2 = Tache("Faire la lessive", "Laver les vêtements")
tache3 = Tache("Faire du sport", "Jogging pendant 30 minutes")

liste_de_taches = ListeDeTaches()
liste_de_taches.ajouter_tache(tache1)
liste_de_taches.ajouter_tache(tache2)
liste_de_taches.ajouter_tache(tache3)

liste_de_taches.afficher_liste()

liste_de_taches.marquer_comme_finie(tache1)


liste_de_taches.supprimer_tache(tache3)

liste_de_taches.afficher_liste()
