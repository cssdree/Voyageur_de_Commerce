import math


def HeuristiqueGloutonne(villes):
    parcours_glouton = [villes.depart]
    ville_actuelle = villes.depart
    villes_possibles = villes.villes_initiales_possibles
    while len(parcours_glouton) != len(villes.dict):
        nouvelle_ville = villes.TrouverPlusProcheVille(ville_actuelle, villes_possibles)
        parcours_glouton.append(nouvelle_ville)
        villes_possibles = villes_possibles - {nouvelle_ville}
        ville_actuelle = nouvelle_ville
    parcours_glouton.append(villes.depart)
    return parcours_glouton


def HeuristiqueCheapestInsertion(villes):
    villes_possibles = villes.villes_initiales_possibles
    premiere = villes.TrouverPlusProcheVille(villes.depart, villes_possibles)
    parcours_cheap = [villes.depart, premiere, villes.depart]
    villes_possibles = villes_possibles - {premiere}
    while len(villes_possibles) != 0:
        meilleure_insertion = math.inf
        meilleure_ville = None
        meilleure_position = None
        for idville in villes_possibles:
            for idinsertion in range(len(parcours_cheap)-1):
                A = parcours_cheap[idinsertion]
                B = parcours_cheap[idinsertion+1]
                insertion = (math.dist(villes.dict[A], villes.dict[idville]) + math.dist(villes.dict[idville], villes.dict[B]) - math.dist(villes.dict[A], villes.dict[B]))
                if insertion < meilleure_insertion:
                    meilleure_insertion = insertion
                    meilleure_ville = idville
                    meilleure_position = idinsertion+1
        parcours_cheap.insert(meilleure_position, meilleure_ville)
        villes_possibles = villes_possibles - {meilleure_ville}
    return parcours_cheap


class ParcoursRecursif():
    def __init__(self, villes):
        self.villes = villes
        self.meilleur_parcours_recursif = ([], math.inf)

    def RechercheRecursive(self, villes_possibles, parcours_recursif, distance_recursive):
        if distance_recursive > self.meilleur_parcours_recursif[1]:
            return
        if len(villes_possibles) == 0:
            if distance_recursive < self.meilleur_parcours_recursif[1]:
                self.meilleur_parcours_recursif = (parcours_recursif, distance_recursive)
            return
        for idville in villes_possibles:
            nouvelle_distance_recursive = distance_recursive + math.dist(self.villes.dict[parcours_recursif[-1]], self.villes.dict[idville])
            self.RechercheRecursive(villes_possibles-{idville}, parcours_recursif+[idville], nouvelle_distance_recursive)

    def ResultatRecursif(self):
        self.RechercheRecursive(self.villes.villes_initiales_possibles, [self.villes.depart], 0)
        return self.meilleur_parcours_recursif[0]+[self.villes.depart]


def Heuristique2OPT(villes, parcours):
    n_unique = len(parcours)-1
    amelioration = True
    while amelioration:
        amelioration = False
        for i in range(n_unique-1):
            for j in range(i+2, n_unique):
                if i == 0 and j == n_unique-1:
                    continue
                v_i, v_i_suivant = parcours[i], parcours[i+1]
                v_j, v_j_suivant = parcours[j], parcours[(j+1)%n_unique]
                distance_actuelle = math.dist(villes.dict[v_i], villes.dict[v_i_suivant]) + math.dist(villes.dict[v_j], villes.dict[v_j_suivant])
                distance_nouvelle = math.dist(villes.dict[v_i], villes.dict[v_j]) + math.dist(villes.dict[v_i_suivant], villes.dict[v_j_suivant])
                if distance_nouvelle < distance_actuelle:
                    parcours[i+1 : j+1] = reversed(parcours[i+1 : j+1])
                    amelioration = True
    return parcours