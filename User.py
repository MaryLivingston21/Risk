from Territory import TERRITORY


class USER:
    # color???
    def __init__(self, name, territories, cards):
        self.name = name
        self.territories = territories
        self.cards = cards

    def getName(self):
        return self.name

    # Territory setters and getters
    def addTerritory(self, territory):
        self.territories.append(territory)

    def removeTerritory(self, territory):
        self.territories.remove(territory)

    def getTerritories(self):
        return self.territories

    # Troop setters and getters
    def adjustTroops(self, territory, numTroops):
        for t in self.territories:
            if t.getName() == territory.getName():
                t.adjustTroops(numTroops)

    def getTroops(self, territory):
        for t in self.territories:
            if t.getName() == territory.getName():
                return t.getNumTroops()
        return None

    # Card setters and getters
    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, card):
        self.cards.remove(card)

    def getCards(self):
        return self.cards

    def __eq__(self, other):
        if isinstance(other, USER):
            return self.name == other.name
        return False
