from random import choice, randint

from nim_game.common.enumerations import AgentLevels
from nim_game.common.models import NimStateChange


class Agent:
    """
    В этом классе реализованы стратегии игры для уровней сложности
    """

    _level: AgentLevels         # уровень сложности

    def __init__(self, level: str) -> None:
        if isinstance(level, str) and level in [i.value for i in AgentLevels]:
            self._level = level
        else:
            raise ValueError

    def _calculate_nim_sum(self, state_curr: list[int]) -> bool:
        ans = state_curr[0]
        for i in range(1, len(state_curr)):
            ans = ans ^ state_curr[i]
        return bool(ans)

    def _make_easy_step(self, state_curr: list[int]) -> NimStateChange:
        heap_num = randint(0, len(state_curr))
        while state_curr[heap_num] == 0:
            heap_num = randint(0, len(state_curr))
        stones_num = randint(1, state_curr[heap_num])
        return NimStateChange(heap_num, stones_num)
    def _make_hard_step(self, state_curr: list[int]) -> NimStateChange:
        test_curr = state_curr[::]
        for i in range(len(state_curr)):
            for j in range(1, state_curr[i]):
                test_curr[i] -= j
                if self._calculate_nim_sum(test_curr):
                    return NimStateChange(i, j)
                test_curr[i] += j
        return self._make_easy_step(state_curr)

    def make_step(self, state_curr: list[int]) -> NimStateChange:
        
        if self._level == AgentLevels.EASY:
            return NimStateChange(self._make_easy_step(state_curr))
        if self._level == AgentLevels.NORMAL:
            if randint(0, 1):
                return NimStateChange(self._make_easy_step(state_curr))
            return NimStateChange(self._make_hard_step(state_curr))
        if self._level == AgentLevels.HARD:
            return NimStateChange(self._make_hard_step(state_curr))


