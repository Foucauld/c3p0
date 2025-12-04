from typing import Tuple, Optional
from commands import Command
from command_functions import (
    allume_device,
    eteins_device,
    donne_planning,
    ajoute_liste_courses,
)


def execute_command(command_tuple: Optional[Tuple[Command, Optional[str]]]):
    """
    Exécute la commande à partir du tuple (Command, param).
    - command_tuple: (cmd, param) ou None
    """
    if command_tuple is None:
        print("Aucune commande à exécuter")
        return

    cmd, param = command_tuple

    try:
        if param:
            # Certaines fonctions peuvent avoir besoin du paramètre
            cmd.func(cmd.target, param)
        else:
            # Pour les fonctions sans paramètre
            cmd.func(cmd.target)
    except Exception as e:
        print(f"Erreur lors de l'exécution de la commande {cmd.name}: {e}")
