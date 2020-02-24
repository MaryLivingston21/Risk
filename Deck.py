from Card import CARD
from Constants import CONSTANTS
constants = CONSTANTS()


class DECK:

    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    # remove card from deck
    def removeCard(self, card):
        self.cards.remove(card)

    def initializeDeck(self):
        territories = constants.listOfTerritories
        i = 1
        for territory in territories:
            if i == 1:
                self.cards.append(CARD(territory, "Infantry"))
            elif i == 2:
                self.cards.append(CARD(territory, "Cavalry"))
            else:
                self.cards.append(CARD(territory, "Artillery"))
            # increment i
            if (i != 3):
                i = i + 1
            else:
                i = 1
