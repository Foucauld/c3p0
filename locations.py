from enum import Enum


# Enum pour représenter les différents devices
class Locations(Enum):
    NONE = 0
    SALON = 1
    CHAMBRE = 2
    BUREAU = 3


location_synonyms = {
    Locations.SALON: ["salon"],
    Locations.CHAMBRE: ["chambre"],
    Locations.BUREAU: ["bureau"],
    # Ajoutez d'autres synonymes au besoin
}