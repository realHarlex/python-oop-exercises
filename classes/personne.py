class Personne:
    def __init__(self, id, nom, prenom, annee_naiss):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.annee_naiss = annee_naiss

    def affiche_infos(self):
        print(f"L'identifiant de la personne est : {self.id}")
        print(f"Le nom de la personne est : {self.nom}")
        print(f"Le prenom de la personne est : {self.prenom}")
        print(f"Son annee de naissance est : {self.annee_naiss}")

    def calcul_age(self):
        return 2025 - self.annee_naiss

    def nom_complet(self):
        return f"{self.nom} {self.prenom}"
