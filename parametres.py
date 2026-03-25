from tkiteasy import *


class Parametres():
    def __init__(self):
        self.nbj = 2
        self.nbv = 12
        self.taille_plan = 900
        self.taille_ville = 110
        self.hauteur_option = 70
        self.longueur_option = 180
        self.taille_grenouille = 75
        self.taille_engrenage = 80

    def initParametres(self):
        self.fenetre_param = ouvrirFenetre(self.taille_plan, self.taille_plan)
        self.fenetre_param.afficherImage(0, 0, "Images/parametres.png", self.taille_plan, self.taille_plan)
        self.engrenage = self.fenetre_param.afficherImage(850 - (self.taille_engrenage / 2),850 - (self.taille_engrenage / 2), "Images/engrenage.png",self.taille_engrenage, self.taille_engrenage)

    def ChoixParametres(self):
        clic = self.fenetre_param.attendreClic()
        while self.fenetre_param.recupererObjet(clic.x, clic.y) != self.engrenage:
            clic = self.fenetre_param.attendreClic()
        self.fenetre_param.fermerFenetre()
        return