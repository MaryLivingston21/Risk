class CONTINENT:
    def __init__(self, name, territories):
        self.name = name
        self.territories = territories

    def getName(self):
        return self.name

    def getTerritories(self):
        return self.territories

    def isOwnedByOnePlayer(self):
        boolean = True
        user = self.territories[0].getUser()
        for t in self.territories:
            if t.getUser != user:
                boolean = False
        return boolean

    def getPoints(self):
        if self.name == "asia":
            return 7
        elif self.name == "north america" or self.name == "europe":
            return 5
        elif self.name == "africa":
            return 3
        elif self.name == "south american" or self.name == "australia":
            return 2
        else:
            return 0


