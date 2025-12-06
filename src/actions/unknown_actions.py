# actions/unknown_actions.py
from nlu.keywords import Keywords

INVALID_COMMANDS_FILE = "nlu/invalid_commands.txt"


def execute(action, target, rooms, params, original_text):
    """
    Action par défaut si aucune commande n'a été trouvée.
    On logue la commande dans un fichier pour traitement manuel.
    Format :
    <phrase> | Target : <target> | Action : <action> | Rooms : <rooms> | Params : <params>
    """
    if original_text is not None:
        rooms_str = ", ".join(r.value for r in rooms) if rooms else ""
        params_str = ", ".join(p.value for p in params) if params else ""
        action_str = action if action is not None else ""
        target_str = target if target is not None else ""

        line = (
            f"{original_text.strip()} | "
            f"Target : {target_str} | "
            f"Action : {action_str} | "
            f"Rooms : {rooms_str} | "
            f"Params : {params_str}\n"
        )

        with open(INVALID_COMMANDS_FILE, "a", encoding="utf-8") as f:
            f.write(line)

    print(f"[UNKNOWN] Aucune commande trouvée pour : {original_text}")
    print(f"Target : {target}")
    print(f"Action : {action}")
    print(f"Rooms : {rooms}")
    print(f"Params : {params}")

    return Keywords.UNKNOWN.name
