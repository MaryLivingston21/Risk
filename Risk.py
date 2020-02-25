from Deck import DECK
from User import USER


def boardSetUp():
    deck = DECK()
    deck.initializeDeck()


class RISK:

    def __init__(self, users):
        ## might have to initialize users, depends on interface
        self.users = users
        self.numSetsTurnedIn = 0
        self.userTurn = ""
        self.stage = ""
        boardSetUp()

    def draft(self, user):
        i = 1

    def attack(self, user):
        i = 1

    def fortify(self, user):
        i = 1

    def getCards(self, user):
        i = 1
        # add card to user Deck iff they won an attack

    def turnInCards(self, userDeck):
        self.numSetsTurnedIn = self.numSetsTurnedIn + 1
        # turn in cards function

    # remove user when defeated
    def removeUser(self, user):
        self.users.remove(user)
