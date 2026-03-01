import random
import math


def TrouverPlusProcheVille(c, l, villes):
    nearest = random.choice(list(villes.keys()))
    for ville in villes:
        if math.dist((c, l), villes[ville]) < math.dist((c, l), villes[nearest]):
            nearest = villes[ville]
    return nearest