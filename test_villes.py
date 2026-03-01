from villes import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_ville_acceptable(self):
        self.assertEqual(VilleAcceptable(c=3, l=3, dict_villes={0:(1,1), 1:(1,4)}), True)
        self.assertEqual(VilleAcceptable(c=1, l=4, dict_villes={0:(1,1), 1:(1,4)}), False)
        self.assertEqual(VilleAcceptable(c=1.2, l=1, dict_villes={0:(1,1), 1:(1,4)}), False)

    def test_trouver_bonne_ville(self):
        villes = Villes(dict_villes={0:(1,1), 1:(1,4), 2:(6,9), 3:(8,3)}, depart=0)
        self.assertEqual(villes.TrouverVille(x=1, y=4), 1)
        self.assertEqual(villes.TrouverVille(x=6.49, y=9), 2)
        self.assertEqual(villes.TrouverVille(x=5, y=5), False)

    def test_trouver_bonne_proche_ville(self):
        villes = Villes(dict_villes={0:(1,1), 1:(1,4), 2:(6,9), 3:(8,3)}, depart=0)
        self.assertEqual(villes.TrouverPlusProcheVille(0, villes_possibles={1, 2, 3}), 1)


if __name__ == '__main__':
    unittest.main()