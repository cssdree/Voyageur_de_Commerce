from joueurs import Joueur
import random
import math


class Jeu():
    def __init__(self, nbjoueur, villes, depart):
        self.nbjoueur = nbjoueur
        self.villes = villes
        self.joueurs = {}
        for j in range(self.nbjoueur):
            self.joueurs[j] = Joueur(depart)

    def TrouverVille(self, x, y):
        for idville in self.villes:
            if math.dist((x,y), self.villes[idville]) < 0.5:
                return idville
        return False

    def ChoixVille(self, idjoueur, idville):
        self.joueurs[idjoueur].ChoixVille(idville)

    def Score(self, idjoueur):
        return self.joueurs[idjoueur].Score(self.villes)

    def Gagnant(self):
        scores = {}
        for j in range(self.nbjoueur):
            score = self.Score(j)
            scores[score] = j
        best_score = min(list(scores.keys()))
        return scores[best_score]


def CreationAleatoireVilles(taille_plan, nbville):
    villes = {}
    v = 0
    while len(villes) < nbville:
        c = round(random.uniform(0,taille_plan-0.8), 3)
        l = round(random.uniform(0,taille_plan-0.8), 3)
        coord = (c, l)
        if VilleAcceptable(c, l, villes):
            villes[v] = coord
            v += 1
    depart = random.randrange(0,len(villes))
    return villes, depart


def VilleAcceptable(c, l, villes):
    coord_villes = set(villes.values())
    if (c, l) in coord_villes:
        return False
    for coord_ville in coord_villes:
        if math.dist((c, l), coord_ville) < 1:
            return False
    return True