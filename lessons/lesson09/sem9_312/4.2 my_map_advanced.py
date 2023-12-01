""" управляемый map """

from enum import Enum
from itertools import zip_longest
from random import randint


class MapTypes(Enum):
    SHORTEST = 'short'
    LONGEST = 'long'

# Напишите функцию my_map() с дополнительными именованными аргументами 'type' и 'fill_value'.
# Если 'type' равен MapTypes.SHORTEST, то my_map должен работать как и встроенный map, обрезая
# все пришедшие коллекции по длине самой короткой коллекции.
# Если 'type' равен MapTypes.LONGEST, то все коллекции расширяются до длины самой длинной
# коллекции, а недостающие значения заоплняются значением 'fill_value'.

def my_map(func, *args, type=MapTypes.SHORTEST, fill_value=0):
    if type == MapTypes.SHORTEST:
        for elems in zip(*args):
            yield func(*elems)
    if type == MapTypes.LONGEST:
        for elems in zip_longest(*args, fillvalue=fill_value):
            yield func(*elems)   

ch = [randint(-9, 9) for _ in range(10)]
ch2 = [randint(-9, 9) for _ in range(7)]
print(*ch)
print(*ch2)
print(*list(my_map(lambda x, y: x * y, ch, ch2, type=MapTypes.LONGEST, fill_value=11)))