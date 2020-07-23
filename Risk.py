from random import shuffle
from random import randrange

from Deck import DECK
from Territory import TERRITORY
from User import USER
from Constants import CONSTANTS


def setUpPlayers(playerNames):
    players = []
    # create users
    for name in playerNames:
        players.append(USER(name, [], []))
    shuffle(players)
    numPlayers = len(playerNames)
    currentPlayer = 0
    territories = CONSTANTS.listOfTerritories
    numTerritories = len(territories)
    # while still territories, give them to the players
    while len(territories) != 0:
        # ensure playerNum is in range of players
        if currentPlayer == numPlayers:
            currentPlayer = 0
        # get random index in list
        num = randrange(len(territories))
        # add corresponding territory to user
        players[currentPlayer].addTerritory(territories[num])
        # remove territory from list
        territories.pop(num)
        # increment which players gets a territory
        currentPlayer = currentPlayer + 1
    for p in players:
        # assign troops to territories
        troopsAvailable = CONSTANTS.initializeNumTroops(numPlayers)
        print("Troops available: " + str(troopsAvailable))
        troopsAvailable = troopsAvailable - len(p.getTerritories())  # territories are initialized with 1 troop
        # while troops available, get random territory and add 1 troop
        while troopsAvailable > 0:
            index = randrange(len(p.getTerritories()))
            userTerritories = p.getTerritories()
            p.adjustTroops(userTerritories[index], 1)
            troopsAvailable = troopsAvailable - 1
    return players


class RISK:

    def __init__(self, playerNames):
        # might have to initialize players, depends on interface
        self.players = setUpPlayers(playerNames)
        self.numSetsTurnedIn = 0
        self.userTurn = ""
        self.stage = ""
        self.deck = DECK()
        self.continents = CONSTANTS.listOfContinents

    def draft(self, user):
        # get troops from territories occupied
        numTerritories = len(user.getTerritories())
        numTroops = numTerritories / 3
        if numTroops < 3:
            numTroops = 3
        # get troops from continents held
        for c in self.continents:
            print(c.getName() + ": ")
            if c.isOwnedByPlayer(user):
                print("true")
                numTroops = numTroops + c.getDraftPoints()
            else:
                print("false")

        # Trade in cards
        if canTradeInCards(user) > 0:
            print("Would you like to trade in cards?(y/n)")

    def canTradeInCards(self, user):
        cards = user.getCards()
        if len(cards) > 2:
            # get type of first card
            type1 = cards[0].getCardType
        else:
            print("You can't trade in any cards this turn")
            return 0
        # Todo: points for owning that country

    def attack(self, user):
        i = 1

    def fortify(self, user):
        i = 1

    def giveUserCard(self, user):
        card = self.deck.getCard()
        user.addCard(card)
        self.deck.removeCard(card)

    def turnInCards(self, userDeck):
        self.numSetsTurnedIn = self.numSetsTurnedIn + 1

    # remove user when defeated
    def removePlayer(self, player):
        self.players.remove(player)

    def getPlayers(self):
        return self.players
