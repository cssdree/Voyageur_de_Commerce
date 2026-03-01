import math


class Jeu():
    def __init__(self, nbjoueur, villes, depart):
        self.nbjoueur = nbjoueur
        self.villes = villes
        self.parcours = [depart]
        self.visitees = {depart}

    def ChoixVille(self, idjoueur, idville):
        if idville in self.visitees:
            raise PermissionError("Ville déjà visitées")
        self.parcours.append(idville)
        self.visitees.add(idville)

    def Score(self, idjoueur):
        score = 0
        for v in range(1, len(self.parcours)):
            distance = math.dist(self.villes[self.parcours[v]], self.villes[self.parcours[v-1]])
            score += distance
        return score