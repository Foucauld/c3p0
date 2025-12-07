from api.phoscon import execute_device, execute_scene, disable_all_lights, get_group_id
from nlu.keywords import Keywords
from nlu.keywords import LIGHTS
from nlu.keywords import AMBIENCES


def execute(action: Keywords, rooms: list, params: list):
    """
    Exécute une commande sur les lumières.
    Pour l'instant, gère seulement enable/disable sur le salon.
    """
    print(f"Execute lights")
    print(f"Action : {action}")
    print(f"Rooms : {rooms}")
    print(f"Params : {params}")
    for room in rooms:
        if room == Keywords.LIVING_ROOM:
            return execute_living_room_actions(action, params)
    print(f"[WARNING] Aucune action définie pour {rooms}")
    return Keywords.UNKNOWN.name


def execute_living_room_actions(action: Keywords, params: list):
    if action == Keywords.ENABLE:
        # Ici tu mettrais l'appel Phoscon pour allumer le salon

        return process_light(Keywords.LIVING_ROOM, params, action)
    elif action == Keywords.DISABLE:
        # Ici tu mettrais l'appel Phoscon pour éteindre le salon

        return process_light(Keywords.LIVING_ROOM, params, action)
    elif action == Keywords.AMBIENCE:
        # Ici tu mettrais l'appel Phoscon pour éteindre le salon
        print("💡 Ambiance dans le salon")
        return process_scene(Keywords.LIVING_ROOM, params)
    else:
        print(f"[WARNING] Action '{action}' non gérée pour lights in living_room")
        return Keywords.UNKNOWN.name


def process_light(room: Keywords, params: list, state: Keywords):
    group_id = get_group_id(room.value)
    if not params:
        if state == Keywords.ENABLE:
            print(f"💡 Allumage de {room.value}")
            execute_scene(group_id, Keywords.AMBIENCE_DEFAULT.value)
            return f"{Keywords.LIGHT.name}_{room.value}_{state.value}"
        elif state == Keywords.DISABLE:
            print(f"💡 Extinction de {room.value}")
            disable_all_lights(group_id)
            return f"{Keywords.LIGHT.name}_{room.value}_{state.value}"
    else:
        lights = LIGHTS.get(room)
        if not lights:
            print(f"[WARNING] Aucune lumière définie pour la pièce {room}")
            return Keywords.UNKNOWN.name
        else:
            for light in lights:
                if light in params:
                    print(
                        f"💡 Action {state.value} dans {room.value} sur {light.value}"
                    )
                    execute_device(light.value, state.value, room.value)
                    return f"{light.name}_{room.value}_{state.value}"
    print(
        f"[WARNING] La lumière proposée ({params}) n'est pas définie pour la pièce {room}"
    )
    return Keywords.UNKNOWN.name


def process_scene(room: Keywords, params: list):
    if not params:
        print("[LIGHT_ACTIONS][PROCESS_SCENE]No params_provided")
        return Keywords.UNKNOWN.name
    else:
        group_id = get_group_id(room.value)
        for ambience in AMBIENCES:
            if ambience in params:
                execute_scene(group_id, ambience.value)
                return f"{ambience.name}"
    print(f"[WARNING] Ambiance ({params}) non définie dans les ambiances : {AMBIENCES}")
    return Keywords.UNKNOWN
