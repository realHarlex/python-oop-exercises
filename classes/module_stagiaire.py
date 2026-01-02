class Module:
    def __init__(self, intitule, m_horaire, nbr_cc):
        self.intitule = intitule
        self.m_horaire = m_horaire
        self.nbr_cc = nbr_cc

class Stagiaire:
    def __init__(self, nom, prenom, groupe, list_CC, efm, module):
        self.nom = nom
        self.prenom = prenom
        self.__groupe = groupe
        self.__list_CC = list_CC
        self.__efm = efm
        self.module = module

    def afficherEmail(self):
        return f"{self.nom.lower()}.{self.prenom.lower()}@ofppt-edu.ma"

    def Calcul_Moy(self):
        moy_cc = sum(self.__list_CC) / len(self.__list_CC)
        return moy_cc * 0.33 + self.__efm * 0.67

    def Validation(self):
        moyenne = self.Calcul_Moy()
        if moyenne >= 10:
            print(f"{self.nom} {self.prenom} a validé le module {self.module.intitule} par {moyenne:.2f}")
        else:
            print(f"{self.nom} {self.prenom} n'a pas validé le module {self.module.intitule} par {moyenne:.2f}")
