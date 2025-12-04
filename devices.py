from enum import Enum


# Enum pour représenter les différents devices
class Devices(Enum):
    NONE = 0
    LIGHT = 1
    LAMP = 2
    CURTAIN = 3
    PLUG = 4
    AMBIENCE = 5


device_synonyms = {
    Devices.LIGHT: ["éclairage", "lumière", "plafonnier", "lumières"],
    Devices.LAMP: ["lampe", "lampes", "hallogène"],
    Devices.CURTAIN: ["volet", "rideau", "volets", "rideaux"],
    Devices.PLUG: ["prise", "multiprise", "truc"],
    Devices.AMBIENCE: ["ambiance", "ambience", "scene", "scène"],
    # Ajoutez d'autres synonymes au besoin
}
