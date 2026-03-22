from villes import CreationAleatoireVilles
from parametres import Parametres
from jeu import JeuLogique
from heuristiques import *
from graphisme import *


def Duel(parametres, fenetre):
    villes = CreationAleatoireVilles(parametres)
    MD = MenuDuelGraphique(parametres, villes, fenetre)
    MD.initPlateau()
    choix_duel = None
    dernier_choix = None
    while choix_duel != "STOP":
        choix_duel = MD.ChoixMenuDuel()
        if choix_duel == "Jeu":
            JL = JeuLogique(villes, parametres.nbj)
            JG = JeuDuelGraphique(villes, parametres, MD, JL)
            JG.initJeu()
            JG.LancerJeu()
        elif choix_duel == "Greedy":
            HG = HeuristiqueGraphique(villes, MD, HeuristiqueGreedy)
            HG.initHeuristique()
        elif choix_duel == "Cheapest":
            HG = HeuristiqueGraphique(villes, MD, HeuristiqueCheapestInsertion)
            HG.initHeuristique()
        elif choix_duel == "Recursif":
            HG = HeuristiqueGraphique(villes, MD, ParcoursRecursif)
            HG.initRecursif()
        elif choix_duel == "2OPT":
            if dernier_choix=="Greedy" or dernier_choix=="Cheapest":
                HG = HeuristiqueGraphique(villes, MD, Heuristique2OPT, dernier_choix)
                HG.init2OPT()
        dernier_choix = choix_duel


parametres = Parametres()
M = MenuPrincipalGraphique(parametres.taille_plan)
while True:
    M.initMenuPrincipal()
    choix_principal = M.ChoixMenuPrincipal()
    if choix_principal == "Duel":
        Duel(parametres, M.fenetre)
    #elif choix_principal == "Solo":
    elif choix_principal == "Parametres":
        parametres.initParametres()