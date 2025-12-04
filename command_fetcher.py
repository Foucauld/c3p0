import actions
import locations
import devices
import commands


def extract_command(command_text):
    # Exemple de texte reconnu : "Allumer la lumière et éteindre les volets dans le salon"
    # Vous devrez adapter cette partie en fonction du format réel du texte reconnu

    # Diviser le texte reconnu en mots
    command_words = command_text.lower().split()

    # Gérer les synonymes pour les actions et les périphériques
    normalized_actions = []
    normalized_devices = []
    normalized_locations = []
    trash_words = []

    categories = [
        (actions.action_synonyms, normalized_actions),
        (devices.device_synonyms, normalized_devices),
        (locations.location_synonyms, normalized_locations),
    ]

    for word in command_words:
        print(f"Mot détecté : {word}")
        found = False
        for synonyms_dict, normalized_list in categories:
            for key, synonyms in synonyms_dict.items():
                if word in synonyms:
                    normalized_list.append(key)
                    found = True
                    break
            if found:
                break
        if not found:
            trash_words.append(word)

    # Vérifier les données manquantes ou en double
    actions_set = set(normalized_actions)
    devices_set = set(normalized_devices)
    locations_set = set(normalized_locations)

    if len(actions_set) != 1:
        print(
            f"Il doit y avoir une seule action dans la commande. Actions: {actions_set}"
        )
        action_return = actions.Actions.NONE
    else:
        action_return = list(actions_set)[0]
    if len(devices_set) != 1:
        print(
            f"Il doit y avoir un seul périphérique dans la commande. Devices: {devices_set}"
        )
        device_return = devices.Devices.NONE
    else:
        device_return = list(devices_set)[0]
    if len(locations_set) != 1:
        print(
            f"Il doit y avoir un seul lieu dans la commande. Locations: {locations_set}"
        )
        location_return = locations.Locations.NONE
    else:
        location_return = list(locations_set)[0]
    print(
        f"Les mots non reconnus dans les actions, lieux ou périphériques : TrashWords : {trash_words}"
    )

    # Retourner les mots normalisés
    return action_return, location_return, device_return


def command_dispatcher(action, location, device):
    """
    Mappe le triplet (action, location, device) à une commande générique.
    L'Enum Command ne dépend plus de la pièce.
    """
    if (
        action == actions.Actions.NONE
        or location == locations.Locations.NONE
        or device == devices.Devices.NONE
    ):
        return commands.Command.NOT_IMPLEMENTED

    if device == devices.Devices.PLUG:
        if action == actions.Actions.ON:
            return commands.Command.PRISE_ON
        elif action == actions.Actions.OFF:
            return commands.Command.PRISE_OFF

    elif device == devices.Devices.LIGHT:
        if action == actions.Actions.ON:
            return commands.Command.LUMIERE_ON
        elif action == actions.Actions.OFF:
            return commands.Command.LUMIERE_OFF

    elif device == devices.Devices.LAMP:
        if action == actions.Actions.ON:
            return commands.Command.LAMPE_ON
        elif action == actions.Actions.OFF:
            return commands.Command.LAMPE_OFF

    elif device == devices.Devices.AMBIENCE:
        if action == actions.Actions.CHILL:
            return commands.Command.AMBIENCE_CHILL
        elif action == actions.Actions.NORMAL:
            return commands.Command.AMBIENCE_NORMAL

    return commands.Command.NOT_IMPLEMENTED
