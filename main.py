from villes import CreationAleatoireVilles
from jeu import JeuLogique
from heuristiques import *
from graphisme import *


NBJ = 2
NBV = 10
TAILLE_PLAN = 900
TAILLE_VILLE = 110
HAUTEUR_OPTION = 70
LONGUEUR_OPTION = 180
TAILLE_GRENOUILLE = 75


def Duel(nbv, taille_plan, taille_ville, taille_grenouille, hauteur_option, longueur_option, fenetre):
    villes = CreationAleatoireVilles(nbv, taille_plan, taille_ville, hauteur_option)
    MD = MenuDuelGraphique(taille_plan, taille_ville, hauteur_option, longueur_option, taille_grenouille, villes, fenetre)
    MD.initPlateau()
    choix_duel = None
    dernier_choix = None
    while choix_duel != "STOP":
        choix_duel = MD.ChoixMenuDuel()
        if choix_duel == "Jeu":
            JL = JeuLogique(villes, NBJ)
            JG = JeuDuelGraphique(villes, MD, JL)
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


M = MenuPrincipalGraphique(TAILLE_PLAN)
while True:
    M.initMenu()
    choix_principal = M.ChoixMenuPrincipal()
    if choix_principal == "Duel":
        Duel(NBV, TAILLE_PLAN, TAILLE_VILLE, TAILLE_GRENOUILLE, HAUTEUR_OPTION, LONGUEUR_OPTION, M.fenetre)
    #elif choix_principal == "Solo":