"""Camera interface used by the NeuroWood core."""

from abc import ABC, abstractmethod

import numpy as np


class Camera(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def capture(self) -> np.ndarray:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass
