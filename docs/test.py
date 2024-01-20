from enum import Enum

class Actions(Enum):
    BAD = "bad person"
    GOOD = "good situation"
a = Actions.BAD.value
print(a)
