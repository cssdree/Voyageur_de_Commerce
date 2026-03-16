from villes import CreationAleatoireVilles
from graphisme import Graphisme
from jeu import Jeu


TAILLE_PLAN = 900
NBJ = 2
NBV = 7


villes = CreationAleatoireVilles(TAILLE_PLAN, NBV)
jeu = Jeu(NBJ, villes)
graphisme = Graphisme(TAILLE_PLAN, villes)