from commands import Command
from typing import Dict, Callable, List
import json


def load_commands(json_path: str, func_map: Dict[str, Callable]):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    commands = [Command.from_dict(d, func_map[d["name"]]) for d in data]

    target_to_triggers = {}
    target_to_commands = {}

    for cmd in commands:
        target_to_triggers.setdefault(cmd.target, [])
        target_to_triggers[cmd.target].extend(cmd.target_triggers)
        # Éventuellement supprimer les doublons
        target_to_triggers[cmd.target] = list(set(target_to_triggers[cmd.target]))
        target_to_commands.setdefault(cmd.target, []).append(cmd)

    return target_to_triggers, target_to_commands


def extract_command(
    command_text: str,
    target_to_triggers: Dict[str, List[str]],
    target_to_commands: Dict[str, List[Command]],
) -> Command:
    words = command_text.lower().split()

    # 1️⃣ Chercher le target
    matched_target = None
    for target, triggers in target_to_triggers.items():
        if any(word in triggers for word in words):
            matched_target = target
            break

    if not matched_target:
        print("Aucune target détectée")
        return None

    # 2️⃣ Chercher la commande spécifique dans les commandes correspondant à la target
    for cmd in target_to_commands[matched_target]:
        if any(word in cmd.action_triggers for word in words):
            # On peut éventuellement chercher les paramètres ici aussi
            matched_param = None
            for param_id, triggers in cmd.parameters.items():
                if any(word in triggers for word in words):
                    matched_param = param_id
                    break
            return (cmd, matched_param)

    print("Aucune commande correspondante trouvée pour la target:", matched_target)
    return None
