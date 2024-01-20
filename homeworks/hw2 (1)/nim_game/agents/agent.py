from random import choice, randint

from nim_game.common.enumerations import AgentLevels
from nim_game.common.models import NimStateChange


class Agent:
    """
    В этом классе реализованы стратегии игры для уровней сложности
    """

    _level: AgentLevels         # уровень сложности

    def __init__(self, level: str) -> None:
        if isinstance(level, str) and \
                level in [item.value for item in AgentLevels]:
            self._level = level
        else:
            raise ValueError

    def make_step(self, state_curr: list[int]) -> NimStateChange:
        if self._level == AgentLevels.EASY:
            return easy_step(state_curr)
        if self._level == AgentLevels.NORMAL:
            return choice[easy_step(state_curr), hard_step(state_curr)]
        return hard_step(state_curr)


def easy_step(state_curr: list[int]) -> NimStateChange:
    heap_id = randint(0, len(state_curr) - 1)
    while state_curr[heap_id] == 0:
        heap_id = randint(0, len(state_curr) - 1)
    decrease = randint(1, state_curr[heap_id])
    return NimStateChange(heap_id, decrease)


def hard_step(state_curr: list[int]) -> NimStateChange:
    bit_sum = state_curr[0]
    for i in range(1, len(state_curr)):
        bit_sum ^= state_curr[i]
    for i in range(len(state_curr)):
        if (bit_sum ^ state_curr[i]) < state_curr[i]:
            return NimStateChange(i, state_curr[i] - (bit_sum ^ state_curr[i]))
    return easy_step(state_curr)
