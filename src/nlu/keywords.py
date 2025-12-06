# keywords.py
from enum import Enum


class Keywords(Enum):
    UNKNOWN = "INCONNU"
    LIGHT = "LUMIERE"
    PLUG = "PRISE"
    SHOPPING_LIST = "LISTE_COURSES"
    PLANNING = "TACHES"
    STOP = "STOP"
    ENABLE = "ON"
    DISABLE = "OFF"
    ADD = ""
    REMOVE = ""
    SHOW = ""
    AMBIENCE = "AMBIANCE"
    LIVING_ROOM = "SALON"
    KITCHEN = "CUISINE"
    STUDY = "BUREAU"
    BEDROOM = "CHAMBRE"
    CEILING = "PLAFOND"
    FLOOR_LAMP = "LAMPE_PIED"
    BED_LAMP = "LAMPE_CHEVET"
    BED_LAMP_LEFT = "LAMPE_CHEVET_GAUCHE"
    BED_LAMP_RIGHT = "LAMPE_CHEVET_DROIT"
    AMBIENCE_DEFAULT = "DEFAUT"
    AMBIENCE_SOFT = "DOUX"
    AMBIENCE_CLASSIC = "NORMAL"
    AMBIENCE_FOREST = "FOREST"
    AMBIENCE_WARM = "WARM"
    AMBIENCE_SUNSET = "SUNSET"
    AMBIENCE_GAMING = "GAMING"
    AMBIENCE_CHILL = "CHILL"


# ---------------------
#  TARGETS
# ---------------------
# Cibles générales (light, plug, shopping_list...)
TARGET_KEYWORDS = {
    Keywords.LIGHT: [
        "lumière",
        "lampe",
        "éclairage",
        "plafonnier",
        "plafond",
        "chevet",
        "ambiance",
    ],
    Keywords.PLUG: ["prise", "fiche"],
    Keywords.SHOPPING_LIST: ["courses", "liste", "liste de courses"],
    Keywords.PLANNING: ["planning", "agenda", "emploi du temps"],
    Keywords.STOP: ["stop", "arrête", "annule", "non", "rien"],
}


# ---------------------
#  ACTIONS
# ---------------------
# Actions génériques
ACTION_KEYWORDS = {
    Keywords.ENABLE: ["allume", "allumer", "ouvre"],
    Keywords.DISABLE: [
        "éteins",
        "eteins",
        "ferme",
        "etant",
        "étant",
        "éteint",
        "temps",
    ],
    Keywords.ADD: ["ajoute", "ajouter", "rajoute"],
    Keywords.REMOVE: ["retire", "retirer", "enlève"],
    Keywords.SHOW: ["montre", "affiche", "donne", "montres-moi"],
    Keywords.AMBIENCE: ["ambiance"],
    Keywords.STOP: ["stop", "arrête", "annule", "non", "rien"],
}


# ---------------------
#  ROOMS
# ---------------------
ROOM_KEYWORDS = {
    Keywords.LIVING_ROOM: ["salon", "séjour", "savon"],
    Keywords.KITCHEN: ["cuisine"],
    Keywords.STUDY: ["bureau"],
    Keywords.BEDROOM: ["chambre"],
}


# ---------------------
#  PARAMETERS (génériques)
# ---------------------
# Ici on met des paramètres précis (types de lumières, objets, etc.)
# Indépendant des targets (light / plug / shopping list)
PARAM_KEYWORDS = {
    # lumières
    Keywords.CEILING: ["plafonnier", "plafond"],
    Keywords.FLOOR_LAMP: ["lampadaire", "lampe"],
    Keywords.BED_LAMP: ["chevet", "lit"],
    Keywords.BED_LAMP_LEFT: ["chevet gauche", "gauche"],
    Keywords.BED_LAMP_RIGHT: ["chevet droit", "droit"],
    Keywords.AMBIENCE_DEFAULT: [],
    Keywords.AMBIENCE_SOFT: ["doux", "douce", "tamisé", "tamisée"],
    Keywords.AMBIENCE_CLASSIC: ["normale", "normal", "classique", "défaut"],
    Keywords.AMBIENCE_FOREST: ["nature", "forêt", "foret", "vert", "verte"],
    Keywords.AMBIENCE_WARM: ["chaude"],
    Keywords.AMBIENCE_SUNSET: ["coucher", "crépuscule"],
    Keywords.AMBIENCE_GAMING: ["jeu", "néon", "violet", "violette"],
    Keywords.AMBIENCE_CHILL: ["tranquille", "bleue"],
    # prises
    # shopping list
    # planning
}

# ---------------------
#  LIGHTS (génériques)
# ---------------------
# Ici on met les lights disponibles dans chaque room
# dépendant des rooms
LIGHTS = {
    Keywords.LIVING_ROOM: [Keywords.CEILING, Keywords.FLOOR_LAMP],
    Keywords.KITCHEN: [Keywords.CEILING],
    Keywords.BEDROOM: [
        Keywords.CEILING,
        Keywords.BED_LAMP_LEFT,
        Keywords.BED_LAMP_RIGHT,
    ],
    Keywords.STUDY: [Keywords.CEILING, Keywords.BED_LAMP],
}

AMBIENCES = [
    Keywords.AMBIENCE_DEFAULT,
    Keywords.AMBIENCE_SOFT,
    Keywords.AMBIENCE_CLASSIC,
    Keywords.AMBIENCE_FOREST,
    Keywords.AMBIENCE_WARM,
    Keywords.AMBIENCE_SUNSET,
    Keywords.AMBIENCE_GAMING,
    Keywords.AMBIENCE_CHILL,
]
