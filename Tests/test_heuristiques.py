from heuristiques import *
from villes import Villes
import unittest


class MyTestCase(unittest.TestCase):
    def test_heuristique_gloutonne(self):
        villes = Villes(dict_villes={0:(1,1), 1:(1,4), 2:(6,6), 3:(8,9)}, depart=0)
        self.assertEqual(HeuristiqueGloutonne(villes), [0, 1, 2, 3, 0])
        villes = Villes(dict_villes={0:(1,1), 1:(1,4), 2:(6,6), 3:(8,9)}, depart=1)
        self.assertEqual(HeuristiqueGloutonne(villes), [1, 0, 2, 3, 1])
        villes = Villes(dict_villes={0:(1,5), 1:(4,3), 2:(3,1), 3:(5,9)}, depart=0)
        self.assertEqual(HeuristiqueGloutonne(villes), [0, 1, 2, 3, 0])

    def test_parcours_recursif(self):
        villes = Villes(dict_villes={0:(5,1), 1:(5,2), 2:(5,3), 3:(5,4)}, depart=0)
        parcours_recursif = ParcoursRecursif(villes)
        self.assertEqual(parcours_recursif.ResultatRecursif(), [0, 1, 2, 3, 0])
        villes = Villes(dict_villes={0:(2,2), 1:(4,2), 2:(4,4), 3:(2,4)}, depart=0)
        parcours_recursif = ParcoursRecursif(villes)
        self.assertEqual(parcours_recursif.ResultatRecursif(), [0, 1, 2, 3, 0])

    def test_heuristique_2OPT(self):
        villes = Villes(dict_villes={0:(1,5), 1:(4,3), 2:(3,1), 3:(5,9)}, depart=0)
        parcours = HeuristiqueGloutonne(villes)
        self.assertEqual(Heuristique2OPT(villes, parcours), [0, 2, 1, 3, 0])


if __name__ == '__main__':
    unittest.main()
