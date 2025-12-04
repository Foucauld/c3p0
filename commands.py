from typing import List, Dict, Callable
import json


class Command:
    def __init__(
        self,
        name: str,
        target: str,
        target_triggers: List[str],
        action: str,
        action_triggers: List[str],
        parameters: Dict[str, List[str]],
        func: Callable,
    ):
        self.name = name
        self.target = target
        self.target_triggers = [w.lower() for w in target_triggers]
        self.action = action
        self.action_triggers = [w.lower() for w in action_triggers]
        self.parameters = {k: [w.lower() for w in v] for k, v in parameters.items()}
        self.func = func

    @staticmethod
    def from_dict(d: dict, func: Callable):
        return Command(
            name=d["name"],
            target=d["target_id"],
            target_triggers=d.get("target_triggers", []),
            action=d["action"],
            action_triggers=d.get("action_triggers", []),
            parameters=d.get("parameters", {}),
            func=func,
        )
