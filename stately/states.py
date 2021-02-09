from typing import TYPE_CHECKING

from stately.base import StateHandling
from stately.constants import RESTING_POWER, RUNNING_EFFORT, WALKING_EFFORT
from stately.enums import PersonStateKey

if TYPE_CHECKING:
    # With the State design pattern, one may encounter circumstances
    # where there is a circular dependency issue. In such cases, look
    # at using deferred imports or the `TYPE_CHECKING` to bypass these
    # errors. Make sure to do these kinds of "hacks" in one/few isolated
    # places. Otherwise, other developers will make mistakes and trigger
    # circular dependencies in the rest of the codebase
    from stately.contexts import PersonContext


class PersonActive(StateHandling):
    """Person active - when he/she is exercising."""

    def __init__(self, person_ctx: "PersonContext"):
        self.person_ctx = person_ctx

    def get_state_key(self):
        return PersonStateKey.ACTIVE

    def walking(self):
        print(f"{self.person_ctx.name} is walking")
        self.person_ctx.lose_energy(WALKING_EFFORT)
        if self.person_ctx.is_tired():
            print(f"{self.person_ctx.name} needs a break from walking")
            self.person_ctx.change_state(PersonPassive(self.person_ctx))

    def running(self):
        print(f"{self.person_ctx.name} is running")
        self.person_ctx.lose_energy(RUNNING_EFFORT)
        if self.person_ctx.is_tired():
            print(f"{self.person_ctx.name} needs a break from running")
            self.person_ctx.change_state(PersonPassive(self.person_ctx))

    def resting(self):
        print(f"{self.person_ctx.name} is going home to get some rest")
        self.person_ctx.gain_energy(RESTING_POWER)
        self.person_ctx.change_state(PersonPassive(self.person_ctx))


class PersonPassive(StateHandling):
    """Person passive - when he/she is not exercising."""

    def __init__(self, person_ctx: "PersonContext"):
        self.person_ctx: PersonContext = person_ctx

    def get_state_key(self):
        return PersonStateKey.PASSIVE

    def walking(self):
        if self.person_ctx.can_move_with(WALKING_EFFORT):
            print(f"{self.person_ctx.name} is walking after a break")
            self.person_ctx.lose_energy(WALKING_EFFORT)
            self.person_ctx.change_state(PersonActive(self.person_ctx))
        else:
            print(f"{self.person_ctx.name} cannot walk and needs a break")

    def running(self):
        if self.person_ctx.can_move_with(RUNNING_EFFORT):
            print(f"{self.person_ctx.name} is running after a break")
            self.person_ctx.lose_energy(RUNNING_EFFORT)
            self.person_ctx.change_state(PersonActive(self.person_ctx))
        else:
            print(f"{self.person_ctx.name} cannot run and needs a break")

    def resting(self):
        print(f"{self.person_ctx.name} is resting peacefully")
        self.person_ctx.gain_energy(RESTING_POWER)
