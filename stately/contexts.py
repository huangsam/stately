from stately.base import ContextHandling, StateHandling
from stately.constants import INITIAL_STAMINA
from stately.enums import PersonStateKey
from stately.states import PersonPassive


class PersonContext(StateHandling, ContextHandling):
    """Person state context."""

    def __init__(self, name: str):
        self.name: str = name
        self.stamina: int = INITIAL_STAMINA
        self.state: StateHandling = PersonPassive(self)

    def is_tired(self) -> bool:
        return self.stamina < 0

    def can_move_with(self, effort: int) -> bool:
        return self.stamina >= effort

    def lose_energy(self, effort: int):
        self.stamina -= effort

    def gain_energy(self, effort: int):
        self.stamina += effort

    def change_state(self, state: StateHandling):
        self.state = state

    def get_state_key(self) -> PersonStateKey:
        return self.state.get_state_key()

    def walking(self):
        self.state.walking()

    def running(self):
        self.state.running()

    def resting(self):
        self.state.resting()
