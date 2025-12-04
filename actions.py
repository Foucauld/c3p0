from enum import Enum


# Enum pour représenter les différents devices
class Actions(Enum):
    NONE = 0
    ON = 1
    OFF = 2
    # ambiances
    CHILL = 101
    NORMAL = 102


# Correspondance partielle pour les actions et les périphériques
action_synonyms = {
    Actions.ON: [
        "allume",
        "mets en marche",
        "active",
        "démarre",
        "ouvre",
        "ouvrir",
        "allumer",
    ],
    Actions.OFF: [
        "éteins",
        "arrête",
        "désactive",
        "ferme",
        "éteint",
        "éteindre",
        "arreter",
        "temps",
        "étant",
    ],
    Actions.CHILL: ["chill", "tranquille", "calme", "relax"],
    Actions.NORMAL: ["normal", "normale", "défaut", "classique"],
    # Ajoutez d'autres synonymes au besoin
}
