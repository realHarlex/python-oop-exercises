class Client:
    def __init__(self, nom, prenom, cin):
        self.nom = nom
        self.prenom = prenom
        self.__cin = cin
    def afficher_client(self):
        print(f"Client: {self.prenom} {self.nom}, CIN: {self.__cin}")


class Transaction:
    def __init__(self, type_transaction, montant, date):
        self.__type = type_transaction
        self.__montant = montant
        self.__date = date

    def afficher_transaction(self):
        print(f"{self.__date} - {self.__type} : {self.__montant} MAD")


class CompteBancaire:
    def __init__(self, num_compte, solde, titulaire):
        self.__num_compte = num_compte
        self.__solde = solde
        self.__titulaire = titulaire
        self.__transactions = []

    def deposer(self, montant, date="01/01/2025"):
        self.__solde += montant
        transaction = Transaction("Dépôt", montant, date)
        self.__transactions.append(transaction)

    def retirer(self, montant, date="01/01/2025"):
        if montant <= self.__solde:
            self.__solde -= montant
            transaction = Transaction("Retrait", montant, date)
            self.__transactions.append(transaction)
        else:
            print("Fonds insuffisants")

    def afficher_solde(self):
        print(f"Solde du compte {self.__num_compte} : {self.__solde} MAD")

    def afficher_transactions(self):
        print(f"Historique des transactions du compte {self.__num_compte} :")
        if not self.__transactions:
            print("Aucune transaction")
        for t in self.__transactions:
            t.afficher_transaction()


client1 = Client("El Amrani", "Youssef", "AB123456")
compte1 = CompteBancaire("123456789", 1000, client1)

compte1.deposer(500)
compte1.retirer(200)
compte1.afficher_solde()
compte1.afficher_transactions()