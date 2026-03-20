from heuristiques import HeuristiqueGreedy, HeuristiqueCheapestInsertion
from tkiteasy import *


class MenuGraphique():
    def __init__(self, taille_plan, taille_ville, hauteur_option, longueur_option, villes):
        self.taille_plan = taille_plan
        self.taille_ville = taille_ville
        self.hauteur_option = hauteur_option
        self.longueur_option = longueur_option
        self.villes = villes
        self.fenetre = ouvrirFenetre(self.taille_plan, self.taille_plan)


    def initPlateau(self):
        self.fenetre.afficherImage(0, 0, "Images/fond.png", self.taille_plan, self.taille_plan)
        self.initMenu()
        self.initVilles()


    def initMenu(self):
        self.ChoixJeu = self.fenetre.afficherImage(0*self.longueur_option, 0, "Images/jeu.png", self.longueur_option, self.hauteur_option)
        self.ChoixGreedy = self.fenetre.afficherImage(1*self.longueur_option, 0, "Images/greedy.png", self.longueur_option, self.hauteur_option)
        self.ChoixCheapest = self.fenetre.afficherImage(2*self.longueur_option, 0, "Images/cheapest.png", self.longueur_option, self.hauteur_option)
        self.ChoixRecursif = self.fenetre.afficherImage(3*self.longueur_option, 0, "Images/recursif.png", self.longueur_option, self.hauteur_option)
        self.ChoixDynamique = self.fenetre.afficherImage(4*self.longueur_option, 0, "Images/dynamique.png", self.longueur_option, self.hauteur_option)
        self.Choix2OPT = self.fenetre.afficherImage(20, self.taille_plan - self.hauteur_option + 7, "Images/2_opt.png", self.longueur_option, self.hauteur_option)
        self.fenetre.afficherImage(self.taille_plan - self.longueur_option - 20, self.taille_plan - self.hauteur_option + 7, "Images/vide.png", self.longueur_option, self.hauteur_option)


    def initVilles(self):
        for ville in self.villes.dict:
            if ville == self.villes.depart:
                self.fenetre.dessinerCercle(self.villes.dict[ville][0], self.villes.dict[ville][1], 80, "white")
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
        if self.fenetre.recupererObjet(clic.x, clic.y) == self.Choix2OPT:
            return "2OPT"



class JeuGraphique():
    def __init__(self, villes, menu, jeu):
        self.villes = villes
        self.menu = menu
        self.jeu = jeu
        self.fenetre = self.menu.fenetre


    def initJeu(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        self.fenetre.afficherImage(20, self.menu.taille_plan - self.menu.hauteur_option + 7, "Images/vide.png", self.menu.longueur_option, self.menu.hauteur_option)
        self.score_joueur_0 = self.fenetre.afficherTexte("0", 20 + (self.menu.longueur_option/2), (self.menu.taille_plan - self.menu.hauteur_option + 7) + (self.menu.hauteur_option/2) + 5, "#2D221B", 25)
        self.score_joueur_1 = self.fenetre.afficherTexte("0", self.menu.taille_plan - (self.menu.longueur_option/2) - 20, (self.menu.taille_plan - self.menu.hauteur_option + 7) + (self.menu.hauteur_option/2) + 5, "#2D221B", 25)


    def LancerJeu(self):
        for idjoueur in range(self.jeu.nbjoueur):
            chemins = []
            while len(self.jeu.joueurs[idjoueur].parcours) < len(self.villes.dict):
                self.ChoixVille(idjoueur)
                chemin = self.AfficherChemin(self.jeu.joueurs[idjoueur].parcours[-2], self.jeu.joueurs[idjoueur].parcours[-1])
                chemins.append(chemin)
                self.AfficherScoreJeu(idjoueur, round(self.jeu.ScoreEnCours(idjoueur)))
            dernier_chemin = self.AfficherChemin(self.jeu.joueurs[idjoueur].parcours[-1], self.villes.depart)
            chemins.append(dernier_chemin)
            self.AfficherScoreJeu(idjoueur, round(self.jeu.ScoreFinal(idjoueur)))
            self.fenetre.pause(1)
            for chemin in chemins :
                self.fenetre.supprimer(chemin)


    def ChoixVille(self, idjoueur):
        choix_graphique_ville = self.fenetre.attendreClic()
        choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu.joueurs[idjoueur].visitees)
        while not choix_logique_ville:
            choix_graphique_ville = self.fenetre.attendreClic()
            choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu.joueurs[idjoueur].visitees)
        self.jeu.ChoixVille(idjoueur, int(choix_logique_ville))


    def AfficherChemin(self, ancienne_ville, nouvelle_ville):
        chemin = self.fenetre.dessinerLigne(self.villes.dict[ancienne_ville][0], self.villes.dict[ancienne_ville][1], self.villes.dict[nouvelle_ville][0], self.villes.dict[nouvelle_ville][1], "white", 5)
        self.fenetre.actualiser()
        return chemin


    def AfficherScoreJeu(self, idjoueur, score):
        if idjoueur == 0:
            self.fenetre.changerTexte(self.score_joueur_0, score)
        if idjoueur == 1:
            self.fenetre.changerTexte(self.score_joueur_1, score)
        self.fenetre.actualiser()



class HeuristiqueGraphique():
    def __init__(self, villes, menu, Heuristique, dernier_choix=None):
        self.villes = villes
        self.menu = menu
        self.Heuristique = Heuristique
        self.dernier_choix = dernier_choix
        self.fenetre = self.menu.fenetre

    def initHeuristique(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours = self.Heuristique(self.villes)
        distance = round(self.villes.DistanceTotaleParcours(parcours))
        self.DessinerParcours(parcours)
        self.AfficherScoreHeuristique(distance)

    def initRecursif(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours_recursif = self.Heuristique(self.villes)
        resultat_recursif = parcours_recursif.ResultatRecursif()
        distance = round(self.villes.DistanceTotaleParcours(resultat_recursif))
        self.DessinerParcours(resultat_recursif)
        self.AfficherScoreHeuristique(distance)

    def init2OPT(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        if self.dernier_choix == "Greedy":
            parcours = HeuristiqueGreedy(self.villes)
        elif self.dernier_choix == "Cheapest":
            parcours = HeuristiqueCheapestInsertion(self.villes)
        parcours_ameliore = self.Heuristique(self.villes, parcours)
        distance = round(self.villes.DistanceTotaleParcours(parcours_ameliore))
        self.DessinerParcours(parcours_ameliore)
        self.AfficherScoreHeuristique(distance)

    def DessinerParcours(self, parcours):
        for posville in range(len(parcours) - 1):
            self.fenetre.dessinerLigne(self.villes.dict[parcours[posville]][0], self.villes.dict[parcours[posville]][1], self.villes.dict[parcours[posville + 1]][0], self.villes.dict[parcours[posville + 1]][1], "white", 5)

    def AfficherScoreHeuristique(self, distance):
        self.fenetre.afficherTexte(distance, self.menu.taille_plan - (self.menu.longueur_option / 2) - 20, (self.menu.taille_plan - self.menu.hauteur_option + 7) + (self.menu.hauteur_option / 2) + 5, "#2D221B", 25)