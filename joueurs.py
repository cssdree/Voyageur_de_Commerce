import math


class Joueur():
    def __init__(self, depart):
        self.parcours = [depart]
        self.visitees = {depart}

    def ChoixVille(self, idville):
        if idville in self.visitees:
            raise PermissionError("Ville déjà visitées")
        self.parcours.append(idville)
        self.visitees.add(idville)

    def Score(self, dict_villes):
        score = 0
        for v in range(1, len(self.parcours)):
            distance = math.dist(dict_villes[self.parcours[v]], dict_villes[self.parcours[v-1]])
            score += distance
        return score