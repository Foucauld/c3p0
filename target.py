from enum import Enum


# Enum pour représenter les différents devices
class Target:
    NONE = 0
    LIGHT = 1
    LAMP = 2
    CURTAIN = 3
    PLUG = 4
    AMBIENCE = 5
    SHOPPING_LIST = 6
    PLANNING = 7


target_synonyms = {
    Target.LIGHT: ["éclairage", "lumière", "plafonnier", "lumières"],
    Target.LAMP: [
        "lampe",
        "lampes",
        "hallogène",
        "hallogènes",
        "hallogene",
        "hallogene",
    ],
    Target.CURTAIN: ["volet", "rideau", "volets", "rideaux"],
    Target.PLUG: ["prise", "multiprise", "truc"],
    Target.AMBIENCE: ["ambiance", "ambience", "scene", "scène"],
    # Ajoutez d'autres synonymes au besoin
}
