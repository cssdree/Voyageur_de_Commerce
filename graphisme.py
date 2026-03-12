from tkiteasy import *


class Graphisme():
    def __init__(self, taille, villes):
        self.taille = taille
        self.villes = villes
        self.fenetre = ouvrirFenetre(self.taille, self.taille)
        self.initGraphisme()

    def initGraphisme(self):
        for ville in self.villes.dict:
            self.fenetre.dessinerDisque(self.villes.dict[ville][0], self.villes.dict[ville][1], 10, "white")
        self.fenetre.actualiser()
        clic = self.fenetre.attendreClic()