from classes.personne import Personne
from classes.module_stagiaire import Module, Stagiaire
from classes.football import Pays, Equipe, Stade, Match

# Personne example
p1 = Personne(1, "Nom1", "Mohammed", 2000)
print(p1.nom_complet())
print(p1.calcul_age())

# Stagiaire example
module1 = Module("Algorithme", "60H", 3)
stagiaire1 = Stagiaire("Hamza", "Mgh", "Dev103", [12, 16, 9], 14, module1)
print(stagiaire1.afficherEmail())
stagiaire1.Validation()

# Football example
maroc = Pays("Maroc", "MAR")
zambia = Pays("Zambia", "ZAM")
eq1 = Equipe("Les lions", maroc, 23)
eq2 = Equipe("Les Chipolopolo", zambia, 23)
stade1 = Stade("Stade Moulay Abdellah", "Rabat", 70000)
match1 = Match(eq1, eq2, stade1, 3, 0, "29/12/2025")
match1.Resulat()
