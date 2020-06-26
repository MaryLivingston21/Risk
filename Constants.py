from Continent import CONTINENT
from Territory import TERRITORY


class CONSTANTS:
    # initialize territories
    Afghanistan = TERRITORY("afghanistan", "", ["Ukraine", "Ural", "China", "India", "Middle East"])
    China = TERRITORY("china", "", ["Afghanistan", "Ural", "Siberia", "Mongolia", "Siam", "India"])
    India = TERRITORY("india", "", ["Middle East", "Afghanistan", "China", "Siam"])
    Irkutsk = TERRITORY("irkutsk", "", ["Siberia", "Mongolia", "Kamchatka", "Yakutsk"])
    Japan = TERRITORY("japan", "", ["Kamchatka", "Mongolia"])
    Kamchatka = TERRITORY("kamchatka", "", ["Yakutsk", "Irkutsk", "Mongolia", "Japan", "Alaska"])
    MiddleEast = TERRITORY("middle east", "", ["Ukraine", "Afghanistan", "India", "Egypt", "Southern Europe"])
    Mongolia = TERRITORY("mongolia", "", ["Japan", "China", "Siberia", "Irkutsk", "Kamchatka"])
    Siam = TERRITORY("siam", "", ["China", "Indonesia", "India"])
    Siberia = TERRITORY("siberia", "", ["Ural", "China", "Mongolia", "Irkutsk", "Yakutsk"])
    Ural = TERRITORY("ural", "", ["Ukraine", "Afghanistan", "China", "Siberia"])
    Yakutsk = TERRITORY("yakutsk", "", ["Siberia", "Irkutsk", "Kamchatka"])
    Alaska = TERRITORY("alaska", "", ["Kamchatka", "Northwest Territory", "Alberta"])
    Alberta = TERRITORY("alberta", "", ["Alaska", "Northwest Territory", "Ontario", "Western United States"])
    CentralAmerica = TERRITORY("central america", "", ["Western United States", "Eastern United States", "Venezuela"])
    EasternUnitedStates = TERRITORY("eastern united states", "", ["Central America", "Western United States", "Ontario", "Quebec"])
    Greenland = TERRITORY("greenland", "", ["Northwest Territory", "Ontario", "Quebec", "Iceland"])
    NorthwestTerritory = TERRITORY("northwest territory", "", ["Alaska", "Alberta", "Greenland", "Ontario"])
    Ontario = TERRITORY("ontario", "", ["Northwest Territory", "Greenland", "Quebec", "Eastern United States", "Western United States",
               "Alberta"])
    Quebec = TERRITORY("quebec", "", ["Ontario", "Greenland", "Eastern United States"])
    WesternUnitedStates = TERRITORY("western united states", "", ["Alberta", "Ontario", "Eastern United States", "Central America"])
    Argentina = TERRITORY("argentina", "", ["Peru", "Brazil"])
    Brazil = TERRITORY("brazil", "", ["Venezuela", "Peru", "Argentina", "North Africa"])
    Peru = TERRITORY("peru", "", ["Venezuela", "Brazil", "Argentina"])
    Venezuela = TERRITORY("venezuela", "", ["Central America", "Brazil", "Peru"])
    GreatBritain = TERRITORY("great britain", "", ["Scandinavia", "Northern Europe", "Western Europe", "Iceland"])
    Iceland = TERRITORY("iceland", "", ["Greenland", "Great Britain", "Scandinavia"])
    NorthernEurope = TERRITORY("northern europe", "", ["Great Britain", "Scandinavia", "Ukraine", "Southern Europe", "Western Europe"])
    Scandinavia = TERRITORY("scandinavia", "", ["Ukraine", "Northern Europe", "Iceland", "Great Britain"])
    SouthernEurope = TERRITORY("southern europe", "", ["Ukraine", "Northern Europe", "Western Europe", "North Africa", "Egypt", "Middle East"])
    Ukraine = TERRITORY("ukraine", "", ["Scandinavia", "Northern Europe", "Southern Europe", "Middle East", "Ural", "Afghanistan"])
    WesternEurope = TERRITORY("western europe", "", ["Great Britain", "North Africa", "Southern Europe", "Northern Europe"])
    Congo = TERRITORY("congo", "", ["North Africa", "East Africa", "South Africa"])
    EastAfrica = TERRITORY("east africa", "", ["Egypt", "North Africa", "South Africa", "Madagascar", "Congo"])
    Egypt = TERRITORY("egypt", "", ["Southern Europe", "North Africa", "East Africa", "Middle East"])
    Madagascar = TERRITORY("madagascar", "", ["East Africa", "South Africa"])
    NorthAfrica = TERRITORY("north africa", "", ["Brazil", "Western Europe", "Southern Europe", "Egypt", "East Africa", "Congo"])
    SouthAfrica = TERRITORY("south africa", "", ["Congo", "East Africa", "Madagascar"])
    EasternAustralia = TERRITORY("eastern australia", "", ["Western Australia", "New Guinea"])
    Indonesia = TERRITORY("indonesia", "", ["Siam", "New Guinea", "Western Australia"])
    NewGuinea = TERRITORY("new guinea", "", ["Indonesia", "Eastern Australia", "Western Australia"])
    WesternAustralia = TERRITORY("western australia", "", ["Eastern Australia", "New Guinea", "Indonesia"])

    listOfTerritories = [Afghanistan, China, India, Irkutsk, Japan,
                         Kamchatka, MiddleEast, Mongolia, Siam, Siberia,
                         Ural, Yakutsk, Alaska, Alberta, CentralAmerica,
                         EasternUnitedStates, Greenland, NorthwestTerritory,
                         Ontario, Quebec, WesternUnitedStates, Argentina,
                         Brazil, Peru, Venezuela, GreatBritain, Iceland,
                         NorthernEurope, Scandinavia, SouthernEurope, Ukraine,
                         WesternEurope, Congo, EastAfrica, Egypt, Madagascar,
                         NorthAfrica, SouthAfrica, EasternAustralia, Indonesia,
                         NewGuinea, WesternAustralia]

    asia = CONTINENT("asia", [Afghanistan, China, India, Irkutsk, Japan, Kamchatka, MiddleEast,
                              Mongolia, Siam, Siberia, Ural, Yakutsk], 7)
    northAmerica = CONTINENT("north america",
                             [Alaska, Alberta, CentralAmerica, EasternUnitedStates, Greenland,
                              NorthwestTerritory, Ontario, Quebec, WesternUnitedStates], 5)
    southAmerica = CONTINENT("south america", [Argentina, Brazil, Peru, Venezuela], 2)
    europe = CONTINENT("europe", [GreatBritain, Iceland, NorthernEurope, Scandinavia, SouthernEurope,
                                  Ukraine, WesternEurope], 5)
    africa = CONTINENT("africa", [Congo, EastAfrica, Egypt, Madagascar, NorthAfrica, SouthAfrica], 3)
    australia = CONTINENT("australia", [EasternAustralia, Indonesia, NewGuinea, WesternAustralia], 2)
    listOfContinents = [asia, northAmerica, southAmerica, europe, africa, australia]

    @classmethod
    def initializeNumTroops(cls, numPlayers):
        if numPlayers == 3:
            return 35
        elif numPlayers == 4:
            return 30
        elif numPlayers == 5:
            return 25
        else:
            return 20

