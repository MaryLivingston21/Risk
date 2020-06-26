class TERRITORY:

    def __init__(self, name, connectingTerritories):
        self.name = name
        self.numTroops = 1
        self.connectingTerritories = connectingTerritories

    def adjustTroops(self, num):
        if num > 0:
            self.numTroops = self.numTroops + num
        else:
            self.numTroops = self.numTroops - num
        if self.numTroops < 1:
            print("ERROR with numTroops")

    def setTroops(self, num):
        if num > 0:
            self.numTroops = num
        else:
            print("ERROR with numTroops")

    def getName(self):
        return self.name

    def getNumTroops(self):
        return self.numTroops

    def getConnectingTerritories(self):
        return self.connectingTerritories
