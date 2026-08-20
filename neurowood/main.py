"""NeuroWood 2.0 entry point - simulation milestone."""

from core.pipeline import NeuroWoodPipeline
from hardware.simulated_camera import SimulatedCamera
from hardware.simulated_plc import SimulatedPLC
from storage.logging_config import setup_logging


def main() -> None:
    logger = setup_logging()
    logger.info("APP_STARTED mode=simulation")

    camera = SimulatedCamera()
    plc = SimulatedPLC()

    try:
        camera.open()
        plc.connect()
        logger.info("SIMULATED_HARDWARE_READY")

        pipeline = NeuroWoodPipeline(camera=camera, plc=plc, logger=logger)
        result = pipeline.run_once()

        print("NeuroWood 2.0 simulation completed")
        print(f"Board: {result.board_id}")
        print(f"Result: {result.classification}")
        print(f"Processing: {result.processing_time_ms:.2f} ms")
    finally:
        camera.close()
        plc.disconnect()
        logger.info("APP_STOPPED")


if __name__ == "__main__":
    main()
