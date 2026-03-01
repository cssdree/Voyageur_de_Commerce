from heuristiques import *
from villes import Villes
import unittest


class MyTestCase(unittest.TestCase):
    def test_heuristique_gloutonne(self):
        villes = Villes(dict_villes={0:(1,1), 1:(1,4), 2:(6,6), 3:(8,9)}, depart=0)
        self.assertEqual(HeuristiqueGloutonne(villes), [0, 1, 2, 3, 0])
        villes = Villes(dict_villes={0: (1, 1), 1: (1, 4), 2: (6, 6), 3: (8, 9)}, depart=1)
        self.assertEqual(HeuristiqueGloutonne(villes), [1, 0, 2, 3, 1])


if __name__ == '__main__':
    unittest.main()
