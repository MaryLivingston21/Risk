class TERRITORY:

    def __init__(self, name, connectingTerritories):
        self.name = name
        self.connectingTerritories = connectingTerritories

    def getName(self):
        return self.name

    def getConnectingTerritories(self):
        return self.connectingTerritories
