from villes import CreationAleatoireVilles
from jeu import JeuLogique
from heuristiques import *
from graphisme import *


NBJ = 2
NBV = 8
TAILLE_PLAN = 900
TAILLE_VILLE = 110
HAUTEUR_OPTION = 60
LONGUEUR_OPTION = 180


villes = CreationAleatoireVilles(NBV, TAILLE_PLAN, TAILLE_VILLE, HAUTEUR_OPTION)
M = MenuGraphique(TAILLE_PLAN, TAILLE_VILLE, HAUTEUR_OPTION, LONGUEUR_OPTION, villes)
M.initPlateau()
while True:
    choix = M.ChoixMenu()
    if choix == "Jeu":
        JL = JeuLogique(villes, NBJ)
        JG = JeuGraphique(villes, M, JL)
        JG.initJeu()
        JG.LancerJeu()
    elif choix == "Greedy":
        HG = HeuristiqueGraphique(villes, M, HeuristiqueGreedy)
        HG.initHeuristique()
    elif choix == "Cheapest":
        HG = HeuristiqueGraphique(villes, M, HeuristiqueCheapestInsertion)
        HG.initHeuristique()
    elif choix == "Recursif":
        RG = RecursifGraphique(villes, M, ParcoursRecursif)
        RG.initRecursif()