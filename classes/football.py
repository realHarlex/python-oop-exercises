class Pays:
    def __init__(self, nom_pay, code_FiFa):
        self.nom_pay = nom_pay
        self.code_FiFa = code_FiFa

class Equipe:
    def __init__(self, nom_equipe, pays, nbr_joueurs):
        self.nom_equipe = nom_equipe
        self.pays = pays
        self.nbr_joueurs = nbr_joueurs

class Stade:
    def __init__(self, nom_stade, ville, capacite):
        self.nom_stade = nom_stade
        self.ville = ville
        self.capacite = capacite

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
        print(f"{self.stade.nom_stade} ({self.stade.capacite} places)")
