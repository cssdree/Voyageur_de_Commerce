from jeu import Jeu
import unittest
import math


class TestJeu(unittest.TestCase):
    def test_partie_un_joueur(self):
        jeu = Jeu(nbjoueur=1, villes={0:(0, 0), 1:(1,1), 2:(6,6)}, depart=0)
        jeu.ChoixVille(idjoueur=1, idville=1)
        self.assertEqual(math.sqrt(2), jeu.Score(idjoueur=1))
        jeu.ChoixVille(idjoueur=1, idville=2)
        self.assertEqual(6*math.sqrt(2), jeu.Score(idjoueur=1))

    def test_interdiction_revisiter_ville(self):
        jeu = Jeu(nbjoueur=1, villes={0:(0, 0), 1:(1,1), 2:(6,6)}, depart=0)
        jeu.ChoixVille(idjoueur=1, idville=1)
        with self.assertRaises(PermissionError):
            jeu.ChoixVille(idjoueur=1, idville=1)
        jeu.ChoixVille(idjoueur=1, idville=2)
        with self.assertRaises(PermissionError):
            jeu.ChoixVille(idjoueur=1, idville=2)

    #def test_partie_deux_joueur(self):


if __name__ == '__main__':
    unittest.main()