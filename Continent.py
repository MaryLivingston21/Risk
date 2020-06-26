class CONTINENT:
    def __init__(self, name, territories, draftPoints):
        self.name = name
        self.territories = territories
        self.draftPoints = draftPoints
        self.criticalTerritoryNum = len(territories)
        self.playerTerritoryCount  # length = num of players

    def getName(self):
        return self.name

    def getTerritories(self):
        return self.territories

    def isOwnedByOnePlayer(self):
        # if playerTerritoryCount[i] = criticalNum, owned by one player
        return False
