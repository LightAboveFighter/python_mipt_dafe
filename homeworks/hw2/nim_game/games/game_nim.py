import json

from nim_game.environments.environment_nim import EnvironmentNim
from nim_game.common.models import NimStateChange, GameState
from nim_game.agents.agent import Agent
from nim_game.common.enumerations import Players


class GameNim:
    _environment: EnvironmentNim        # состояния кучек
    _agent: Agent                       # бот

    def __init__(self, path_to_config: str) -> None:
        with open(path_to_config, "w") as file:
            text = json.load(file)
            heaps_amount = int(text["heaps_amount"])
            opponent_level = str(text["opponent_level"])
            GameNim._environment = EnvironmentNim(heaps_amount)
            GameNim._agent = Agent(opponent_level)

    def make_steps(self, player_step: NimStateChange) -> GameState:
        Game_State = GameState()
        self._environment.change_state(player_step)
        if self.is_game_finished():
            Game_State.winner = Players.USER.value
            return Game_State
        step = self._agent.make_step(self._environment.get_state())
        self._environment.change_state(step)
        Game_State.heaps_state = self._environment.get_state()
        Game_State.opponent_step = step
        if self.is_game_finished():
            Game_State.winner = Players.BOT.value
        return Game_State

    def is_game_finished(self) -> bool:
        return not any(self._environment.get_state())

    @property
    def heaps_state(self) -> list[int]:
        return self._environment.get_state()
