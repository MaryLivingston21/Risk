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
    while territories != 0:
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
    # assign troops to territories
    troopsAvailable = CONSTANTS.initializeNumTroops(numPlayers)
    troopsAvailable = troopsAvailable - numTerritories  # territories are initialized with 1 troop
    # while troops available, get random territory and add 1 troop
    while troopsAvailable > 0:
        if currentPlayer == numPlayers:
            currentPlayer = 0
        index = randrange(len(currentPlayer.getTerritories()))
        currentPlayer.getTerritories[index].setTroops(1)
        #TODO: FIX THIS!
        troopsAvailable = troopsAvailable - 1
        # increment which players gets more troops
        currentPlayer = currentPlayer + 1

    return players


class RISK:

    def __init__(self, playerNames):
        # might have to initialize players, depends on interface
        self.players = setUpPlayers(playerNames)
        self.numSetsTurnedIn = 0
        self.userTurn = ""
        self.stage = ""
        self.deck = DECK()

    def draft(self, user):
        # get troops from territories occupied
        numTerritories = len(user.getTerritories())
        numTroops = numTerritories / 3
        if numTroops < 3:
            numTroops = 3
        # get troops from continents held

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
        # turn in cards function

    # remove user when defeated
    def removePlayer(self, player):
        self.players.remove(player)

    def getPlayers(self):
        return self.players
