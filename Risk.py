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
    # while still territories, give them to the players
    while len(territories) != 0:
        # ensure playerNum is in range of players
        if currentPlayer == numPlayers:
            currentPlayer = 0
        # get random index in list
        num = randrange(len(territories))
        # add corresponding territory to user
        players[currentPlayer].addTerritory(TERRITORY(territories[num], players[currentPlayer]))
        # remove territory from list
        territories.pop(num)
        # increment which players gets a territory
        currentPlayer = currentPlayer + 1
    # assign troops to territories
    for player in players:
        troopsAvailable = CONSTANTS.initializeNumTroops(numPlayers)
        playerTerritories = player.getTerritories()
        numTerritories = len(playerTerritories)
        troopsAvailable = troopsAvailable - numTerritories  # territories are initialized with 1 troop
        # while troops available, get random territory and add 1 troop
        while troopsAvailable > 0:
            index = randrange(len(player.getTerritories()))
            playerTerritories[index].addTroops(1)
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

    def draft(self, user):
        i = 1

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
