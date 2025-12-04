# commandes.py
from typing import Callable


class Command:
    def __init__(
        self,
        name: str,
        target: str,
        action: str,
        func: Callable,
        location_required: bool = False,
    ):
        self.name = name
        self.target = target  # lumière, prise, planning, liste_de_courses
        self.action = action  # allumer, éteindre, donner, ajouter
        self.func = func  # fonction à appeler
        self.location_required = location_required
