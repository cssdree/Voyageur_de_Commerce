from heuristiques import HeuristiqueGreedy, HeuristiqueCheapestInsertion
from tkiteasy import *


class MenuPrincipalGraphique():
    def __init__(self, taille_plan, taille_engrenage):
        self.taille_plan = taille_plan
        self.taille_engrenage = taille_engrenage
        self.fenetre = ouvrirFenetre(self.taille_plan, self.taille_plan)

    def initMenuPrincipal(self):
        try:
            self.fenetre.supprimerTout()
        except Exception:
            pass
        self.fenetre.afficherImage(0, 0, "Images/menu.png", self.taille_plan, self.taille_plan)
        self.engrenage = self.fenetre.afficherImage(850-(self.taille_engrenage/2), 850-(self.taille_engrenage/2), "Images/engrenage.png", self.taille_engrenage, self.taille_engrenage)

    def ChoixMenuPrincipal(self):
        clic = self.fenetre.attendreClic()
        if clic.x > 220 and clic.x < 675 and clic.y > 220 and clic.y < 400:
            return "Duel"
        elif clic.x > 220 and clic.x < 675 and clic.y > 510 and clic.y < 690:
            return "Solo"
        elif self.fenetre.recupererObjet(clic.x, clic.y) == self.engrenage:
            return "Parametres"


class MenuDuelGraphique():
    def __init__(self, villes, fenetre, parametres):
        self.villes = villes
        self.fenetre = fenetre
        self.parametres = parametres

    def initPlateau(self):
        self.fenetre.supprimerTout()
        self.fenetre.afficherImage(0, 0, "Images/fond.png", self.parametres.taille_plan, self.parametres.taille_plan)
        self.initMenuDuel()
        self.initVilles()
        self.initGrenouille()

    def initMenuDuel(self):
        self.choix_jeu = self.fenetre.afficherImage(0 * self.parametres.longueur_option, 0, "Images/jeu.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_greedy = self.fenetre.afficherImage(1 * self.parametres.longueur_option, 0, "Images/greedy.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_cheapest = self.fenetre.afficherImage(2 * self.parametres.longueur_option, 0, "Images/cheapest.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_recursif = self.fenetre.afficherImage(3 * self.parametres.longueur_option, 0, "Images/recursif.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_dynamique = self.fenetre.afficherImage(4 * self.parametres.longueur_option, 0, "Images/dynamique.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_2OPT = self.fenetre.afficherImage(20, self.parametres.taille_plan - self.parametres.hauteur_option + 7, "Images/2_opt.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.fenetre.afficherImage(self.parametres.taille_plan - self.parametres.longueur_option - 20, self.parametres.taille_plan - self.parametres.hauteur_option + 7, "Images/vide.png", self.parametres.longueur_option, self.parametres.hauteur_option)

    def initVilles(self):
        for ville in self.villes.dict:
            self.fenetre.afficherImage(self.villes.dict[ville][0]-(self.parametres.taille_ville_duel/2), self.villes.dict[ville][1]-(self.parametres.taille_ville_duel/2), "Images/nenuphar.png", self.parametres.taille_ville_duel, self.parametres.taille_ville_duel)
        self.fenetre.actualiser()

    def initGrenouille(self):
        self.grenouille = self.fenetre.afficherImage(self.villes.dict[self.villes.depart][0] - (self.parametres.taille_grenouille/2), self.villes.dict[self.villes.depart][1] - (self.parametres.taille_grenouille/1.5), "Images/assis_face.png", self.parametres.taille_grenouille, self.parametres.taille_grenouille)

    def ChoixMenuDuel(self):
        clic = self.fenetre.attendreClic()
        if clic.num == 3:
            return "STOP"
        if self.fenetre.recupererObjet(clic.x, clic.y) == self.choix_jeu:
            return "Jeu"
        elif self.fenetre.recupererObjet(clic.x, clic.y) == self.choix_greedy:
            return "Greedy"
        elif self.fenetre.recupererObjet(clic.x, clic.y) == self.choix_cheapest:
            return "Cheapest"
        elif self.fenetre.recupererObjet(clic.x, clic.y) == self.choix_recursif:
            return "Recursif"
        elif self.fenetre.recupererObjet(clic.x, clic.y) == self.choix_dynamique:
            return "Dynamique"
        elif self.fenetre.recupererObjet(clic.x, clic.y) == self.choix_2OPT:
            return "2OPT"


class JeuDuelGraphique():
    def __init__(self, villes, menu_duel, jeu_duel, parametres):
        self.villes = villes
        self.menu_duel = menu_duel
        self.jeu_duel = jeu_duel
        self.parametres = parametres
        self.fenetre = self.menu_duel.fenetre
        self.grenouilles = {"assis_face":"Images/assis_face.png", "assis_dos":"Images/assis_dos.png", "assis_droite":"Images/assis_droite.png", "assis_gauche":"Images/assis_gauche.png", "saut_face":"Images/saut_face.png", "saut_dos":"Images/saut_dos.png", "saut_droite":"Images/saut_droite.png", "saut_gauche":"Images/saut_gauche.png"}

    def initJeuDuel(self):
        self.fenetre.supprimerTout()
        self.menu_duel.initPlateau()
        self.fenetre.supprimer(self.menu_duel.grenouille)
        self.grenouille = self.fenetre.afficherImage(self.villes.dict[self.villes.depart][0] - (self.parametres.taille_grenouille/2), self.villes.dict[self.villes.depart][1] - (self.parametres.taille_grenouille/1.5), "Images/assis_face.png", self.parametres.taille_grenouille, self.parametres.taille_grenouille)
        self.fenetre.afficherImage(20, self.parametres.taille_plan - self.parametres.hauteur_option + 7, "Images/vide.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.score_joueur_0 = self.fenetre.afficherTexte("0", 20 + (self.parametres.longueur_option/2), (self.parametres.taille_plan - self.parametres.hauteur_option + 7) + (self.parametres.hauteur_option/2) + 5, "#2D221B", 25)
        self.score_joueur_1 = self.fenetre.afficherTexte("0", self.parametres.taille_plan - (self.parametres.longueur_option/2) - 20, (self.parametres.taille_plan - self.parametres.hauteur_option + 7) + (self.parametres.hauteur_option/2) + 5, "#2D221B", 25)

    def LancerJeuDuel(self):
        for idjoueur in range(self.jeu_duel.nbjoueur):
            chemins = []
            while len(self.jeu_duel.joueurs[idjoueur].parcours) < len(self.villes.dict):
                self.ChoixVille(idjoueur)
                self.DeplacerGrenouille(self.villes.dict[self.jeu_duel.joueurs[idjoueur].parcours[-2]], self.villes.dict[self.jeu_duel.joueurs[idjoueur].parcours[-1]])
                chemin = self.AfficherChemin(self.jeu_duel.joueurs[idjoueur].parcours[-2], self.jeu_duel.joueurs[idjoueur].parcours[-1])
                chemins.append(chemin)
                self.fenetre.placerAuDessus(self.grenouille)
                self.AfficherScoreJeu(idjoueur, round(self.jeu_duel.ScoreEnCours(idjoueur)))
            dernier_chemin = self.AfficherChemin(self.jeu_duel.joueurs[idjoueur].parcours[-1], self.villes.depart)
            chemins.append(dernier_chemin)
            self.DeplacerGrenouille(self.villes.dict[self.jeu_duel.joueurs[idjoueur].parcours[-1]], self.villes.dict[self.villes.depart], "fin")
            self.AfficherScoreJeu(idjoueur, round(self.jeu_duel.ScoreFinal(idjoueur)))
            self.fenetre.pause(1)
            for chemin in chemins :
                self.fenetre.supprimer(chemin)

    def ChoixVille(self, idjoueur):
        choix_graphique_ville = self.fenetre.attendreClic()
        choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu_duel.joueurs[idjoueur].visitees)
        while not choix_logique_ville:
            choix_graphique_ville = self.fenetre.attendreClic()
            choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu_duel.joueurs[idjoueur].visitees)
        self.jeu_duel.ChoixVille(idjoueur, int(choix_logique_ville))

    def DeplacerGrenouille(self, old_position, new_position, etape=None):
        nouvelles_grenouilles = self.DirectionGrenouille(old_position, new_position)
        self.fenetre.supprimer(self.grenouille)
        if etape == "fin":
            self.fenetre.pause(0.1)
        self.SauterGrenouille(nouvelles_grenouilles[1], old_position, new_position)
        self.grenouille = self.fenetre.afficherImage(old_position[0], old_position[1], nouvelles_grenouilles[0], self.parametres.taille_grenouille, self.parametres.taille_grenouille)
        self.fenetre.deplacer(self.grenouille, new_position[0] - old_position[0] - (self.parametres.taille_grenouille/2), new_position[1] - old_position[1] - (self.parametres.taille_grenouille/1.5))
        self.fenetre.placerAuDessus(self.grenouille)

    def DirectionGrenouille(self, old_position, new_position):
        dx = new_position[0] - old_position[0]
        dy = new_position[1] - old_position[1]
        if abs(dx) > abs(dy):
            if dx > 0:
                return (self.grenouilles["assis_droite"], self.grenouilles["saut_droite"])
            else:
                return (self.grenouilles["assis_gauche"], self.grenouilles["saut_gauche"])
        else:
            if dy > 0:
                return (self.grenouilles["assis_face"], self.grenouilles["saut_face"])
            else:
                return (self.grenouilles["assis_dos"], self.grenouilles["saut_dos"])

    def SauterGrenouille(self, grenouille_sautante, old_position, new_position):
        self.fenetre.pause(0.1)
        grenouille_en_saut = self.fenetre.afficherImage(((new_position[0] + old_position[0])//2) - (self.parametres.taille_grenouille/2), ((new_position[1] + old_position[1])//2) - (self.parametres.taille_grenouille/1.5), grenouille_sautante, self.parametres.taille_grenouille, self.parametres.taille_grenouille)
        self.fenetre.actualiser()
        self.fenetre.pause(0.2)
        self.fenetre.supprimer(grenouille_en_saut)

    def AfficherChemin(self, old_ville, new_ville):
        chemin = self.fenetre.dessinerLigne(self.villes.dict[old_ville][0], self.villes.dict[old_ville][1], self.villes.dict[new_ville][0], self.villes.dict[new_ville][1], "white", 5)
        self.fenetre.actualiser()
        return chemin

    def AfficherScoreJeu(self, idjoueur, score):
        if idjoueur == 0:
            self.fenetre.changerTexte(self.score_joueur_0, score)
        if idjoueur == 1:
            self.fenetre.changerTexte(self.score_joueur_1, score)
        self.fenetre.actualiser()


class JeuSoloGraphique():
    def __init__(self, villes, fenetre, parametres):
        self.villes = villes
        self.fenetre = fenetre
        self.parametres = parametres
        self.chemins = []
        self.cercle_ville_1 = None
        self.cercle_ville_2 = None

    def initJeuSolo(self):
        self.fenetre.supprimerTout()
        self.fenetre.afficherImage(0, 0, "Images/fond.png", self.parametres.taille_plan, self.parametres.taille_plan)
        self.fenetre.afficherImage(self.parametres.taille_plan - self.parametres.longueur_option - 20, self.parametres.taille_plan - self.parametres.hauteur_option + 7, "Images/vide.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.distance = self.fenetre.afficherTexte("0", self.parametres.taille_plan - (self.parametres.longueur_option/2) - 20, (self.parametres.taille_plan - self.parametres.hauteur_option + 7) + (self.parametres.hauteur_option / 2) + 5, "#2D221B",25)
        self.initVilles()

    def initVilles(self):
        for ville in self.villes.dict:
            self.fenetre.afficherImage(self.villes.dict[ville][0] - (self.parametres.taille_ville_solo/2), self.villes.dict[ville][1] - (self.parametres.taille_ville_solo/2), "Images/nenuphar.png", self.parametres.taille_ville_solo, self.parametres.taille_ville_solo)
        self.fenetre.actualiser()

    def LancerJeuSolo(self):
        self.parcours = HeuristiqueGreedy(self.villes)
        self.DessinerParcours()
        new_distance = round(self.villes.DistanceTotaleParcours(self.parcours))
        self.fenetre.changerTexte(self.distance, new_distance)
        choix_ville_1, choix_ville_2 = self.ChoixVilles()
        while choix_ville_1 and choix_ville_2:
            print(self.parcours)
            self.parcours = PermuterVilles(self.parcours, int(choix_ville_1), int(choix_ville_2))
            print(self.parcours)
            self.DessinerParcours()
            new_distance = round(self.villes.DistanceTotaleParcours(self.parcours))
            self.fenetre.changerTexte(self.distance, new_distance)
            choix_ville_1, choix_ville_2 = self.ChoixVilles()

    def ChoixVilles(self):
        if self.cercle_ville_1:
            self.fenetre.supprimer(self.cercle_ville_1)
        if self.cercle_ville_2:
            self.fenetre.supprimer(self.cercle_ville_2)
        choix_graphique_ville_1 = self.fenetre.attendreClic()
        if choix_graphique_ville_1.num == 3:
            return None, None
        choix_logique_ville_1 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_1.x, choix_graphique_ville_1.y, set())
        while not choix_logique_ville_1:
            choix_graphique_ville_1 = self.fenetre.attendreClic()
            if choix_graphique_ville_1.num == 3:
                return None, None
            choix_logique_ville_1 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_1.x, choix_graphique_ville_1.y, set())
        self.cercle_ville_1 = self.fenetre.dessinerCercle(self.villes.dict[int(choix_logique_ville_1)][0], self.villes.dict[int(choix_logique_ville_1)][1], self.parametres.taille_ville_solo / 1.5, "white")
        choix_graphique_ville_2 = self.fenetre.attendreClic()
        choix_logique_ville_2 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_2.x, choix_graphique_ville_2.y, set())
        while not choix_logique_ville_2:
            choix_graphique_ville_2 = self.fenetre.attendreClic()
            choix_logique_ville_2 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_2.x, choix_graphique_ville_2.y, set())
        self.cercle_ville_2 = self.fenetre.dessinerCercle(self.villes.dict[int(choix_logique_ville_2)][0], self.villes.dict[int(choix_logique_ville_2)][1], self.parametres.taille_ville_solo / 1.5, "white")
        return choix_logique_ville_1, choix_logique_ville_2

    def DessinerParcours(self):
        if len(self.chemins)>0:
            for chemin in self.chemins:
                self.fenetre.supprimer(chemin)
            self.chemins = []
        for posville in range(len(self.parcours)-1):
            chemin = self.fenetre.dessinerLigne(self.villes.dict[self.parcours[posville]][0], self.villes.dict[self.parcours[posville]][1], self.villes.dict[self.parcours[posville+1]][0], self.villes.dict[self.parcours[posville+1]][1], "white", 5)
            self.chemins.append(chemin)


class HeuristiqueGraphique():
    def __init__(self, villes, menu, parametres, Heuristique, dernier_choix=None):
        self.villes = villes
        self.menu = menu
        self.parametres = parametres
        self.Heuristique = Heuristique
        self.dernier_choix = dernier_choix
        self.fenetre = self.menu.fenetre

    def initHeuristique(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours = self.Heuristique(self.villes)
        distance = round(self.villes.DistanceTotaleParcours(parcours))
        self.DessinerParcours(parcours)
        self.fenetre.placerAuDessus(self.menu.grenouille)
        self.AfficherScoreHeuristique(distance)

    def initRecursif(self):
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours_recursif = self.Heuristique(self.villes)
        resultat_recursif = parcours_recursif.ResultatRecursif()
        distance = round(self.villes.DistanceTotaleParcours(resultat_recursif))
        self.DessinerParcours(resultat_recursif)
        self.fenetre.placerAuDessus(self.menu.grenouille)
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
        self.fenetre.placerAuDessus(self.menu.grenouille)
        self.AfficherScoreHeuristique(distance)

    def AfficherScoreHeuristique(self, distance):
        self.fenetre.afficherTexte(distance, self.parametres.taille_plan - (self.parametres.longueur_option/2) - 20,(self.parametres.taille_plan - self.parametres.hauteur_option + 7) + (self.parametres.hauteur_option/2) + 5, "#2D221B", 25)

    def DessinerParcours(self, parcours):
        for posville in range(len(parcours) - 1):
            self.fenetre.dessinerLigne(self.villes.dict[parcours[posville]][0], self.villes.dict[parcours[posville]][1], self.villes.dict[parcours[posville+1]][0], self.villes.dict[parcours[posville+1]][1], "white", 5)


def PermuterVilles(parcours, ville_1, ville_2):
    nouveau_parcours = parcours.copy()
    id1 = nouveau_parcours.index(ville_1)
    id2 = nouveau_parcours.index(ville_2)
    nouveau_parcours[id1], nouveau_parcours[id2] = nouveau_parcours[id2], nouveau_parcours[id1]
    return nouveau_parcours