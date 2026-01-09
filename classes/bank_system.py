class Client:
    def __init__(self, nom, prenom, cin):
        self.nom = nom
        self.prenom = prenom
        self.__cin = cin


class Transaction:
    def __init__(self, type, montant, date):
        self.__type = type
        self.__montant = montant
        self.__date = date


class CompteBancaire:
    def __init__(self, num_compte, solde, titulaire.historique_transaction):
        self.__num_compte = num_compte
        self.__solde = solde
        self.__titulaire = titulaire
        self.__historique_transactions = []

    def deposer(self):

    def retirer(self):

    def afficher_solde(self):

    def afficher_transactions(self):
