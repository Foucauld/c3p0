# parser.py

import re
from nlu.keywords import TARGET_KEYWORDS, ACTION_KEYWORDS, ROOM_KEYWORDS, PARAM_KEYWORDS


def match_keywords(text, keyword_map):
    """Retourne la liste des clés dont au moins un mot-clé apparaît dans text."""
    matches = []
    for key, triggers in keyword_map.items():
        for trig in triggers:
            if trig in text:
                matches.append(key)
                break
    return matches


def parse_text(text: str) -> dict:
    """Analyse la phrase et retourne action/target/rooms/params."""
    text = text.lower()

    detected_action = match_keywords(text, ACTION_KEYWORDS)
    detected_target = match_keywords(text, TARGET_KEYWORDS)
    detected_rooms = match_keywords(text, ROOM_KEYWORDS)
    detected_params = match_keywords(text, PARAM_KEYWORDS)

    # On choisit le premier match si multiples (simple, efficace)
    action = detected_action[0] if detected_action else None
    target = detected_target[0] if detected_target else None
    print_action = ""
    print_target = ""
    print_room = ""
    print_param = ""
    for act in detected_action:
        print_action = " ".join(print_action, act)
    for tar in detected_target:
        print_target = " ".join(print_target, tar)
    for room in detected_rooms:
        print_room = " ".join(print_room, room)
    for param in detected_params:
        print_param = " ".join(print_param, param)

    print(
        f"Actions : {print_action}\nTarget : {print_target}\nRooms : {print_room}\nParams : {print_param}\n"
    )
    return {
        "action": action,
        "target": target,
        "rooms": detected_rooms,
        "params": detected_params,
    }
