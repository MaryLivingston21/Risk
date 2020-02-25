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

    # Card setters and getters
    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, card):
        self.cards.remove(card)

    def getCards(self):
        return self.cards
