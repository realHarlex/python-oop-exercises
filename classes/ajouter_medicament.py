class Patient:
    def __init__(self, nom, cin):
        self.nom = nom
        self.cin = cin


class Medecin:
    def __init__(self, nom, prix, specialite):
        self.nom = nom
        self.prix = prix
        self.specialite = specialite


class Medicament:
    def __init__(self, nom, prix, nbr_fois):
        self.nom = nom
        self.prix = prix
        self.nbr_fois = nbr_fois


class Consultation:
    def __init__(self, num_consultation, date, patient, medecin, diagnostique, prix_consultation):
        self.num_consultation = num_consultation
        self.date = date
        self.patient = patient
        self.medecin = medecin
        self.diagnostique = diagnostique
        self.prix_consultation = prix_consultation
        self.medicaments = []   # liste de médicaments

    def ecrire_ordonnance(self):
        print("----- ORDONNANCE -----")
        print(f"Patient : {self.patient.nom}")
        print(f"Médecin : {self.medecin.nom}")
        print(f"Diagnostique : {self.diagnostique}")
        print("Médicaments :")
        for med in self.medicaments:
            print(f"- {med.nom} | {med.nbr_fois} fois | {med.prix} DH")
        print("----------------------")

    def ajouter_medicament(self, med):
        self.medicaments.append(med)

    def calcul_prix(self):
        total = self.prix_consultation
        for med in self.medicaments:
            total += med.prix
        return total
p = Patient("Ali", "AB123")
m = Medecin("Dr Sara", 100, "Généraliste")

c = Consultation(1, "01/01/2026", p, m, "Grippe", 100)

med1 = Medicament("Paracétamol", 20, 3)
med2 = Medicament("Vitamine C", 15, 2)

c.ajouter_medicament(med1)
c.ajouter_medicament(med2)

c.ecrire_ordonnance()
print("Prix total :", c.calcul_prix(), "DH")
 