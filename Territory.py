class TERRITORY:

    def __init__(self, name, user, connectingTerritories):
        self.name = name
        self.user = user
        self.numTroops = 1
        self.connectingTerritories = connectingTerritories

    def setUser(self, user):
        self.user = user

    def setTroops(self, num):
        if num > 0:
            self.numTroops = self.numTroops + num
        else:
            self.numTroops = self.numTroops - num
        if self.numTroops < 1:
            print("ERROR with numTroops")

    def getUser(self):
        return self.user

    def getName(self):
        return self.name

    def getNumTroops(self):
        return self.numTroops

    def getConnectingTerritories(self):
        return self.connectingTerritories
