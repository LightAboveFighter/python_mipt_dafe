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

    def calculate_nim_sum(self, state_curr: list[int]) -> bool:
        ans = state_curr[0]
        for i in range(1, len(state_curr)):
            ans = ans ^ state_curr[i]
        return bool(ans)

    def easy_step(self, state_curr: list[int]) -> NimStateChange:
        heap_id = randint(0, len(state_curr)-1)
        while state_curr[heap_id] == 0:
            heap_id = randint(0, len(state_curr)-1)
        stones_num = randint(1, state_curr[heap_id])
        return NimStateChange(heap_id, stones_num)

    def hard_step(self, state_curr: list[int]) -> NimStateChange:
        test_curr = state_curr[::]
        for i in range(len(state_curr)):
            for j in range(1, state_curr[i]):
                test_curr[i] -= j
                if self.calculate_nim_sum(test_curr):
                    return NimStateChange(i+1, j)
                test_curr[i] += j
        return self.easy_step(state_curr)

    def make_step(self, state_curr: list[int]) -> NimStateChange:

        if self._level == AgentLevels.EASY.value:
            return self.easy_step(state_curr)
        if self._level == AgentLevels.NORMAL.value:
            return choice[self.easy_step(state_curr),
                          self.hard_step(state_curr)]
        return self.hard_step(state_curr)
