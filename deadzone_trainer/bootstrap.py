from __future__ import annotations

import logging
import sys

from trainer_config import load_config
from deadzone_trainer.core.engine import TrainerEngine
from deadzone_trainer.core.process_bridge import ProcessBridge
from shared.logging_setup import setup_logging


def main() -> int:
    cfg = load_config()
    setup_logging(cfg.log_level)
    log = logging.getLogger("trainer.bootstrap")

    log.info("Deadzone Rogue 2 Trainer starting (poll=%dHz)", cfg.poll_hz)
    bridge = ProcessBridge(cfg.process_name)
    try:
        bridge.attach()
    except RuntimeError as exc:
        log.error("attach failed: %s", exc)
        return 1

    engine = TrainerEngine(bridge=bridge, config=cfg)
    try:
        engine.run()
    except KeyboardInterrupt:
        log.info("shutdown requested")
    finally:
        bridge.detach()
    return 0


if __name__ == "__main__":
    sys.exit(main())