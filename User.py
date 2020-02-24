from Territory import TERRITORY


class USER:
    ## color???
    def __init__(self, name, territories, cards):
        self.name = name
        self.territories = territories
        self.cards = cards

    def getName(self):
        return self.name

    def getTerritories(self):
        return self.territories

    def getCards(self):
        return self.cards
