import math

class Jeu():
    def __init__(self, nbjoueur, villes):
        self.nbjoueur = nbjoueur
        self.villes = villes
        self.parcours = []

    def ChoixVille(self, joueur, idville):
        self.parcours.append(self.villes[idville])

    def Score(self, joueur):
        score = 0
        for v in range(1, len(self.parcours)):
            distance = math.dist(self.parcours[v], self.parcours[v-1])
            score += distance
        return score