from abc import ABC, abstractmethod


class AbstractDb(ABC):

    @abstractmethod
    def history_save(self, first_number: float, operation: str, second_number: float):
        raise NotImplemented

    @abstractmethod
    def history_load(self) -> list[dict]:
        raise NotImplemented
