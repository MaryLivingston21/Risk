class TERRITORY:

    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.numTroops = 1

    def setUser(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def getName(self):
        return self.name

    def getNumTroops(self):
        return self.numTroops

    def addTroops(self, num):
        self.numTroops = self.numTroops + num

    def removeTroops(self, num):
        self.numTroops = self.numTroops - num
