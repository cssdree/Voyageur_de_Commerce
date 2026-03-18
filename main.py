from villes import CreationAleatoireVilles
from graphisme import MenuGraphique, JeuGraphique
from jeu import JeuLogique


TAILLE_PLAN = 900
NBJ = 2
NBV = 7


M = MenuGraphique(TAILLE_PLAN)
M.initMenu()
while True:
    choix = M.ChoixMenu()
    if choix=="Jeu" :
        villes = CreationAleatoireVilles(TAILLE_PLAN, NBV)
        L = JeuLogique(villes, NBJ)
        G = JeuGraphique(villes, M.taille, M.fenetre, L, M)
        G.initJeu()
        G.LancerJeu()
