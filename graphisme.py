import heuristiques
from tkiteasy import *


class MenuGraphique():
    def __init__(self, taille_plan, taille_ville, hauteur_option, longueur_option, villes):
        self.taille_plan = taille_plan
        self.taille_ville = taille_ville
        self.hauteur_option = hauteur_option
        self.longueur_option = longueur_option
        self.villes = villes
        self.fenetre = ouvrirFenetre(self.taille_plan, self.taille_plan+self.hauteur_option,)


    def initPlateau(self):
        self.fenetre.afficherImage(0, self.hauteur_option, "Images/fond.png", self.taille_plan, self.taille_plan)
        self.initMenu()
        self.initVilles()


    def initMenu(self):
        self.ChoixJeu = self.fenetre.dessinerRectangle(0*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "white")
        self.ChoixGreedy = self.fenetre.dessinerRectangle(1*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "pink")
        self.ChoixCheapest = self.fenetre.dessinerRectangle(2*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "white")
        self.ChoixRecursif = self.fenetre.dessinerRectangle(3*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "pink")


    def initVilles(self):
        for ville in self.villes.dict:
            if ville == self.villes.depart:
                self.fenetre.dessinerCercle(self.villes.dict[ville][0], self.villes.dict[ville][1], 100, "white")
            self.fenetre.afficherImage(self.villes.dict[ville][0]-(self.taille_ville/2), self.villes.dict[ville][1]-(self.taille_ville/2), "Images/nenuphar.png", self.taille_ville, self.taille_ville)
        self.fenetre.actualiser()


    def ChoixMenu(self):
        clic = self.fenetre.attendreClic()
        if self.fenetre.recupererObjet(clic.x, clic.y) == self.ChoixJeu:
            return "Jeu"
        if self.fenetre.recupererObjet(clic.x, clic.y) == self.ChoixGreedy:
            return "Greedy"
        if self.fenetre.recupererObjet(clic.x, clic.y) == self.ChoixCheapest:
            return "Cheapest"
        if self.fenetre.recupererObjet(clic.x, clic.y) == self.ChoixRecursif:
            return "Recursif"



class JeuGraphique():
    def __init__(self, villes, menu, jeu):
        self.villes = villes
        self.menu = menu
        self.jeu = jeu
        self.fenetre = self.menu.fenetre


    def initJeu(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()


    def LancerJeu(self):
        for idjoueur in range(self.jeu.nbjoueur):
            chemins = []
            while len(self.jeu.joueurs[idjoueur].parcours) < len(self.villes.dict):
                self.ChoixVille(idjoueur)
                chemin = self.DessinerChemin(self.jeu.joueurs[idjoueur].parcours[-2], self.jeu.joueurs[idjoueur].parcours[-1])
                chemins.append(chemin)
                print(self.jeu.ScoreEnCours(idjoueur))
            dernier_chemin = self.DessinerChemin(self.jeu.joueurs[idjoueur].parcours[-1], self.villes.depart)
            chemins.append(dernier_chemin)
            print(f"SCORE FINAL : {self.jeu.ScoreFinal(idjoueur)}")
            self.fenetre.pause(2)
            for chemin in chemins :
                self.fenetre.supprimer(chemin)
        print(f"GAGNANT : JOUEUR {self.jeu.Gagnant()+1}")


    def ChoixVille(self, idjoueur):
        choix_graphique_ville = self.fenetre.attendreClic()
        choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu.joueurs[idjoueur].visitees)
        while not choix_logique_ville:
            choix_graphique_ville = self.fenetre.attendreClic()
            choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu.joueurs[idjoueur].visitees)
        self.jeu.ChoixVille(idjoueur, int(choix_logique_ville))


    def DessinerChemin(self, ancienne_ville, nouvelle_ville):
        chemin = self.fenetre.dessinerLigne(self.villes.dict[ancienne_ville][0], self.villes.dict[ancienne_ville][1], self.villes.dict[nouvelle_ville][0], self.villes.dict[nouvelle_ville][1], "white", 5)
        self.fenetre.actualiser()
        return chemin


def DessinerParcours(fenetre, villes, parcours):
    for posville in range(len(parcours)-1):
        fenetre.dessinerLigne(villes.dict[parcours[posville]][0], villes.dict[parcours[posville]][1], villes.dict[parcours[posville+1]][0], villes.dict[parcours[posville+1]][1], "white", 5)



class GreedyGraphique():
    def __init__(self, villes, menu):
        self.villes = villes
        self.menu = menu
        self.fenetre = self.menu.fenetre

    def initGreedy(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours_greedy = heuristiques.HeuristiqueGreedy(self.villes)
        print(parcours_greedy)
        DessinerParcours(self.fenetre, self.villes, parcours_greedy)
        print(self.villes.DistanceTotaleParcours(parcours_greedy))



class CheapestGraphique():
    def __init__(self, villes, menu):
        self.villes = villes
        self.menu = menu
        self.fenetre = self.menu.fenetre

    def initCheapest(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours_cheap = heuristiques.HeuristiqueCheapestInsertion(self.villes)
        print(parcours_cheap)
        DessinerParcours(self.fenetre, self.villes, parcours_cheap)
        print(self.villes.DistanceTotaleParcours(parcours_cheap))



class RecursifGraphique():
    def __init__(self, villes, menu):
        self.villes = villes
        self.menu = menu
        self.fenetre = self.menu.fenetre

    def initRecursif(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours_recursif = heuristiques.ParcoursRecursif(self.villes)
        resultat_recursif = parcours_recursif.ResultatRecursif()
        print(resultat_recursif)
        DessinerParcours(self.fenetre, self.villes, resultat_recursif)
        print(self.villes.DistanceTotaleParcours(resultat_recursif))