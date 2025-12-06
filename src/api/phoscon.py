import requests

# IP et clé API Phoscon / ConBee III
PHOSCON_IP = "192.168.1.194"
API_KEY = "642D529D1B"


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


def execute_scene(group_id: str, scene_name: str):
    print(f"scene {scene_name}, groupe {group_id}")
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


def disable_all_lights(group_id: str):
    """
    Éteint toutes les lumières du groupe donné en utilisant l'API Phoscon / deCONZ.
    """
    if not group_id:
        print("Erreur : group_id obligatoire pour éteindre les lumières")
        return

    url = f"http://{PHOSCON_IP}:8080/api/{API_KEY}/groups/{group_id}/action"
    payload = {"on": False}  # Éteint toutes les lumières du groupe

    try:
        resp = requests.put(url, json=payload)
        resp.raise_for_status()
        print(f"Toutes les lumières du groupe {group_id} ont été éteintes")
    except requests.RequestException as e:
        print(f"Erreur en éteignant le groupe {group_id} : {e}")


def get_group_id(location: str):
    """Retourne l'ID du groupe correspondant à la location."""
    groups = get_groups()
    for gid, g in groups.items():
        if g.get("name") == location:
            return gid
    return None


def get_groups():
    """Récupère tous les groupes depuis Phoscon."""
    resp = requests.get(f"http://{PHOSCON_IP}:8080/api/{API_KEY}/groups")
    resp.raise_for_status()
    return resp.json()
