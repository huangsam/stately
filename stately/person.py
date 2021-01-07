from stately.base import State
from stately.enums import PersonStateKey

_INITIAL_STAMINA = 5
_WALKING_EFFORT = 2
_RUNNING_EFFORT = 3
_RESTING_POWER = 5


# Placed Person here to avoid cyclic dependencies. The con though is that too
# much code may end up living in one module. An alternative solution is to
# actually defer the PassiveState import until the constructor of Person is
# invoked. See the following resource for more tips:
# https://stackabuse.com/python-circular-imports/
class Person(State):
    def __init__(self, name: str):
        self.name = name
        self.stamina = _INITIAL_STAMINA
        self.state = PassiveState(self)

    def get_state_key(self) -> PersonStateKey:
        return self.state.get_state_key()

    def is_tired(self) -> bool:
        return self.stamina < 0

    def can_move(self, effort: int) -> bool:
        return self.stamina >= effort

    def lose_energy(self, effort: int):
        self.stamina -= effort

    def gain_energy(self, effort: int):
        self.stamina += effort

    def change_state(self, state: State):
        self.state = state

    def walking(self):
        self.state.walking()

    def running(self):
        self.state.running()

    def resting(self):
        self.state.resting()


class ActiveState(State):
    def __init__(self, context: Person):
        self.person: Person = context

    def get_state_key(self):
        return PersonStateKey.ACTIVE

    def walking(self):
        print(f"{self.person.name} is walking")
        self.person.lose_energy(_WALKING_EFFORT)
        if self.person.is_tired():
            print(f"{self.person.name} needs a break from walking")
            self.person.change_state(PassiveState(self.person))

    def running(self):
        print(f"{self.person.name} is running")
        self.person.lose_energy(_RUNNING_EFFORT)
        if self.person.is_tired():
            print(f"{self.person.name} needs a break from running")
            self.person.change_state(PassiveState(self.person))

    def resting(self):
        print(f"{self.person.name} is going home to get some rest")
        self.person.gain_energy(_RESTING_POWER)
        self.person.change_state(PassiveState(self.person))


class PassiveState(State):
    def __init__(self, context: Person):
        self.person: Person = context

    def get_state_key(self):
        return PersonStateKey.PASSIVE

    def walking(self):
        if self.person.can_move(_WALKING_EFFORT):
            print(f"{self.person.name} is walking after a break")
            self.person.lose_energy(_WALKING_EFFORT)
            self.person.change_state(ActiveState(self.person))
        else:
            print(f"{self.person.name} cannot walk and needs a break")

    def running(self):
        if self.person.can_move(_RUNNING_EFFORT):
            print(f"{self.person.name} is running after break")
            self.person.lose_energy(_RUNNING_EFFORT)
            self.person.change_state(ActiveState(self.person))
        else:
            print(f"{self.person.name} cannot run and needs a break")

    def resting(self):
        print(f"{self.person.name} is resting peacefully")
        self.person.gain_energy(_RESTING_POWER)
