# command_dispatcher.py

from nlu.parser import parse_text

# Import des modules d'action
import actions.light_actions as light_actions
import actions.plug_actions as plug_actions
import actions.shoppinglist_actions as shoppinglist_actions
import actions.planning_actions as planning_actions
import actions.unknown_actions as unknown_actions  # <--- import du fallback

# ----------------------------
#  DISPATCH TABLE
# ----------------------------
TARGET_DISPATCH = {
    "light": light_actions,
    "plug": plug_actions,
    "shopping_list": shoppinglist_actions,
    "planning": planning_actions,
}


def dispatch_command(text: str):
    """
    text : la phrase du user
    Retourne ce qu’a renvoyé l’executor du target.
    """
    parsed = parse_text(text)

    action = parsed["action"]
    target = parsed["target"]
    rooms = parsed["rooms"]
    params = parsed["params"]

    # Si target ou action manquant, ou module inconnu → fallback
    if not target or not action or target not in TARGET_DISPATCH:
        return unknown_actions.execute(action, target, rooms, params, text)

    # Cherche le module d’action correspondant
    module = TARGET_DISPATCH.get(target)

    # Exécute la fonction "execute" du module
    return module.execute(action, rooms, params)
