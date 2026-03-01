import random
import math


class Villes():
    def __init__(self, dict_villes, depart):
        self.dict = dict_villes
        self.depart = depart
        self.ids = list(self.dict.keys())
        self.coords = list(self.dict.values())

    def TrouverVille(self, x, y):
        for idville in self.dict:
            if math.dist((x,y), self.dict[idville]) < 0.5:
                return idville
        return False

    def TrouverPlusProcheVille(self, c, l):
        nearest = random.choice(self.ids)
        for idville in self.dict:
            if math.dist((c, l), self.dict[idville]) < math.dist((c, l), self.dict[nearest]):
                nearest = self.dict[idville]
        return nearest


def VilleAcceptable(c, l, dict_villes):
    coords = set(dict_villes.values())
    if (c, l) in coords:
        return False
    for coord in coords:
        if math.dist((c, l), coord) < 1:
            return False
    return True


def CreationAleatoireVilles(taille_plan, nbville):
    dict_villes = {}
    v = 0
    while len(dict_villes) < nbville:
        c = round(random.uniform(0,taille_plan-0.8), 3)
        l = round(random.uniform(0,taille_plan-0.8), 3)
        coord = (c, l)
        if VilleAcceptable(c, l, dict_villes):
            dict_villes[v] = coord
            v += 1
    depart = random.randrange(0,len(dict_villes))
    return Villes(dict_villes, depart)