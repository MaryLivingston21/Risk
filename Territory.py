class TERRITORY:

    def __init__(self, name, connectingTerritories):
        self.name = name
        self.connectingTerritories = connectingTerritories
        self.user = ""

    def __init__(self, name, connectingTerritories, user):
        self.name = name
        self.connectingTerritories = connectingTerritories
        self.user = user

    def setUser(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def getName(self):
        return self.name

    def getConnectingTerritories(self):
        return self.connectingTerritories

