from heuristiques import HeuristiqueGreedy, HeuristiqueCheapestInsertion
from tkiteasy import *


class MenuPrincipalGraphique():
    def __init__(self, taille_plan, taille_engrenage):
        self.taille_plan = taille_plan
        self.taille_engrenage = taille_engrenage
        self.fenetre = ouvrirFenetre(self.taille_plan, self.taille_plan)

    def initMenuPrincipal(self):
        """
        Nettoie la fenêtre et affiche l'image de fond du menu et l'icône des paramètres.
        """
        try:
            self.fenetre.supprimerTout()
        except Exception:
            pass
        self.fenetre.afficherImage(0, 0, "Images/menu.png", self.taille_plan, self.taille_plan)
        self.engrenage = self.fenetre.afficherImage(int(self.taille_plan*850/900)-(self.taille_engrenage/2), int(self.taille_plan*850/900)-(self.taille_engrenage/2), "Images/engrenage.png", self.taille_engrenage, self.taille_engrenage)

    def ChoixMenuPrincipal(self):
        """
        Attend un clic de l'utilisateur et renvoie le mode de jeu ou l'action sélectionnée.
        """
        clic = self.fenetre.attendreClic()
        if clic.x > int(self.taille_plan*220/900) and clic.x < int(self.taille_plan*675/900) and clic.y > int(self.taille_plan*220/900) and clic.y < int(self.taille_plan*400/900):
            return "Duel"
        elif clic.x > int(self.taille_plan*220/900) and clic.x < int(self.taille_plan*675/900) and clic.y > int(self.taille_plan*510/900) and clic.y < int(self.taille_plan*690/900):
            return "Solo"
        elif self.fenetre.recupererObjet(clic.x, clic.y) == self.engrenage:
            return "Parametres"


class MenuDuelGraphique():
    def __init__(self, villes, fenetre, parametres):
        self.villes = villes
        self.fenetre = fenetre
        self.parametres = parametres

    def initPlateau(self):
        """
        Prépare l'affichage du plateau de jeu incluant le fond, les boutons et les nénuphars.
        """
        self.fenetre.supprimerTout()
        self.fenetre.afficherImage(0, 0, "Images/fond.png", self.parametres.taille_plan, self.parametres.taille_plan)
        self.initMenuDuel()
        self.initVilles()
        self.initGrenouille()

    def initMenuDuel(self):
        """
        Affiche les icônes interactives permettant de choisir les différentes heuristiques ou le jeu duel.
        """
        self.choix_jeu = self.fenetre.afficherImage(0*self.parametres.longueur_option, 0, "Images/jeu.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_greedy = self.fenetre.afficherImage(1*self.parametres.longueur_option, 0, "Images/greedy.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_cheapest = self.fenetre.afficherImage(2*self.parametres.longueur_option, 0, "Images/cheapest.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_recursif = self.fenetre.afficherImage(3*self.parametres.longueur_option, 0, "Images/recursif.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_dynamique = self.fenetre.afficherImage(4*self.parametres.longueur_option, 0, "Images/dynamique.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.choix_2OPT = self.fenetre.afficherImage(int(self.parametres.taille_plan*20/900), self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900), "Images/2_opt.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.fenetre.afficherImage(self.parametres.taille_plan - self.parametres.longueur_option - int(self.parametres.taille_plan*20/900), self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900), "Images/vide.png", self.parametres.longueur_option, self.parametres.hauteur_option)

    def initVilles(self):
        """
        Dessine chaque nénuphar sur la carte aux coordonnées correspondantes du dictionnaire de villes.
        """
        for ville in self.villes.dict:
            self.fenetre.afficherImage(self.villes.dict[ville][0]-(self.parametres.taille_ville_duel/2), self.villes.dict[ville][1]-(self.parametres.taille_ville_duel/2), "Images/nenuphar.png", self.parametres.taille_ville_duel, self.parametres.taille_ville_duel)
        self.fenetre.actualiser()

    def initGrenouille(self):
        """
        Place l'image de la grenouille sur la ville définie comme point de départ.
        """
        self.grenouille = self.fenetre.afficherImage(self.villes.dict[self.villes.depart][0] - (self.parametres.taille_grenouille/2), self.villes.dict[self.villes.depart][1] - (self.parametres.taille_grenouille/1.5), "Images/assis_face.png", self.parametres.taille_grenouille, self.parametres.taille_grenouille)

    def ChoixMenuDuel(self):
        """
        Gère les interactions avec le menu du mode duel et retourne l'action choisie par l'utilisateur.
        """
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
        """
        Prépare l'affichage spécifique au début d'une partie de jeu duel.
        """
        self.fenetre.supprimerTout()
        self.menu_duel.initPlateau()
        self.fenetre.supprimer(self.menu_duel.grenouille)
        self.grenouille = self.fenetre.afficherImage(self.villes.dict[self.villes.depart][0] - (self.parametres.taille_grenouille/2), self.villes.dict[self.villes.depart][1] - (self.parametres.taille_grenouille/1.5), "Images/assis_face.png", self.parametres.taille_grenouille, self.parametres.taille_grenouille)
        self.fenetre.afficherImage(int(self.parametres.taille_plan*20/900), self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900), "Images/vide.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.score_joueur_0 = self.fenetre.afficherTexte("0", int(self.parametres.taille_plan*20/900) + (self.parametres.longueur_option/2), (self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900)) + (self.parametres.hauteur_option/2) + int(self.parametres.taille_plan*5/900), "#2D221B", int(self.parametres.taille_plan*25/900))
        self.score_joueur_1 = self.fenetre.afficherTexte("0", self.parametres.taille_plan - (self.parametres.longueur_option/2) - int(self.parametres.taille_plan*20/900), (self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900)) + (self.parametres.hauteur_option/2) + int(self.parametres.taille_plan*5/900), "#2D221B", int(self.parametres.taille_plan*25/900))

    def LancerJeuDuel(self):
        """
        Gère la boucle principale du jeu duel, incluant les clics, les déplacements et l'affichage des chemins.
        """
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
        """
        Attend un clic valide sur un nénuphar non visité pour enregistrer le coup du joueur.
        """
        choix_graphique_ville = self.fenetre.attendreClic()
        choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu_duel.joueurs[idjoueur].visitees)
        while not choix_logique_ville:
            choix_graphique_ville = self.fenetre.attendreClic()
            choix_logique_ville = self.villes.TrouverVilleAcceptable(choix_graphique_ville.x, choix_graphique_ville.y, self.jeu_duel.joueurs[idjoueur].visitees)
        self.jeu_duel.ChoixVille(idjoueur, int(choix_logique_ville))

    def DeplacerGrenouille(self, old_position, new_position, etape=None):
        """
        Réalise l'animation complète du déplacement de la grenouille entre deux points.
        """
        nouvelles_grenouilles = self.DirectionGrenouille(old_position, new_position)
        self.fenetre.supprimer(self.grenouille)
        if etape == "fin":
            self.fenetre.pause(0.1)
        self.SauterGrenouille(nouvelles_grenouilles[1], old_position, new_position)
        self.grenouille = self.fenetre.afficherImage(old_position[0], old_position[1], nouvelles_grenouilles[0], self.parametres.taille_grenouille, self.parametres.taille_grenouille)
        self.fenetre.deplacer(self.grenouille, new_position[0] - old_position[0] - (self.parametres.taille_grenouille/2), new_position[1] - old_position[1] - (self.parametres.taille_grenouille/1.5))
        self.fenetre.placerAuDessus(self.grenouille)

    def DirectionGrenouille(self, old_position, new_position):
        """
        Sélectionne les images de la grenouille (assise et saut) en fonction de l'orientation du mouvement.
        """
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
        """
        Affiche brièvement l'image de la grenouille en l'air à mi-chemin du déplacement pour simuler un saut.
        """
        self.fenetre.pause(0.1)
        grenouille_en_saut = self.fenetre.afficherImage(((new_position[0] + old_position[0])//2) - (self.parametres.taille_grenouille/2), ((new_position[1] + old_position[1])//2) - (self.parametres.taille_grenouille/1.5), grenouille_sautante, self.parametres.taille_grenouille, self.parametres.taille_grenouille)
        self.fenetre.actualiser()
        self.fenetre.pause(0.2)
        self.fenetre.supprimer(grenouille_en_saut)

    def AfficherChemin(self, old_ville, new_ville):
        """
        Trace une ligne blanche représentant le chemin parcouru entre deux nénuphars.
        """
        chemin = self.fenetre.dessinerLigne(self.villes.dict[old_ville][0], self.villes.dict[old_ville][1], self.villes.dict[new_ville][0], self.villes.dict[new_ville][1], "white", 5)
        self.fenetre.actualiser()
        return chemin

    def AfficherScoreJeu(self, idjoueur, score):
        """
        Met à jour l'affichage numérique du score pour le joueur spécifié.
        """
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
        self.cercle_ville_en_cours = None

    def initJeuSolo(self):
        """
        Prépare l'affichage spécifique au début d'une partie de jeu solo incluant le fond, les villes et le compteur de distance.
        """
        self.fenetre.supprimerTout()
        self.fenetre.afficherImage(0, 0, "Images/fond.png", self.parametres.taille_plan, self.parametres.taille_plan)
        self.fenetre.afficherImage(self.parametres.taille_plan - self.parametres.longueur_option - int(self.parametres.taille_plan*20/900), self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900), "Images/vide.png", self.parametres.longueur_option, self.parametres.hauteur_option)
        self.distance = self.fenetre.afficherTexte("0", self.parametres.taille_plan - (self.parametres.longueur_option/2) - int(self.parametres.taille_plan*20/900), (self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900)) + (self.parametres.hauteur_option/2) + int(self.parametres.taille_plan*5/900), "#2D221B", int(self.parametres.taille_plan*25/900))
        self.initVilles()

    def initVilles(self):
        """
        Affiche les nénuphars et dessine un cadre autour de la ville de départ pour la distinguer.
        """
        for ville in self.villes.dict:
            if ville == self.villes.depart:
                self.fenetre.dessinerLigne(self.villes.dict[ville][0]-self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]-self.parametres.taille_ville_solo/2, self.villes.dict[ville][0]+self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]-self.parametres.taille_ville_solo/2, "#2D221B", ep=int(self.parametres.taille_plan*3/900))
                self.fenetre.dessinerLigne(self.villes.dict[ville][0]-self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]-self.parametres.taille_ville_solo/2, self.villes.dict[ville][0]-self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]+self.parametres.taille_ville_solo/2, "#2D221B", ep=int(self.parametres.taille_plan*3/900))
                self.fenetre.dessinerLigne(self.villes.dict[ville][0]-self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]+self.parametres.taille_ville_solo/2, self.villes.dict[ville][0]+self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]+self.parametres.taille_ville_solo/2, "#2D221B", ep=int(self.parametres.taille_plan*3/900))
                self.fenetre.dessinerLigne(self.villes.dict[ville][0]+self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]-self.parametres.taille_ville_solo/2, self.villes.dict[ville][0]+self.parametres.taille_ville_solo/2, self.villes.dict[ville][1]+self.parametres.taille_ville_solo/2, "#2D221B", ep=int(self.parametres.taille_plan*3/900))
            self.fenetre.afficherImage(self.villes.dict[ville][0] - (self.parametres.taille_ville_solo/2), self.villes.dict[ville][1] - (self.parametres.taille_ville_solo/2), "Images/nenuphar.png", self.parametres.taille_ville_solo, self.parametres.taille_ville_solo)
        self.fenetre.actualiser()

    def LancerJeuSolo(self):
        """
        Gère la boucle principale du jeu solo permettant d'échanger deux villes dans le parcours actuel.
        """
        self.parcours = HeuristiqueGreedy(self.villes)
        self.DessinerParcours()
        new_distance = round(self.villes.DistanceTotaleParcours(self.parcours))
        self.fenetre.changerTexte(self.distance, new_distance)
        choix_ville_1, choix_ville_2 = self.ChoixVilles()
        while choix_ville_1 and choix_ville_2:
            self.parcours = PermuterVilles(self.parcours, int(choix_ville_1), int(choix_ville_2))
            self.DessinerParcours()
            new_distance = round(self.villes.DistanceTotaleParcours(self.parcours))
            self.fenetre.changerTexte(self.distance, new_distance)
            choix_ville_1, choix_ville_2 = self.ChoixVilles()

    def ChoixVilles(self):
        """
        Gère la sélection par clic de deux nénuphars permutables.
        """
        if self.cercle_ville_en_cours:
            self.fenetre.supprimer(self.cercle_ville_en_cours)
        choix_graphique_ville_1 = self.fenetre.attendreClic()
        if choix_graphique_ville_1.num == 3:
            return None, None
        choix_logique_ville_1 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_1.x, choix_graphique_ville_1.y, {self.villes.depart})
        while not choix_logique_ville_1:
            choix_graphique_ville_1 = self.fenetre.attendreClic()
            if choix_graphique_ville_1.num == 3:
                return None, None
            choix_logique_ville_1 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_1.x, choix_graphique_ville_1.y, {self.villes.depart})
        self.cercle_ville_en_cours = self.fenetre.dessinerCercle(self.villes.dict[int(choix_logique_ville_1)][0], self.villes.dict[int(choix_logique_ville_1)][1], self.parametres.taille_ville_solo/1.5, "white")
        choix_graphique_ville_2 = self.fenetre.attendreClic()
        choix_logique_ville_2 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_2.x, choix_graphique_ville_2.y, {self.villes.depart})
        while not choix_logique_ville_2:
            choix_graphique_ville_2 = self.fenetre.attendreClic()
            choix_logique_ville_2 = self.villes.TrouverVilleAcceptable(choix_graphique_ville_2.x, choix_graphique_ville_2.y, {self.villes.depart})
        return choix_logique_ville_1, choix_logique_ville_2

    def DessinerParcours(self):
        """
        Efface les anciens chemins et dessine les nouveaux chemins.
        """
        if len(self.chemins)>0:
            for chemin in self.chemins:
                self.fenetre.supprimer(chemin)
            self.chemins = []
        for posville in range(len(self.parcours)-1):
            chemin = self.fenetre.dessinerLigne(self.villes.dict[self.parcours[posville]][0], self.villes.dict[self.parcours[posville]][1], self.villes.dict[self.parcours[posville+1]][0], self.villes.dict[self.parcours[posville+1]][1], "white", int(self.parametres.taille_plan*5/900))
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
        """
        Calcule et affiche le parcours généré par les heuristiques Greedy ou Cheapest.
        """
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours = self.Heuristique(self.villes)
        distance = round(self.villes.DistanceTotaleParcours(parcours))
        self.DessinerParcours(parcours)
        self.fenetre.placerAuDessus(self.menu.grenouille)
        self.AfficherScoreHeuristique(distance)

    def initRecursif(self):
        """
        Calcule et affiche le parcours généré par les heuristiques Récursive ou Dynamique.
        """
        self.fenetre.supprimerTout()
        self.menu.initPlateau()
        parcours_recursif = self.Heuristique(self.villes)
        resultat_recursif = parcours_recursif.ResultatRecursif()
        distance = round(self.villes.DistanceTotaleParcours(resultat_recursif))
        self.DessinerParcours(resultat_recursif)
        self.fenetre.placerAuDessus(self.menu.grenouille)
        self.AfficherScoreHeuristique(distance)

    def init2OPT(self):
        """
        Applique et affiche l'optimisation 2-OPT à partir du dernier parcours calculé.
        """
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
        """
        Affiche le score total de l'heuristique calculée dans la zone dédiée.
        """
        self.fenetre.afficherTexte(distance, self.parametres.taille_plan - (self.parametres.longueur_option/2) - int(self.parametres.taille_plan*20/900),(self.parametres.taille_plan - self.parametres.hauteur_option + int(self.parametres.taille_plan*7/900)) + (self.parametres.hauteur_option/2) + int(self.parametres.taille_plan*5/900), "#2D221B", int(self.parametres.taille_plan*25/900))

    def DessinerParcours(self, parcours):
        """
        Trace tous les chemins reliant les villes dans l'ordre du parcours fourni.
        """
        for posville in range(len(parcours)-1):
            self.fenetre.dessinerLigne(self.villes.dict[parcours[posville]][0], self.villes.dict[parcours[posville]][1], self.villes.dict[parcours[posville+1]][0], self.villes.dict[parcours[posville+1]][1], "white", int(self.parametres.taille_plan*5/900))


def PermuterVilles(parcours, ville_1, ville_2):
    """
    Échange la position de deux villes dans la liste du parcours fourni et renvoie la nouvelle liste.
    """
    nouveau_parcours = parcours.copy()
    id1 = nouveau_parcours.index(ville_1)
    id2 = nouveau_parcours.index(ville_2)
    nouveau_parcours[id1], nouveau_parcours[id2] = nouveau_parcours[id2], nouveau_parcours[id1]
    return nouveau_parcours