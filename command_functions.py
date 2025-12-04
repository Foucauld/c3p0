# command_functions.py


def allume_device(target: str, param: str = None):
    """
    Allume un device ou un groupe.
    - target: identifiant du device ou du groupe
    - param: optionnel, identifiant spécifique dans le groupe
    """
    if param:
        print(f"Allumage de {param} dans {target}")
        # Ici tu appelles l'API Phoscon ou autre pour allumer ce device précis
    else:
        print(f"Allumage de tout le groupe {target}")
        # Ici tu appelles l'API pour allumer tout le groupe


def eteins_device(target: str, param: str = None):
    """
    Éteint un device ou un groupe.
    """
    if param:
        print(f"Extinction de {param} dans {target}")
    else:
        print(f"Extinction de tout le groupe {target}")


def donne_planning(target: str, param: str = None):
    """
    Récupère et affiche le planning.
    """
    print("Voici le planning de la journée")


def ajoute_liste_courses(target: str, param: str = None):
    """
    Récupère et affiche le planning.
    """
    print("Voici le planning de la journée")
