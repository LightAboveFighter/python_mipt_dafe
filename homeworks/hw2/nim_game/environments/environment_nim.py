from random import randint

from nim_game.common.models import NimStateChange


STONE_AMOUNT_MIN = 1        # минимальное начальное число камней в кучке
STONE_AMOUNT_MAX = 10       # максимальное начальное число камней в кучке


class EnvironmentNim:
    """
    Класс для хранения и взаимодействия с кучками
    """

    _heaps: list[int]       # кучки

    def __init__(self, heaps_amount: int) -> None:

        if heaps_amount < 2 or heaps_amount > 10:
            raise ValueError("Incorrect heaps amount")
        EnvironmentNim._heaps = [0]*heaps_amount
        for i in range(len(EnvironmentNim._heaps)):
            EnvironmentNim._heaps[i] = randint(STONE_AMOUNT_MIN, STONE_AMOUNT_MAX)

    def get_state(self) -> list[int]:
        return EnvironmentNim._heaps
    def change_state(self, state_change: NimStateChange) -> None:

        if state_change.heap_id < 0 or state_change.heap_id > len(EnvironmentNim._heaps):
            raise ValueError("Decraasing from incorrect heap")
        if (state_change.decrease < 1 or state_change.decrease >
        EnvironmentNim._heaps[state_change.heap_id]):
            raise ValueError("Decreasing incorrect num of stones")
        EnvironmentNim._heaps[state_change.heap_id] -= state_change.decrease