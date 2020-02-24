from Card import CARD


class DECK:

    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    ##remove card from deck
    def removeCard(self, card):
        self.cards.remove(card)
