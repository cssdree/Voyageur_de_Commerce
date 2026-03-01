

def HeuristiqueGloutonne(villes):
    parcours_glouton = [villes.depart]
    ville_actuelle = villes.depart
    villes_possibles = villes.set_id - {villes.depart}
    while len(parcours_glouton) != len(villes.dict):
        nouvelle_ville = villes.TrouverPlusProcheVille(ville_actuelle, villes_possibles)
        parcours_glouton.append(nouvelle_ville)
        villes_possibles = villes_possibles - {nouvelle_ville}
        ville_actuelle = nouvelle_ville
    parcours_glouton.append(villes.depart)
    return parcours_glouton


def ParcoursRecursif(villes):
