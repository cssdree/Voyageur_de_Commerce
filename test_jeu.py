import unittest
import math

from jeu import Jeu


class TestJeu(unittest.TestCase):
    def test_partie_1_joueur(self):
        jeu = Jeu(nbjoueur=1, villes=[(0, 0), (1,1), (6,6)])
        jeu.ChoixVille(joueur=1, idville=1)
        jeu.ChoixVille(joueur=1, idville=0)
        jeu.ChoixVille(joueur=1, idville=2)
        self.assertEqual(7*math.sqrt(2), jeu.Score(joueur=1))  # add assertion here


if __name__ == '__main__':
    unittest.main()