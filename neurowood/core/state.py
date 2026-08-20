"""Operational states for NeuroWood 2.0."""

from enum import Enum, auto


class SystemState(Enum):
    STARTING = auto()
    READY = auto()
    WAITING_PIECE = auto()
    CAPTURING = auto()
    PROCESSING = auto()
    REPORTING = auto()
    STOPPED = auto()
    FAULT = auto()
