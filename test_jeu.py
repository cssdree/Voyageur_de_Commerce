from jeu import Jeu, VilleAcceptable
import unittest
import math


class TestJeu(unittest.TestCase):
    def test_partie_un_joueur(self):
        jeu = Jeu(nbjoueur=1, villes={0:(0, 0), 1:(1,1), 2:(6,6)}, depart=0)
        jeu.ChoixVille(idjoueur=0, idville=1)
        self.assertEqual(math.sqrt(2), jeu.Score(idjoueur=0))
        jeu.ChoixVille(idjoueur=0, idville=2)
        self.assertEqual(6*math.sqrt(2), jeu.Score(idjoueur=0))

    def test_interdiction_revisiter_ville(self):
        jeu = Jeu(nbjoueur=1, villes={0:(0, 0), 1:(1,1), 2:(6,6)}, depart=0)
        jeu.ChoixVille(idjoueur=0, idville=1)
        with self.assertRaises(PermissionError):
            jeu.ChoixVille(idjoueur=0, idville=1)
        jeu.ChoixVille(idjoueur=0, idville=2)
        with self.assertRaises(PermissionError):
            jeu.ChoixVille(idjoueur=0, idville=2)

    def test_partie_deux_joueur(self):
        jeu = Jeu(nbjoueur=2, villes={0:(0, 0), 1:(1, 1), 2:(6, 6), 3:(8,8)}, depart=0)
        jeu.ChoixVille(idjoueur=0, idville=3)
        jeu.ChoixVille(idjoueur=0, idville=2)
        jeu.ChoixVille(idjoueur=0, idville=1)
        jeu.ChoixVille(idjoueur=1, idville=1)
        jeu.ChoixVille(idjoueur=1, idville=2)
        jeu.ChoixVille(idjoueur=1, idville=3)
        self.assertEqual(15*math.sqrt(2), jeu.Score(idjoueur=0))
        self.assertEqual(8*math.sqrt(2), jeu.Score(idjoueur=1))
        self.assertEqual(1, jeu.Gagnant())

    def test_ville_acceptable(self):
        self.assertEqual(VilleAcceptable(3, 3, {0:(1,1), 1:(1,4)}), True)
        self.assertEqual(VilleAcceptable(1, 4, {0:(1,1), 1:(1,4)}), False)
        self.assertEqual(VilleAcceptable(1.2,1, {0:(1,1), 1:(1,4)}), False)

    def test_trouver_bonne_ville(self):
        jeu = Jeu(nbjoueur=2, villes={0:(1,1), 1:(1,4), 2:(6,9), 3:(8,3)}, depart=0)
        self.assertEqual(jeu.TrouverVille(1,4), 1)
        self.assertEqual(jeu.TrouverVille(6.49, 9), 2)
        self.assertEqual(jeu.TrouverVille(5,5), False)

if __name__ == '__main__':
    unittest.main()