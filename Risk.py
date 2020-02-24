from Deck import DECK
from User import USER


class RISK:

    def __init__(self, users):
        ## might have to initialize users, depends on interface
        self.users = users
        self.numSetsTurnedIn = 0
        self.userTurn = ""
        self.stage = ""

    def boardSetUp(self):
        deck = DECK()

    def draft(self, user):
        ##something

    def attack(self, user):
        ##something

    def fortify(self, user):
        ##something

    def getCards(self, user):
        ##add card to user Deck iff they won an attack
