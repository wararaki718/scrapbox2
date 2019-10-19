from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def test(self):
        raise NotImplementedError
