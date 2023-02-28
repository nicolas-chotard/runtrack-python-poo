class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__nb_credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, nb_credits):
        if nb_credits > 0:
            self.__nb_credits += nb_credits
            self.__level = self.__studentEval()
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_num_etudiant(self):
        return self.__num_etudiant

    def set_num_etudiant(self, num_etudiant):
        self.__num_etudiant = num_etudiant

    def get_nb_credits(self):
        return self.__nb_credits

    def __studentEval(self):
        if self.__nb_credits >= 90:
            return "Excellent"
        elif self.__nb_credits >= 80:
            return "Très bien"
        elif self.__nb_credits >= 70:
            return "Bien"
        elif self.__nb_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Identifiant : {self.__num_etudiant}")
       
        print(f"Niveau : {self.__level}")

john_doe = Student("Doe", "John", 145)
john_doe.add_credits(20)
john_doe.add_credits(40)
john_doe.add_credits(10)

print(f"Nombre total de crédits de John Doe : {john_doe.get_nb_credits()}")

john_doe.studentInfo()
