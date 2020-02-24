from Territory import TERRITORY


class CONTINENT:
    def __init__(self, name, territories):
        self.name = name
        if name.lower() == "asia":
            self.territories = []
        if name.lower() == "north america":
            self.territories = []
        if name.lower() == "south america":
            self.territories = []
        if name.lower() == "europe":
            self.territories = []
        if name.lower() == "africa":
            self.territories = []
        if name.lower() == "australia":
            self.territories = []

    def getName(self):
        return self.name

    def getTerritories(self):
        return self.territories
