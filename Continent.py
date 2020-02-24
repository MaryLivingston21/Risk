from Territory import TERRITORY
from Constants import CONSTANTS

constants = CONSTANTS()


class CONTINENT:
    def __init__(self, name, territories):
        self.name = name
        if self.name.lower() == "asia":
            self.territories = constants.asia

        if self.name.lower() == "north america":
            self.territories = constants.northAmerica

        if self.name.lower() == "south america":
            self.territories = constants.southAmerica

        if self.name.lower() == "europe":
            self.territories = constants.europe

        if name.lower() == "africa":
            self.territories = constants.africa

        if name.lower() == "australia":
            self.territories = constants.australia

    def getName(self):
        return self.name

    def getTerritories(self):
        return self.territories
