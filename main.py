from villes import CreationAleatoireVilles
from parametres import Parametres
from jeu import JeuDuelLogique
from heuristiques import *
from graphisme import *


def Duel(parametres, fenetre):
    villes = CreationAleatoireVilles(parametres.nbv_duel, parametres.taille_ville_duel, parametres.taille_plan, parametres.hauteur_option, "Duel")
    MD = MenuDuelGraphique(villes, fenetre, parametres)
    MD.initPlateau()
    choix_duel = None
    dernier_choix = None
    while choix_duel != "STOP":
        choix_duel = MD.ChoixMenuDuel()
        if choix_duel == "Jeu":
            JL = JeuDuelLogique(villes, parametres.nbj)
            JG = JeuDuelGraphique(villes, MD, JL, parametres)
            JG.initJeuDuel()
            JG.LancerJeuDuel()
        elif choix_duel == "Greedy":
            HG = HeuristiqueGraphique(villes, MD, parametres, HeuristiqueGreedy)
            HG.initHeuristique()
        elif choix_duel == "Cheapest":
            HG = HeuristiqueGraphique(villes, MD, parametres, HeuristiqueCheapestInsertion)
            HG.initHeuristique()
        elif choix_duel == "Recursif":
            HG = HeuristiqueGraphique(villes, MD, parametres, HeuristiqueRecursif)
            HG.initRecursif()
        elif choix_duel == "Dynamique":
            HG = HeuristiqueGraphique(villes, MD, parametres, HeuristiqueDynamique)
            HG.initRecursif()
        elif choix_duel == "2OPT":
            if dernier_choix=="Greedy" or dernier_choix=="Cheapest":
                HG = HeuristiqueGraphique(villes, MD, parametres, Heuristique2OPT, dernier_choix)
                HG.init2OPT()
        dernier_choix = choix_duel


def Solo(parametres, fenetre):
    villes = CreationAleatoireVilles(parametres.nbv_solo, parametres.taille_ville_solo, parametres.taille_plan, parametres.hauteur_option, "Solo")
    JG = JeuSoloGraphique(villes, fenetre, parametres)
    JG.initJeuSolo()
    JG.LancerJeuSolo()


parametres = Parametres()
M = MenuPrincipalGraphique(parametres.taille_plan, parametres.taille_engrenage)
while True:
    M.initMenuPrincipal()
    choix_principal = M.ChoixMenuPrincipal()
    if choix_principal == "Duel":
        Duel(parametres, M.fenetre)
    elif choix_principal == "Solo":
        Solo(parametres, M.fenetre)
    elif choix_principal == "Parametres":
        parametres.initParametres()
        parametres.ChoixParametres()