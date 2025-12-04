import requests
from commands import Command, parse_command

# IP et clé API Phoscon / ConBee III
PHOSCON_IP = "192.168.1.194"
API_KEY = "642D529D1B"


def get_groups():
    """Récupère tous les groupes depuis Phoscon."""
    resp = requests.get(f"http://{PHOSCON_IP}:8080/api/{API_KEY}/groups")
    resp.raise_for_status()
    return resp.json()


def get_group_id(location: str):
    """Retourne l'ID du groupe correspondant à la location."""
    groups = get_groups()
    for gid, g in groups.items():
        if g.get("name") == location:
            return gid
    return None


def execute_scene(group_id: str, scene_name: str):
    """Rappelle la scène scene_name dans le groupe group_id."""
    resp = requests.get(
        f"http://{PHOSCON_IP}:8080/api/{API_KEY}/groups/{group_id}/scenes"
    )
    resp.raise_for_status()
    scenes = resp.json()

    scene_id = None
    for sid, scene in scenes.items():
        if scene.get("name") == scene_name:
            scene_id = sid
            break

    if scene_id:
        recall_url = f"http://{PHOSCON_IP}:8080/api/{API_KEY}/groups/{group_id}/scenes/{scene_id}/recall"
        requests.put(recall_url)
        print(f"Scène {scene_name} activée dans le groupe {group_id}")
    else:
        print(f"Scène {scene_name} non trouvée dans le groupe {group_id}")


def execute_device(device_name: str, action: str, location: str):
    """Met à jour l'état du device normal (lumière, prise, etc.)"""
    if not location:
        print(f"Erreur : location obligatoire pour le device {device_name}")
        return

    full_device_name = f"{device_name}_{location}"
    resp = requests.get(f"http://{PHOSCON_IP}:8080/api/{API_KEY}/lights")
    resp.raise_for_status()
    lights = resp.json()

    for light_id, light in lights.items():
        if light.get("name") == full_device_name:
            url = f"http://{PHOSCON_IP}:8080/api/{API_KEY}/lights/{light_id}/state"
            payload = {"on": True} if action.upper() == "ON" else {"on": False}
            requests.put(url, json=payload)
            print(f"{full_device_name} mis à jour : {action}")
            return

    print(f"Device {full_device_name} non trouvé dans Phoscon")


def execute_command(command: Command, location: str = None):
    """
    Exécute la commande sur Phoscon :
    - pour les devices normaux : PUT /lights/<id>/state
    - pour les ambiances : PUT /groups/<group_id>/scenes/<scene_id>/recall
    """
    device_name, loc, action = parse_command(command, location)
    print(
        f"Ambiance : device_name : {device_name}, action : {action}, location : {loc}, command : {command}, location : {location}"
    )

    if device_name is None:
        print("Commande non implémentée")
        return

    try:
        # Cas ambiance
        if device_name.startswith("AMBIENCE"):
            if loc:
                group_id = get_group_id(loc)
                if group_id:
                    execute_scene(group_id, action)
                else:
                    print(f"Groupe '{loc}' non trouvé")
            else:
                # appliquer la scène à tous les groupes
                groups = get_groups()
                for gid in groups.keys():
                    execute_scene(gid, action)

        # Cas device normal
        else:
            execute_device(device_name, action, loc)

    except requests.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Phoscon : {e}")
