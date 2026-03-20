from villes import CreationAleatoireVilles
from jeu import JeuLogique
from heuristiques import *
from graphisme import *


NBJ = 2
NBV = 12
TAILLE_PLAN = 900
TAILLE_VILLE = 110
HAUTEUR_OPTION = 70
LONGUEUR_OPTION = 180
TAILLE_GRENOUILLE = 75


dernier_choix = None
M = MenuPrincipalGraphique(TAILLE_PLAN)
while True:
    M.initMenu()
    choix_principal = M.ChoixMenuPrincipal()
    if choix_principal == "Duel":
        villes = CreationAleatoireVilles(NBV, TAILLE_PLAN, TAILLE_VILLE, HAUTEUR_OPTION)
        MD = MenuDuelGraphique(TAILLE_PLAN, TAILLE_VILLE, HAUTEUR_OPTION, LONGUEUR_OPTION, TAILLE_GRENOUILLE, villes, M.fenetre)
        MD.initPlateau()
        touche = None
        while touche != "Escape":
            choix_duel = MD.ChoixMenuDuel()
            touche = M.fenetre.recupererTouche()
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
    #elif choix_principal == "Solo":