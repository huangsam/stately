from abc import ABC, abstractmethod


class StateHandling(ABC):
    """State interface."""

    @abstractmethod
    def get_state_key(self):
        raise LookupError

    @abstractmethod
    def walking(self):
        raise NotImplementedError

    @abstractmethod
    def running(self):
        raise NotImplementedError

    @abstractmethod
    def resting(self):
        raise NotImplementedError


class ContextHandling(ABC):
    """Context interface."""

    @abstractmethod
    def change_state(self, state: StateHandling):
        raise NotImplementedError
