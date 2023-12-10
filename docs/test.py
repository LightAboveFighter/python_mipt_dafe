from enum import Enum

class Actions(Enum):
    BAD = "bad person",
    GOOD = "good situation"

print("bad person" == str(Actions.BAD))
