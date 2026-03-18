from tkiteasy import *


class MenuGraphique():
    def __init__(self, taille, hauteur_option, longueur_option):
        self.taille = taille
        self.hauteur_option = hauteur_option
        self.longueur_option = longueur_option
        self.fenetre = ouvrirFenetre(self.taille, self.taille)


    def initMenu(self):
        self.fenetre.afficherImage(0, 0, "Images/fond.png", self.taille, self.taille)
        self.ChoixJeu = self.fenetre.dessinerRectangle(0*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "white")
        self.ChoixGreedy = self.fenetre.dessinerRectangle(1*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "pink")
        self.ChoixCheapest = self.fenetre.dessinerRectangle(2*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "white")
        self.ChoixRecursif = self.fenetre.dessinerRectangle(3*self.longueur_option, 0, self.longueur_option, self.hauteur_option, "pink")


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
    def __init__(self, taille_ville, villes, menu, jeu):
        self.taille_ville = taille_ville
        self.villes = villes
        self.menu = menu
        self.jeu = jeu
        self.fenetre = self.menu.fenetre


    def initJeu(self):
        self.fenetre.supprimerTout()
        self.menu.initMenu()
        for ville in self.villes.dict:
            if ville == self.villes.depart:
                self.fenetre.dessinerCercle(self.villes.dict[ville][0], self.villes.dict[ville][1], 100, "white")
            self.fenetre.afficherImage(self.villes.dict[ville][0]-(self.taille_ville/2), self.villes.dict[ville][1]-(self.taille_ville/2), "Images/nenuphar.png", self.taille_ville, self.taille_ville)
        self.fenetre.actualiser()


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
        choix_logique_ville = self.villes.TrouverVille(choix_graphique_ville.x, choix_graphique_ville.y)
        while not choix_logique_ville:
            choix_graphique_ville = self.fenetre.attendreClic()
            choix_logique_ville = self.villes.TrouverVille(choix_graphique_ville.x, choix_graphique_ville.y)
        self.jeu.ChoixVille(idjoueur, int(choix_logique_ville))


    def DessinerChemin(self, ancienne_ville, nouvelle_ville):
        chemin = self.fenetre.dessinerLigne(self.villes.dict[ancienne_ville][0], self.villes.dict[ancienne_ville][1], self.villes.dict[nouvelle_ville][0], self.villes.dict[nouvelle_ville][1], "white", 5)
        self.fenetre.actualiser()
        return chemin