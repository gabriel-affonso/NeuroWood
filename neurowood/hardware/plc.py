"""PLC interface used by the NeuroWood core."""

from abc import ABC, abstractmethod

from core.models import BoardResult


class PLC(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def send_result(self, result: BoardResult) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass
