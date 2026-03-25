from tkiteasy import *


class Parametres():
    def __init__(self):
        self.nbj = 2
        self.nbv_duel = 10
        self.nbv_solo = 20
        self.taille_plan = 900
        self.taille_ville_duel = 110
        self.taille_ville_solo = 40
        self.hauteur_option = 70
        self.longueur_option = 180
        self.taille_grenouille = 75
        self.taille_engrenage = 80
        self.rayon_parametre = 10
        self.catalogue_duel = {"5":(408,216), "6":(408,268), "7":(408,320), "8":(408,371), "9":(616,216), "10":(616,268), "11":(616,320), "12":(616,371)}
        self.catalogue_solo = {"15":(553,580), "20":(553,648), "30":(553,714)}

    def initParametres(self):
        self.fenetre_param = ouvrirFenetre(self.taille_plan, self.taille_plan)
        self.fenetre_param.afficherImage(0, 0, "Images/parametres.png", self.taille_plan, self.taille_plan)
        self.disque_duel = self.fenetre_param.dessinerDisque(self.catalogue_duel[str(self.nbv_duel)][0], self.catalogue_duel[str(self.nbv_duel)][1], self.rayon_parametre, "#2D221B")
        self.disque_solo = self.fenetre_param.dessinerDisque(self.catalogue_solo[str(self.nbv_solo)][0], self.catalogue_solo[str(self.nbv_solo)][1], self.rayon_parametre, "#2D221B")

        self.engrenage = self.fenetre_param.afficherImage(850 - (self.taille_engrenage / 2),850 - (self.taille_engrenage / 2), "Images/engrenage.png",self.taille_engrenage, self.taille_engrenage)

    def ChoixParametres(self):
        clic = self.fenetre_param.attendreClic()
        while self.fenetre_param.recupererObjet(clic.x, clic.y) != self.engrenage:
            choix_nbv_duel = self.ChoixNbvDuel(clic.x, clic.y)
            choix_nbv_solo = self.ChoixNbvSolo(clic.x, clic.y)
            if choix_nbv_duel:
                self.fenetre_param.deplacer(self.disque_duel, self.catalogue_duel[str(choix_nbv_duel)][0]-self.catalogue_duel[str(self.nbv_duel)][0], self.catalogue_duel[str(choix_nbv_duel)][1]-self.catalogue_duel[str(self.nbv_duel)][1])
                self.nbv_duel = int(choix_nbv_duel)
            if choix_nbv_solo:
                self.fenetre_param.deplacer(self.disque_solo, self.catalogue_solo[str(choix_nbv_solo)][0]-self.catalogue_solo[str(self.nbv_solo)][0], self.catalogue_solo[str(choix_nbv_solo)][1]-self.catalogue_solo[str(self.nbv_solo)][1])
                self.nbv_solo = int(choix_nbv_solo)
            clic = self.fenetre_param.attendreClic()
        self.fenetre_param.fermerFenetre()
        return

    def ChoixNbvDuel(self, x, y):
        if x > 275 and x < 375 and y > 200 and y < 235:
            return "5"
        elif x > 275 and x < 375 and y > 250 and y < 285:
            return "6"
        elif x > 275 and x < 375 and y > 300 and y < 338:
            return "7"
        elif x > 275 and x < 375 and y > 355 and y < 390:
            return "8"
        elif x > 480 and x < 580 and y > 200 and y < 235:
            return "9"
        elif x > 480 and x < 580 and y > 250 and y < 285:
            return "10"
        elif x > 480 and x < 580 and y > 300 and y < 338:
            return "11"
        elif x > 480 and x < 580 and y > 355 and y < 390:
            return "12"

    def ChoixNbvSolo(self, x, y):
        if x > 385 and x < 515 and y > 560 and y < 605:
            return "15"
        elif x > 385 and x < 515 and y > 625 and y < 675:
            return "20"
        elif x > 385 and x < 515 and y > 690 and y < 740:
            return "30"