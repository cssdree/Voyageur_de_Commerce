from villes import CreationAleatoireVilles
from graphisme import Graphisme
from jeu import Jeu


TAILLE_PLAN = 800
NBJ = 2
NBV = 4


villes = CreationAleatoireVilles(TAILLE_PLAN, NBV)
jeu = Jeu(NBJ, villes)
graphisme = Graphisme(TAILLE_PLAN, villes)