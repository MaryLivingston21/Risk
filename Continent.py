import User

class CONTINENT:
    def __init__(self, name, territories, draftPoints):
        self.name = name
        self.territories = territories
        self.draftPoints = draftPoints

    def getName(self):
        return self.name

    def getTerritories(self):
        return self.territories

    def isOwnedByPlayer(self, player):
        userTerritories = player.getTerritories()
        for t in self.territories:
            if t not in userTerritories:
                return False
        return True
