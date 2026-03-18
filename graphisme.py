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
        self.ChoixAutre = self.fenetre.afficherImage(4*self.longueur_option, 0, "Images/autre.png", self.longueur_option, self.hauteur_option)
        self.Choix2OPT = self.fenetre.dessinerRectangle(20, 820, 150, 60, "white")
        self.fenetre.dessinerRectangle(730, 820, 150, 60, "white")


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
        self.score_joueur_0 = self.fenetre.afficherTexte("0", 95, 850, "black")
        self.score_joueur_1 = self.fenetre.afficherTexte("0", 805, 850, "Black")


    def LancerJeu(self):
        for idjoueur in range(self.jeu.nbjoueur):
            chemins = []
            while len(self.jeu.joueurs[idjoueur].parcours) < len(self.villes.dict):
                self.ChoixVille(idjoueur)
                chemin = self.AfficherChemin(self.jeu.joueurs[idjoueur].parcours[-2], self.jeu.joueurs[idjoueur].parcours[-1])
                chemins.append(chemin)
                self.AfficherScore(idjoueur, round(self.jeu.ScoreEnCours(idjoueur)))
            dernier_chemin = self.AfficherChemin(self.jeu.joueurs[idjoueur].parcours[-1], self.villes.depart)
            chemins.append(dernier_chemin)
            self.AfficherScore(idjoueur, round(self.jeu.ScoreFinal(idjoueur)))
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


    def AfficherScore(self, idjoueur, score):
        if idjoueur == 0:
            self.fenetre.changerTexte(self.score_joueur_0, score)
        if idjoueur == 1:
            self.fenetre.changerTexte(self.score_joueur_1, score)
        self.fenetre.actualiser()


def DessinerParcours(fenetre, villes, parcours):
    for posville in range(len(parcours)-1):
        fenetre.dessinerLigne(villes.dict[parcours[posville]][0], villes.dict[parcours[posville]][1], villes.dict[parcours[posville+1]][0], villes.dict[parcours[posville+1]][1], "white", 5)



class HeuristiqueGraphique():
    def __init__(self, villes, menu, Heuristique):
        self.villes = villes
        self.menu = menu
        self.Heuristique = Heuristique
        self.fenetre = self.menu.fenetre

    def initHeuristique(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours = self.Heuristique(self.villes)
        distance = round(self.villes.DistanceTotaleParcours(parcours))
        DessinerParcours(self.fenetre, self.villes, parcours)
        self.fenetre.afficherTexte(distance, 805, 850, "black")



class RecursifGraphique():
    def __init__(self, villes, menu, Heuristique):
        self.villes = villes
        self.menu = menu
        self.Heuristique = Heuristique
        self.fenetre = self.menu.fenetre

    def initRecursif(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours_recursif = self.Heuristique(self.villes)
        resultat_recursif = parcours_recursif.ResultatRecursif()
        distance = round(self.villes.DistanceTotaleParcours(resultat_recursif))
        DessinerParcours(self.fenetre, self.villes, resultat_recursif)
        self.fenetre.afficherTexte(distance, 805, 850, "black")