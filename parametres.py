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

    def initParametres(self):
        self.fenetre_param = ouvrirFenetre(self.taille_plan, self.taille_plan)