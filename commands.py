from enum import Enum


class Command(Enum):
    NOT_IMPLEMENTED = 0

    # Prises
    PRISE_ON = 1
    PRISE_OFF = 2

    # Lumières
    LUMIERE_ON = 3
    LUMIERE_OFF = 4
    LAMPE_ON = 5
    LAMPE_OFF = 6

    # Ambiances (scènes)
    AMBIENCE_CHILL = 7
    AMBIENCE_NORMAL = 8


def parse_command(command: Command, location: str):
    """
    Transforme un enum Command et une location en triplet complet :
    (device_name, location, action)
    Exemples :
        Command.LUMIERE_ON + "SALON" -> ("LUMIERE_SALON", "SALON", "ON")
        Command.AMBIENCE_CHILL + "SALON" -> ("AMBIENCE_SALON", "SALON", "CHILL")
    """
    if command == Command.NOT_IMPLEMENTED:
        return (None, None, None)

    parts = command.name.split("_")  # ex: ["LUMIERE", "ON"] ou ["AMBIENCE", "CHILL"]
    device_base = parts[0]  # ex: "LUMIERE" ou "AMBIENCE"
    action = "_".join(parts[1:])  # ex: "ON" / "CHILL"

    device_name = f"{device_base}_{location}"  # ex: "LUMIERE_SALON"

    return device_name, location, action
