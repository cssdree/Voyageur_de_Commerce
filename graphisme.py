from tkiteasy import *


class Graphisme():
    def __init__(self, taille, villes):
        self.taille = taille
        self.villes = villes
        self.fenetre = ouvrirFenetre(self.taille, self.taille)
        self.initGraphisme()

    def initGraphisme(self):
        self.fenetre.afficherImage(0, 0, "Images/fond.png", 900, 900)
        for ville in self.villes.dict:
            self.fenetre.afficherImage(self.villes.dict[ville][0], self.villes.dict[ville][1], "Images/nenuphar.png", 150, 150)
        self.fenetre.actualiser()
        clic = self.fenetre.attendreClic()