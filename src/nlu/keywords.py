# keywords.py

# ---------------------
#  TARGETS
# ---------------------
# Cibles générales (light, plug, shopping_list...)
TARGET_KEYWORDS = {
    "light": ["lumière", "lampe", "éclairage", "plafonnier", "chevet"],
    "plug": ["prise", "fiche"],
    "shopping_list": ["courses", "liste", "liste de courses"],
    "planning": ["planning", "agenda", "emploi du temps"],
}


# ---------------------
#  ACTIONS
# ---------------------
# Actions génériques
ACTION_KEYWORDS = {
    "enable": ["allume", "allumer", "ouvre"],
    "disable": ["éteins", "eteins", "ferme", "etant", "étant"],
    "add": ["ajoute", "ajouter", "rajoute"],
    "remove": ["retire", "retirer", "enlève"],
    "show": ["montre", "affiche", "donne", "montres-moi"],
}


# ---------------------
#  ROOMS
# ---------------------
ROOM_KEYWORDS = {
    "living_room": ["salon", "séjour"],
    "kitchen": ["cuisine"],
    "study": ["bureau"],
    "bedroom": ["chambre"],
}


# ---------------------
#  PARAMETERS (génériques)
# ---------------------
# Ici on met des paramètres précis (types de lumières, objets, etc.)
# Indépendant des targets (light / plug / shopping list)
PARAM_KEYWORDS = {
    # lumières
    "ceiling": ["plafonnier", "plafond"],
    "floor_lamp": ["lampadaire", "lampe"],
    "bed_lamp": ["chevet", "lit"],
    "bed_lamp_left": ["chevet gauche", "gauche"],
    "bed_lamp_right": ["chevet droit", "droit"],
    # prises
    "plug_tv": ["télé", "tv"],
    "plug_pc": ["ordinateur", "pc"],
    # shopping list
    "item_fruits": ["fruits", "pomme", "banane"],
    "item_pain": ["pain", "baguette"],
    # planning
    "morning": ["matin"],
    "evening": ["soir"],
}
