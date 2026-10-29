from abc import ABC, abstractmethod


class AbstractDb(ABC):
    @abstractmethod
    def history_save(
        self, first_number: float, operation: str, second_number: float, session_id: str = "default"
    ):
        raise NotImplementedError

    @abstractmethod
    def history_load(
        self, operation: str | None = None, session_id: str | None = None
    ) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def history_clear(self, session_id: str | None = None):
        raise NotImplementedError
