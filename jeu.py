from joueurs import Joueur
import math


class Jeu():
    def __init__(self, nbjoueur, villes):
        self.nbjoueur = nbjoueur
        self.villes = villes
        self.joueurs = {}
        for j in range(self.nbjoueur):
            self.joueurs[j] = Joueur(self.villes.depart)

    def TrouverVille(self, x, y):
        for idville in self.villes.dict:
            if math.dist((x,y), self.villes.dict[idville]) < 0.5:
                return idville
        return False

    def ChoixVille(self, idjoueur, idville):
        self.joueurs[idjoueur].ChoixVille(idville)

    def Score(self, idjoueur):
        return self.joueurs[idjoueur].Score(self.villes.dict)

    def Gagnant(self):
        scores = {}
        for j in range(self.nbjoueur):
            score = self.Score(j)
            scores[score] = j
        best_score = min(list(scores.keys()))
        return scores[best_score]