import json

from nim_game.environments.environment_nim import EnvironmentNim
from nim_game.common.models import NimStateChange, GameState
from nim_game.agents.agent import Agent
from nim_game.common.enumerations import Players


class GameNim:
    _environment: EnvironmentNim        # состояния кучек
    _agent: Agent                       # бот

    def __init__(self, path_to_config: str) -> None:
        file = open(path_to_config, "r")
        text = file.readline()
        for i in range(len(text)-14):
            if text[i:i+12] == "heaps_amount":
                heaps_amount = text[i+14]
                j = 1
                while text[i+14+j] != ",":
                    heaps_amount += text[i+14+j]
                    j += 1
                self._environment = EnvironmentNim(int(heaps_amount))
            if text[i:i+14] == "opponent_level":
                self._agent = Agent(text[i+17:i+21])

    def make_steps(self, player_step: NimStateChange) -> GameState:
        self._environment.change_state(player_step)
        if self.is_game_finished():
            return GameState(Players.USER, player_step)
        step = self._agent.make_step(self._environment.get_state)
        self._environment.change_state(step)
        if self.is_game_finished():
            return GameState(Players.BOT, step, self._environment.get_state)
        return GameState(None, step, self._environment.get_state)
        pass

    def is_game_finished(self) -> bool:
        return not any(self._environment.get_state)

    @property
    def heaps_state(self) -> list[int]:
        return self._environment.get_state()
