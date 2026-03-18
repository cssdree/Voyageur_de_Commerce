from villes import CreationAleatoireVilles
from graphisme import MenuGraphique, JeuGraphique
from jeu import JeuLogique


NBJ = 2
NBV = 7
TAILLE_PLAN = 900
TAILLE_VILLE = 120
HAUTEUR_OPTION = 50
LONGUEUR_OPTION = 225


villes = CreationAleatoireVilles(NBV, TAILLE_PLAN, TAILLE_VILLE, HAUTEUR_OPTION)
M = MenuGraphique(TAILLE_PLAN, HAUTEUR_OPTION, LONGUEUR_OPTION)
M.initMenu()
while True:
    choix = M.ChoixMenu()
    if choix == "Jeu":
        L = JeuLogique(villes, NBJ)
        G = JeuGraphique(TAILLE_VILLE, villes, M, L)
        G.initJeu()
        G.LancerJeu()
    elif choix == "Greedy":
        None
    elif choix == "Cheapest":
        None
    elif choix == "Recursif":
        None