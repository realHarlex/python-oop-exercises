# class Personne:
#     def __init__(self, id, nom, prenom, anne_naiss):
#         self.id = id
#         self.nom = nom
#         self.prenom = prenom
#         self.annee_naiss = anne_naiss
        
#     def affiche_infos(self):
#         print(f"L'identifiant de la personne est : {self.id}")
#         print(f"Le nom de la personne est : {self.nom}")
#         print(f"Le prenom de la personne est : {self.prenom}")
#         print(f"Son annee de naissance est : {self.annee_naiss}")
        
#     def calcul_age(self):
#         age = 2025 - self.annee_naiss
#         return age
    
#     def nom_complet(self):
#         return f"{self.nom}  {self.prenom}"

# P1 = Personne(1, "Nom 1", "Mohammed", 2000)
# P2 = Personne(2, "Nom 2", "Siham", 2004)

# print(P1.calcul_age())
# print(P2.nom_complet())

# _________________________________________________________________________________________________________________

# class Personne:
#     def __init__(self, nom, prenom, age, skills):
#         self.nom = nom
#         self.prenom = prenom
#         self.age = age
#         self.__skills = skills
        
#     def getAge(self):
#         return self.__age
        
#     def setAge(self, newAge):
#         self.__age = newAge
    
#     def nom_complet(self):
#         return f"{self.nom}  {self.prenom}"

#     def afficherSkills(self):
#         for i in range(len(self.__skills)):
#             print(f"{i+1} - {self.__skills[i]}")
        
# P1 = Personne("Khalid", "Tarik", 20, ["HTML", "CSS", "PYTHON"])
# P1.getAge
# P1.setAge(25)
# P1.afficherSkills()

# _________________________________________________________________________________________________________________

# class Module:
#     def __init__(self, intitule, m_horaire, nbr_cc):
#         self.intitule = intitule
#         self.m_horaire = m_horaire
#         self.nbr_cc = nbr_cc

#     def afficher_infos_module(self):
#         print(f"L'intitulé du module : {self.intitule}")
#         print(f"Le temps horaire : {self.m_horaire}")
#         print(f"Nombre de contrôles : {self.nbr_cc}")

# class Stagiaire:
#     def __init__(self, nom, prenom, groupe, list_CC, efm, module):
#         self.nom = nom
#         self.prenom = prenom
#         self.__groupe = groupe
#         self.__list_CC = list_CC
#         self.__efm = efm
#         self.module = module

#     def afficherEmail(self):
#         return f"{self.nom.lower()}.{self.prenom.lower()}@ofppt-edu.ma"

#     def Calcul_Moy(self):
#         moy_cc = sum(self.__list_CC) / len(self.__list_CC)
#         moy = moy_cc * 0.33 + self.__efm * 0.67
#         return moy

#     def Validation(self):
#         moyenne = self.Calcul_Moy()
#         if moyenne >= 10:
#             print(f"{self.nom} {self.prenom} a validé le module {self.module.intitule} par {moyenne:.2f}")
#         else:
#             print(f"{self.nom} {self.prenom} n'a pas validé le module {self.module.intitule} par {moyenne:.2f}")

# module = Module("Algorithme", "60H", 3)
# stagiaire = Stagiaire("Hamza", "Mgh", "Dev103", [12, 16, 9], 14, module)

# print(stagiaire.afficherEmail())
# print(f"Moyenne : {stagiaire.Calcul_Moy():.2f}")

# stagiaire.Validation()
# stagiaire.module.afficher_infos_module()

class Pays:
    def __init__(self, nom_pay, code_FiFa):
        self.nom_pay = nom_pay
        self.code_FiFa = code_FiFa
        
Pay1 = Pays("Maroc", "MAR")
Pay2 = Pays("Zambia", "ZAM")
        
class Equipe:
    def __init__(self, nom_equipe, pays, nbr_joueurs):
        self.nom_equipe = nom_equipe
        self.pays = pays
        self.nbr_joueurs = nbr_joueurs
 
Eq1 = Equipe("Les lions", Pay1, 23)
Eq2 = Equipe("Les Chipolopolo", Pay2, 23)
 
class Stade:
    def __init__(self, nom_stade, ville, capacité):
        self.nom_stade = nom_stade
        self.ville = ville
        self.capacité = capacité

Stade1 = Stade("Stade Moulay Abdellah", "Rabat", 70000)
class Match:
    def __init__(self, equipe1, equipe2, stade, score_equ1, score_equ2, date):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        self.stade = stade
        self.score_equ1 = score_equ1
        self.score_equ2 = score_equ2
        self.date = date

    def Resulat(self):
        print(self.date)
        print(f"{self.equipe1.pays.nom_pay} ({self.equipe1.pays.code_FiFa}) vs {self.equipe2.pays.nom_pay} ({self.equipe2.pays.code_FiFa}) : {self.score_equ1} - {self.score_equ2}")
        print(f"{Stade1.nom_stade} ({self.stade.nom_stade}, {Stade1.capacité} Places)")
        
Match1 = Match(Eq1, Eq2, Stade1, 3, 0, "29/12/2025")

Match1.Resulat()
