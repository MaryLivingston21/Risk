from Risk import RISK
from User import USER


def main():
    playerNames = getUsers()
    game = RISK(playerNames)

    for user in game.getPlayers():
        print("user: " + user.getName())
        print("territories: ")
        for territory in user.getTerritories():
            print(territory.getName() + ": " + str(territory.getNumTroops()) + " ")
        game.draft(user)



def getUsers():
    numUsers = 0
    playerNames = []

    while numUsers > 7 or numUsers < 3:
        try:
            numUsers = int(input("Input number of users(3-6): "))
        except ValueError:
            numUsers = input("Input number of users: ")

    for i in range(1, numUsers + 1):
        name = input("Input player " + str(i) + "'s name")
        playerNames.append(name)

    return playerNames


main()
