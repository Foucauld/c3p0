# light_action.py

# Exemple structure des lumières dans Phoscon
ROOM_TO_LIGHTS = {
    "salon": {"ceiling": ["CEILING"], "floor_lamp": ["FLOOR_LAMP"]},
    "cuisine": {"ceiling": ["CEILING_1", "CEILING_2", "CEILING_3"]},
    "bureau": {"ceiling": ["CEILING_1", "CEILING_2", "CEILING_3"]},
    "chambre": {
        "ceiling": ["CEILING_1", "CEILING_2", "CEILING_3"],
        "bed_lamp_left": ["BED_LAMP_1"],
        "bed_lamp_right": ["BED_LAMP_2"],
    },
}


def execute_light_action(action: str, rooms: list, params: list, phoscon_client):
    """
    action : enable / disable
    rooms : ["salon"] ou []
    params : ["ceiling", "floor_lamp"] ou []
    phoscon_client : ton interface vers Phoscon
    """

    to_toggle = []

    # --- 1. Si une room est précisée ---
    if rooms:
        for room in rooms:
            if room not in ROOM_TO_LIGHTS:
                continue

            if params:
                # Paramètres dans une room
                for p in params:
                    if p in ROOM_TO_LIGHTS[room]:
                        to_toggle.extend(ROOM_TO_LIGHTS[room][p])
            else:
                # Pas de paramètres → toute la room
                for lst in ROOM_TO_LIGHTS[room].values():
                    to_toggle.extend(lst)

    # --- 2. Aucun room → paramètres seuls (cas rare mais utile)
    else:
        for room, room_mapping in ROOM_TO_LIGHTS.items():
            for p in params:
                if p in room_mapping:
                    to_toggle.extend(room_mapping[p])

    # --- 3. Absolument aucun contexte → all lights ?
    if not rooms and not params:
        # Sécurité : on pourrait allumer TOUTES les pièces
        for room in ROOM_TO_LIGHTS.values():
            for devices in room.values():
                to_toggle.extend(devices)

    # --- 4. Execution via Phoscon ---
    for device_id in to_toggle:
        if action == "enable":
            phoscon_client.turn_on(device_id)
        elif action == "disable":
            phoscon_client.turn_off(device_id)

    return to_toggle
