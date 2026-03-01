from heuristiques import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_trouver_bonne_plus_proche_ville(self):
        self.assertEqual(TrouverPlusProcheVille(7, 8,{0:(1,1), 1:(1,4), 2:(6,9), 3:(8,3)}), 2)


if __name__ == '__main__':
    unittest.main()