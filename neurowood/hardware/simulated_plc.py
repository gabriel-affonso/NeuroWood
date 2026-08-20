"""Simple PLC simulator for development without Siemens hardware."""

from core.models import BoardResult
from hardware.plc import PLC


class SimulatedPLC(PLC):
    def __init__(self):
        self._connected = False
        self.last_result = None

    def connect(self) -> None:
        self._connected = True

    def send_result(self, result: BoardResult) -> None:
        if not self._connected:
            raise RuntimeError("Simulated PLC is not connected")
        self.last_result = result

    def disconnect(self) -> None:
        self._connected = False

    def is_connected(self) -> bool:
        return self._connected
