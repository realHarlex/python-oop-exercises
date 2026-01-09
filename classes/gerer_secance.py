from datetime import date

class Personne:
    def __init__(self, nom, prenom, date_naiss):
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        
    def afficher_infos(self):
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Date de naissance : {self.date_naiss}")
    
    def afficher_email(self):
        print(f"{self.nom.lower()}.{self.prenom.lower()}@gmail.com")
    
    def calcul_age(self):
        return date.today().year - self.date_naiss

class Stagiaire(Personne):
    def __init__(self, nom, prenom, date_naiss, groupe, moyenne):
        Personne.__init__(self, nom, prenom, date_naiss)
        self.groupe = groupe
        self.moyenne = moyenne

    def afficher_infos(self):
        Personne.afficher_infos(self)
        print(f"Groupe : {self.groupe}")
        print(f"Moyenne : {self.moyenne}")
    
    def validation(self):
        if self.moyenne >= 10:
            print("Validé")
        else:
            print("Non validé")

class Formateur(Personne):
    def __init__(self, nom, prenom, date_naiss, specialite, prix_heure):
        Personne.__init__(self, nom, prenom, date_naiss)
        self.specialite = specialite
        self.prix_heure = prix_heure
        
    def calcul_remuneration(self, heures):
        return heures * self.prix_heure
    
    def afficher_infos(self):
        Personne.afficher_infos(self)
        print(f"Spécialité : {self.specialite}")
        print(f"Prix par heure : {self.prix_heure}")

class Module:
    def __init__(self, intitule, m_horaire):
        self.intitule = intitule
        self.m_horaire = m_horaire

class Seance:
    def __init__(self, module, date_seance, h_debut, h_fin, formateur, stagiaires):
        self.module = module
        self.date_seance = date_seance
        self.h_debut = h_debut
        self.h_fin = h_fin
        self.formateur = formateur
        self.stagiaires = stagiaires
        
    def afficher_infos(self):
        print(f"Module : {self.module.intitule}")
        print(f"Date : {self.date_seance}")
        print(f"Heure : {self.h_debut}h - {self.h_fin}h")
        print(f"Formateur : {self.formateur.nom}")
    
    def calcul_duree(self):
        return self.h_fin - self.h_debut
    
    def nbr_stg_present(self):
        return len(self.stagiaires)

class SeancePresentiel(Seance):
    def __init__(self, module, date_seance, h_debut, h_fin, formateur, stagiaires, pole, etage, salle):
        Seance.__init__(self, module, date_seance, h_debut, h_fin, formateur, stagiaires)
        self.pole = pole
        self.etage = etage
        self.salle = salle
        
    def afficher_infos(self):
        Seance.afficher_infos(self)
        print(f"Pôle : {self.pole}, Étage : {self.etage}, Salle : {self.salle}")

class SeanceEnLigne(Seance):
    def __init__(self, module, date_seance, h_debut, h_fin, formateur, stagiaires, plateforme, lien):
        Seance.__init__(self, module, date_seance, h_debut, h_fin, formateur, stagiaires)
        self.plateforme = plateforme
        self.lien = lien
        
    def afficher_infos(self):
        Seance.afficher_infos(self)
        print(f"Plateforme : {self.plateforme}")
        print(f"Lien : {self.lien}")

stg1 = Stagiaire("Zablo", "Amin", 2005, 1, 15)
stg2 = Stagiaire("Mastour", "Hachim", 2004, 1, 12)

form = Formateur("Ali", "Karim", 1985, "Python", 100)
mod = Module("POO Python", 30)

seance = SeancePresentiel(mod,"2026-01-10",8,12,form,[stg1, stg2],"Pole Digital",2,"Salle 5")

seance.afficher_infos()
print("Durée :", seance.calcul_duree(), "heures")
print("Stagiaires présents :", seance.nbr_stg_present())