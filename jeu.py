from joueurs import Joueur
import math


class Jeu():
    def __init__(self, nbjoueur, villes, depart):
        self.nbjoueur = nbjoueur
        self.villes = villes
        self.joueurs = {}
        for j in range(self.nbjoueur):
            self.joueurs[j] = Joueur(0)

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