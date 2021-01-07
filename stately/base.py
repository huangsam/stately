from abc import ABC, abstractmethod


class State(ABC):

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
