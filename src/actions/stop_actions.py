from nlu.keywords import Keywords


def execute(action: str, rooms: list, params: list):
    print(f"Execute plug")
    print(f"Action : {action}")
    print(f"Rooms : {rooms}")
    print(f"Params : {params}")
    return Keywords.STOP.value
