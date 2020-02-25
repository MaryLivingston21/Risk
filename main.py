from Risk import RISK
from User import USER


def main():
    users = getUsers()
    game = RISK(users)


def getUsers():
    numUsers = ""
    users = []

    List = []
    for i in range(2, 7):
        List.append(i)

    while numUsers not in List:
        try:
            numUsers = int(input("Input number of users(2-6): "))
        except ValueError:
            numUsers = input("Input number of users: ")

    for i in range(1, numUsers + 1):
        name = input("Input player " + str(i) + "'s name")
        t = []
        c = []
        users.append(USER(name, t, c))

    return users


main()
