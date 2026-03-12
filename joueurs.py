

class Joueur():
    def __init__(self, depart):
        self.depart = depart
        self.parcours = [self.depart]
        self.visitees = {self.depart}

    def ChoixVille(self, idville):
        if idville in self.visitees:
            raise PermissionError("Ville déjà visitées")
        self.parcours.append(idville)
        self.visitees.add(idville)

    def ScoreEnCours(self, villes):
        return villes.DistanceTotaleParcours(self.parcours)

    def ScoreFinal(self, villes):
        return villes.DistanceTotaleParcours(self.parcours+[self.depart])