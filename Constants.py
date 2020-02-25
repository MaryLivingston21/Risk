class CONSTANTS:
    listOfTerritories = ["Afghanistan", "China", "India", "Irkutsk", "Japan",
                                  "Kamchatka", "Middle East", "Mongolia", "Siam", "Siberia",
                                  "Ural", "Yakutsk", "Alaska", "Alberta", "Central America",
                                  "Eastern United States", "Greenland", "Northwest Territory",
                                  "Ontario", "Quebec", "Western United States", "Argentina",
                                  "Brazil", "Peru", "Venezuela", "Great Britain", "Iceland",
                                  "Northern Europe", "Scandinavia", "Southern Europe", "Ukraine",
                                  "Western Europe", "Congo", "East Africa", "Egypt", "Madagascar",
                                  "North Africa", "South Africa", "Eastern Australia", "Indonesia",
                                  "New Guinea", "Western Australia"]
    asia = ["Afghanistan", "China", "India", "Irkutsk", "Japan", "Kamchatka", "Middle East",
            "Mongolia", "Siam", "Siberia", "Ural", "Yakutsk"]
    northAmerica = ["Alaska", "Alberta", "Central America", "Eastern United States", "Greenland",
                    "Northwest Territory", "Ontario", "Quebec", "Western United States"]
    southAmerica = ["Argentina", "Brazil", "Peru", "Venezuela"]
    europe = ["Great Britain", "Iceland", "Northern Europe", "Scandinavia", "Southern Europe",
              "Ukraine", "Western Europe"]
    africa = ["Congo", "East Africa", "Egypt", "Madagascar", "North Africa", "South Africa"]
    australia = ["Eastern Australia", "Indonesia", "New Guinea", "Western Australia"]

    # make adjacency list
    Afghanistan = ["Ukraine", "Ural", "China", "India", "Middle East"]
    China = ["Afghanistan", "Ural", "Siberia", "Mongolia", "Siam", "India"]
    India = ["Middle East", "Afghanistan", "China", "Siam"]
    Irkutsk = ["Siberia", "Mongolia", "Kamchatka", "Yakutsk"]
    Japan = ["Kamchatka", "Mongolia"]
    Kamchatka = ["Yakutsk", "Irkutsk", "Mongolia", "Japan", "Alaska"]
    MiddleEast = ["Ukraine", "Afghanistan", "India", "Egypt", "Southern Europe"]
    Mongolia = ["Japan", "China", "Siberia", "Irkutsk", "Kamchatka"]
    Siam = ["China", "Indonesia", "India"]
    Siberia = ["Ural", "China", "Mongolia", "Irkutsk", "Yakutsk"]
    Ural = ["Ukraine", "Afghanistan", "China", "Siberia"]
    Yakutsk = ["Siberia", "Irkutsk", "Kamchatka"]
    Alaska = ["Kamchatka", "Northwest Territory", "Alberta"]
    Alberta = ["Alaska", "Northwest Territory", "Ontario", "Western United States"]
    CentralAmerica = ["Western United States", "Eastern United States", "Venezuela"]
    EasternUnitedStates = ["Central America", "Western United States", "Ontario", "Quebec"]
    Greenland = ["Northwest Territory", "Ontario", "Quebec", "Iceland"]
    NorthwestTerritory =["Alaska", "Alberta", "Greenland", "Ontario"]
    Ontario = ["Northwest Territory", "Greenland", "Quebec", "Eastern United States", "Western United States", "Alberta"]
    Quebec = ["Ontario", "Greenland", "Eastern United States"]
    WesternUnitedStates = ["Alberta", "Ontario", "Eastern United States", "Central America"]
    Argentina = ["Peru", "Brazil"]
    Brazil = ["Venezuela", "Peru", "Argentina", "North Africa"]
    Peru = ["Venezuela", "Brazil", "Argentina"]
    Venezuela = ["Central America", "Brazil", "Peru"]
    GreatBritain = ["Scandinavia", "Northern Europe", "Western Europe", "Iceland"]
    Iceland = ["Greenland", "Great Britain", "Scandinavia"]
    NorthernEurope = ["Great Britain", "Scandinavia", "Ukraine", "Southern Europe", "Western Europe"]
    Scandinavia = ["Ukraine", "Northern Europe", "Iceland", "Great Britain"]
    SouthernEurope = ["Ukraine", "Northern Europe", "Western Europe", "North Africa", "Egypt", "Middle East"]
    Ukraine = ["Scandinavia", "Northern Europe", "Southern Europe", "Middle East", "Ural", "Afghanistan"]
    WesternEurope = ["Great Britain", "North Africa", "Southern Europe", "Northern Europe"]
    Congo = ["North Africa", "East Africa", "South Africa"]
    EastAfrica = ["Egypt", "North Africa", "South Africa", "Madagascar", "Congo"]
    Egypt = ["Southern Europe", "North Africa", "East Africa", "Middle East"]
    Madagascar = ["East Africa", "South Africa"]
    NorthAfrica = ["Brazil", "Western Europe", "Southern Europe", "Egypt", "East Africa", "Congo"]
    SouthAfrica = ["Congo", "East Africa", "Madagascar"]
    EasternAustralia = ["Western Australia", "New Guinea"]
    Indonesia = ["Siam", "New Guinea", "Western Australia"]
    NewGuinea = ["Indonesia", "Eastern Australia", "Western Australia"]
    WesternAustralia = ["Eastern Australia", "New Guinea", "Indonesia"]

    AdjacencyList = [Afghanistan, China, India, Irkutsk, Japan, Kamchatka, MiddleEast, Mongolia, Siam, Siberia,
                     Ural, Yakutsk, Alaska, Alberta, CentralAmerica, EasternUnitedStates, Greenland,
                     NorthwestTerritory, Ontario, Quebec, WesternUnitedStates, Argentina, Brazil, Peru,
                     Venezuela, GreatBritain, Iceland, NorthernEurope, Scandinavia, SouthernEurope, Ukraine,
                     WesternEurope, Congo, EastAfrica, Egypt, Madagascar, NorthAfrica, SouthAfrica,
                     EasternAustralia, Indonesia, NewGuinea, WesternAustralia]


