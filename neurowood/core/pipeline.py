"""Main inspection pipeline for NeuroWood 2.0.

The first version intentionally remains small. Vision algorithms will be
migrated into this pipeline incrementally after the simulated hardware layer
is validated.
"""

from datetime import datetime
from time import perf_counter
from uuid import uuid4

from core.models import BoardResult


class NeuroWoodPipeline:
    def __init__(self, camera, plc, logger):
        self.camera = camera
        self.plc = plc
        self.logger = logger

    def run_once(self) -> BoardResult:
        start = perf_counter()
        frame = self.camera.capture()

        # Temporary result used only to validate the 2.0 architecture.
        result = BoardResult(
            board_id=f"NW-{uuid4().hex[:8].upper()}",
            timestamp=datetime.now(),
            classification="SIMULATION_OK" if frame is not None else "NO_FRAME",
            processing_time_ms=(perf_counter() - start) * 1000,
        )

        self.plc.send_result(result)
        self.logger.info(
            "BOARD_PROCESSED board_id=%s classification=%s processing_ms=%.2f",
            result.board_id,
            result.classification,
            result.processing_time_ms,
        )
        return result
