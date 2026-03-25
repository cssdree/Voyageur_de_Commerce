import random
import math


class Villes():
    def __init__(self, dict_villes, depart, taille_ville=0):
        self.taille_ville = taille_ville
        self.dict = dict_villes
        self.depart = depart
        self.villes_initiales_possibles = set(self.dict.keys()) - {self.depart}

    def TrouverVilleAcceptable(self, x, y, visitees):
        for idville in self.dict:
            if (math.dist((x,y), self.dict[idville]) < (self.taille_ville/2.5)):
                if idville not in visitees:
                    return str(idville)
                return False
        return False

    def TrouverPlusProcheVille(self, ville_actuelle, villes_possibles):
        nearest = random.choice(list(villes_possibles))
        for idville in villes_possibles:
            if math.dist(self.dict[ville_actuelle], self.dict[idville]) < math.dist(self.dict[ville_actuelle], self.dict[nearest]):
                nearest = idville
        return nearest

    def DistanceTotaleParcours(self, parcours):
        distance = 0
        for v in range(1, len(parcours)):
            distance += math.dist(self.dict[parcours[v]], self.dict[parcours[v-1]])
        return distance

    def Distance(self, idville1, idville2):
        return math.dist(self.dict[idville1], self.dict[idville2])


def VilleAcceptable(x, y, dict_villes, taille_ville, hauteur_option):
    coords = set(dict_villes.values())
    if VilleDansTriangle((x, y), (0, 450), (0, 900), (500, 900)) or VilleDansTriangle((x, y), (900, 200), (700, 450), (900, 650)):
        return False
    if VilleDansOptions(y, hauteur_option) or VilleDansRondins(x, y):
        return False
    if (x, y) in coords:
        return False
    for coord in coords:
        if math.dist((x, y), coord) < taille_ville+(taille_ville/2):
            return False
    return True


def VilleDansTriangle(ville, a, b, c):
    def signe(p1, p2, p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1])-(p2[0]-p3[0])*(p1[1]-p3[1])
    d1 = signe(ville, a, b)
    d2 = signe(ville, b, c)
    d3 = signe(ville, c, a)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)


def VilleDansOptions(y, hauteur_option):
    return y < hauteur_option*1.5


def VilleDansRondins(x, y):
    return (x > 690) and (y > 790)


def CreationAleatoireVilles(parametres):
    dict_villes = {}
    v = 0
    while len(dict_villes) < parametres.nbv_duel:
        x = round(random.uniform(parametres.taille_ville, parametres.taille_plan-parametres.taille_ville), 3)
        y = round(random.uniform(parametres.taille_ville, parametres.taille_plan-parametres.taille_ville), 3)
        coord = (x, y)
        if VilleAcceptable(x, y, dict_villes, parametres.taille_ville, parametres.hauteur_option):
            dict_villes[v] = coord
            v += 1
    depart = random.randrange(0,len(dict_villes))
    return Villes(dict_villes, depart, parametres.taille_ville)