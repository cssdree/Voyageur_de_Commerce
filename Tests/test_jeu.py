from villes import Villes
from jeu import *
import unittest
import math


class TestJeu(unittest.TestCase):
    def test_partie_un_joueur(self):
        villes = Villes(dict_villes={0:(0, 0), 1:(1,1), 2:(6,6)}, depart=0)
        jeu = Jeu(nbjoueur=1, villes=villes)
        jeu.ChoixVille(idjoueur=0, idville=1)
        self.assertEqual(math.sqrt(2), jeu.ScoreEnCours(idjoueur=0))
        jeu.ChoixVille(idjoueur=0, idville=2)
        self.assertEqual(12*math.sqrt(2), jeu.ScoreFinal(idjoueur=0))

    def test_interdiction_revisiter_ville(self):
        villes = Villes(dict_villes={0:(0, 0), 1:(1,1), 2:(6,6)}, depart=0)
        jeu = Jeu(nbjoueur=1, villes=villes)
        jeu.ChoixVille(idjoueur=0, idville=1)
        with self.assertRaises(PermissionError):
            jeu.ChoixVille(idjoueur=0, idville=1)
        jeu.ChoixVille(idjoueur=0, idville=2)
        with self.assertRaises(PermissionError):
            jeu.ChoixVille(idjoueur=0, idville=2)

    def test_partie_deux_joueur(self):
        villes = Villes(dict_villes={0:(0,0), 1:(2,8), 2:(2,2), 3:(6,6)}, depart=0)
        jeu = Jeu(nbjoueur=2, villes=villes)
        jeu.ChoixVille(idjoueur=0, idville=2)
        jeu.ChoixVille(idjoueur=0, idville=3)
        jeu.ChoixVille(idjoueur=0, idville=1)
        jeu.ChoixVille(idjoueur=1, idville=1)
        jeu.ChoixVille(idjoueur=1, idville=2)
        jeu.ChoixVille(idjoueur=1, idville=3)
        self.assertEqual(6*math.sqrt(2)+2*math.sqrt(5)+2*math.sqrt(17), jeu.ScoreFinal(idjoueur=0))
        self.assertEqual(10*math.sqrt(2)+2*math.sqrt(17)+6, jeu.ScoreFinal(idjoueur=1))
        self.assertEqual(0, jeu.Gagnant())


if __name__ == '__main__':
    unittest.main()