from tkiteasy import *


TAILLE_VILLE = 110
LONGUEUR_OPTION = 225
HAUTEUR_OPTION = 50


class MenuGraphique():
    def __init__(self, taille):
        self.taille = taille
        self.fenetre = ouvrirFenetre(self.taille, self.taille)

    def initMenu(self):
        self.fenetre.afficherImage(0, 0, "Images/fond.png", 900, 900)
        self.fenetre.dessinerLigne(0, 100, 900, 100, "white", 10)
        self.ChoixJeu = self.fenetre.dessinerRectangle(0*LONGUEUR_OPTION, 0, LONGUEUR_OPTION, HAUTEUR_OPTION, "white")
        self.ChoixGreedy = self.fenetre.dessinerRectangle(1*LONGUEUR_OPTION, 0, LONGUEUR_OPTION, HAUTEUR_OPTION, "pink")
        self.ChoixCheapest = self.fenetre.dessinerRectangle(2*LONGUEUR_OPTION, 0, LONGUEUR_OPTION, HAUTEUR_OPTION, "blue")
        self.ChoixRecursif = self.fenetre.dessinerRectangle(3*LONGUEUR_OPTION, 0, LONGUEUR_OPTION, HAUTEUR_OPTION, "green")

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
    def __init__(self, villes, taille, fenetre, jeu, menu):
        self.taille = taille
        self.villes = villes
        self.fenetre = fenetre
        self.jeu = jeu
        self.menu = menu

    def initJeu(self):
        self.fenetre.supprimerTout()
        self.menu.initMenu()
        for ville in self.villes.dict:
            if ville == self.villes.depart:
                self.fenetre.dessinerCercle(self.villes.dict[ville][0], self.villes.dict[ville][1], 100, "white")
            self.fenetre.afficherImage(self.villes.dict[ville][0]-(TAILLE_VILLE/2), self.villes.dict[ville][1]-(TAILLE_VILLE/2), "Images/nenuphar.png", TAILLE_VILLE, TAILLE_VILLE)
        self.fenetre.actualiser()

    def LancerJeu(self):
        for idjoueur in range(self.jeu.nbjoueur):
            chemins = []
            while len(self.jeu.joueurs[idjoueur].parcours) < len(self.villes.dict):
                choix_graphique_ville = self.fenetre.attendreClic()
                choix_logique_ville = self.villes.TrouverVille(choix_graphique_ville.x, choix_graphique_ville.y)
                while not choix_logique_ville:
                    choix_graphique_ville = self.fenetre.attendreClic()
                    choix_logique_ville = self.villes.TrouverVille(choix_graphique_ville.x, choix_graphique_ville.y)
                self.jeu.ChoixVille(idjoueur, int(choix_logique_ville))
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

    def DessinerChemin(self, ancienne_ville, nouvelle_ville):
        chemin = self.fenetre.dessinerLigne(self.villes.dict[ancienne_ville][0], self.villes.dict[ancienne_ville][1], self.villes.dict[nouvelle_ville][0], self.villes.dict[nouvelle_ville][1], "white", 5)
        self.fenetre.actualiser()
        return chemin

