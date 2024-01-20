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
            raise ValueError("Incorrect difficulty")

    def calculate_nim_sum(self, state_curr: list[int]) -> bool:
        ans = state_curr[0]
        for i in range(1, len(state_curr)):
            ans ^= state_curr[i]
        return bool(ans)

    def easy_step(self, state_curr: list[int]) -> NimStateChange:
        not_null_id = [i for i in range(len(state_curr)) if state_curr[i] != 0]
        heap_id = choice(not_null_id)
        stones_num = randint(1, state_curr[heap_id])
        return NimStateChange(heap_id, stones_num)

    def hard_step(self, state_curr: list[int]) -> NimStateChange:
        test_curr = state_curr.copy()
        print("[hard_step] ", state_curr)
        for heap_id in range(len(state_curr)):
            print("[hard step]", heap_id)
            if state_curr[heap_id] == 0:
                print("[hard step] continued ", heap_id)
                continue
            for stones_to_take in range(1, state_curr[heap_id]):
                test_curr[heap_id] -= stones_to_take
                if self.calculate_nim_sum(test_curr):
                    print("[hard_step] ", "calc", NimStateChange(heap_id, stones_to_take))
                    return NimStateChange(heap_id, stones_to_take)
                test_curr[heap_id] += stones_to_take
        return self.easy_step(state_curr)

    def make_step(self, state_curr: list[int]) -> NimStateChange:

        if self._level == AgentLevels.EASY.value:
            return self.easy_step(state_curr)
        if self._level == AgentLevels.NORMAL.value:
            if choice[1, 0]:
                return self.easy_step(state_curr)
            return self.hard_step(state_curr)
        return self.hard_step(state_curr)
