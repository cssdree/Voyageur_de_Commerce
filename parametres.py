from tkiteasy import *


class Parametres():
    def __init__(self):
        self.nbj = 2
        self.nbv_duel = 10
        self.nbv_solo = 20
        self.taille_plan = 600
        self.taille_ville_duel = int(self.taille_plan*110/900)
        self.taille_ville_solo = int(self.taille_plan*50/900)
        self.hauteur_option = int(self.taille_plan*70/900)
        self.longueur_option = int(self.taille_plan*180/900)
        self.taille_grenouille = int(self.taille_plan*75/900)
        self.taille_engrenage = int(self.taille_plan*80/900)
        self.rayon_parametre = int(self.taille_plan*10/900)
        self.catalogue_duel = {"5":(int(self.taille_plan*408/900), int(self.taille_plan*216/900)), "6":(int(self.taille_plan*408/900), int(self.taille_plan*268/900)), "7":(int(self.taille_plan*408/900), int(self.taille_plan*320/900)), "8":(int(self.taille_plan*408/900), int(self.taille_plan*371/900)), "9":(int(self.taille_plan*616/900), int(self.taille_plan*216/900)), "10":(int(self.taille_plan*616/900), int(self.taille_plan*268/900)), "11":(int(self.taille_plan*616/900), int(self.taille_plan*320/900)), "12":(int(self.taille_plan*616/900), int(self.taille_plan*371/900))}
        self.catalogue_solo = {"15":(int(self.taille_plan*553/900), int(self.taille_plan*580/900)), "20":(int(self.taille_plan*553/900), int(self.taille_plan*648/900)), "30":(int(self.taille_plan*553/900), int(self.taille_plan*714/900))}

    def initParametres(self):
        self.fenetre_param = ouvrirFenetre(self.taille_plan, self.taille_plan)
        self.fenetre_param.afficherImage(0, 0, "Images/parametres.png", self.taille_plan, self.taille_plan)
        self.disque_duel = self.fenetre_param.dessinerDisque(self.catalogue_duel[str(self.nbv_duel)][0], self.catalogue_duel[str(self.nbv_duel)][1], self.rayon_parametre, "#2D221B")
        self.disque_solo = self.fenetre_param.dessinerDisque(self.catalogue_solo[str(self.nbv_solo)][0], self.catalogue_solo[str(self.nbv_solo)][1], self.rayon_parametre, "#2D221B")
        self.engrenage = self.fenetre_param.afficherImage(int(self.taille_plan*850/900) - (self.taille_engrenage/2), int(self.taille_plan*850/900) - (self.taille_engrenage/2), "Images/engrenage.png", self.taille_engrenage, self.taille_engrenage)

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
        if x > int(self.taille_plan*275/900) and x < int(self.taille_plan*375/900) and y > int(self.taille_plan*200/900) and y < int(self.taille_plan*235/900):
            return "5"
        elif x > int(self.taille_plan*275/900) and x < int(self.taille_plan*375/900) and y > int(self.taille_plan*250/900) and y < int(self.taille_plan*285/900):
            return "6"
        elif x > int(self.taille_plan*275/900) and x < int(self.taille_plan*375/900) and y > int(self.taille_plan*300/900) and y < int(self.taille_plan*338/900):
            return "7"
        elif x > int(self.taille_plan*275/900) and x < int(self.taille_plan*375/900) and y > int(self.taille_plan*355/900) and y < int(self.taille_plan*390/900):
            return "8"
        elif x > int(self.taille_plan*480/900) and x < int(self.taille_plan*580/900) and y > int(self.taille_plan*200/900) and y < int(self.taille_plan*235/900):
            return "9"
        elif x > int(self.taille_plan*480/900) and x < int(self.taille_plan*580/900) and y > int(self.taille_plan*250/900) and y < int(self.taille_plan*285/900):
            return "10"
        elif x > int(self.taille_plan*480/900) and x < int(self.taille_plan*580/900) and y > int(self.taille_plan*300/900) and y < int(self.taille_plan*338/900):
            return "11"
        elif x > int(self.taille_plan*480/900) and x < int(self.taille_plan*580/900) and y > int(self.taille_plan*355/900) and y < int(self.taille_plan*390/900):
            return "12"

    def ChoixNbvSolo(self, x, y):
        if x > int(self.taille_plan*385/900) and x < int(self.taille_plan*515/900) and y > int(self.taille_plan*560/900) and y < int(self.taille_plan*605/900):
            return "15"
        elif x > int(self.taille_plan*385/900) and x < int(self.taille_plan*515/900) and y > int(self.taille_plan*625/900) and y < int(self.taille_plan*675/900):
            return "20"
        elif x > int(self.taille_plan*385/900) and x < int(self.taille_plan*515/900) and y > int(self.taille_plan*690/900) and y < int(self.taille_plan*740/900):
            return "30"