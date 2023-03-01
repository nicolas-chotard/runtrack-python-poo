class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
        
    def marquerUnBut(self):
        self.buts_marques += 1
        
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        
    def afficherStatistiques(self):
        print("Statistiques de ", self.nom)
        print("Nombre de buts marqués :", self.buts_marques)
        print("Nombre de passes décisives :", self.passes_decisives)
        print("Nombre de cartons jaunes reçus :", self.cartons_jaunes)
        print("Nombre de cartons rouges reçus :", self.cartons_rouges)


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
        
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        
    def afficherStatistiquesJoueurs(self):
        print("Statistiques de l'équipe", self.nom)
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
            
    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Action invalide")
                break

j1 = Joueur("Ronaldo", 7, "Attaquant")
j2 = Joueur("Messi", 10, "Attaquant")
j3 = Joueur("Neymar", 11, "Attaquant")
j4 = Joueur("Mbappé", 9, "Attaquant")
j5 = Joueur("Kante", 6, "Milieu")
j6 = Joueur("Pogba", 8, "Milieu")
j7 = Joueur("Varane", 4, "Défenseur")
j8 = Joueur("Lenglet", 5, "Défenseur")
j9 = Joueur("Kimpembe", 3, "Défenseur")
j10 = Joueur("Lloris", 1, "Gardien")

equipe1 = Equipe("Equipe 1")
equipe2 = Equipe("Equipe 2")

equipe1.ajouterJoueur(j1)
equipe1.ajouterJoueur(j2)
equipe1.ajouterJoueur(j3)
equipe1.ajouterJoueur(j4)
equipe1.ajouterJoueur(j5)
equipe1.ajouterJoueur(j6)
equipe1.ajouterJoueur(j7)
equipe1.ajouterJoueur(j8)
equipe1.ajouterJoueur(j9)
equipe1.ajouterJoueur(j10)

equipe2.ajouterJoueur(j1)
equipe2.ajouterJoueur(j2)
equipe2.ajouterJoueur(j3)
equipe2.ajouterJoueur(j4)
equipe2.ajouterJoueur(j5)
equipe2.ajouterJoueur(j6)
equipe2.ajouterJoueur(j7)
equipe2.ajouterJoueur(j8)
equipe2.ajouterJoueur(j9)
equipe2.ajouterJoueur(j10)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur("Ronaldo", "but")
equipe1.mettreAJourStatistiquesJoueur("Messi", "passe")
equipe1.mettreAJourStatistiquesJoueur("Kante", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Neymar", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Mbappé", "rouge")

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
