"""Simple camera simulator for development without Basler hardware."""

import numpy as np

from hardware.camera import Camera


class SimulatedCamera(Camera):
    def __init__(self, width: int = 1280, height: int = 720):
        self.width = width
        self.height = height
        self._connected = False
        self._frame_id = 0

    def open(self) -> None:
        self._connected = True

    def capture(self) -> np.ndarray:
        if not self._connected:
            raise RuntimeError("Simulated camera is not open")

        self._frame_id += 1
        # Neutral grayscale frame. Real recorded frames will replace this later.
        return np.full((self.height, self.width), 128, dtype=np.uint8)

    def close(self) -> None:
        self._connected = False

    def is_connected(self) -> bool:
        return self._connected
