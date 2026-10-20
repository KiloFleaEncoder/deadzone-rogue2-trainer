from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Protocol

from trainer_config import TrainerConfig
from deadzone_trainer.feature_handlers import HANDLER_REGISTRY
from deadzone_trainer.feature_handlers.base import FeatureHandler


class Bridge(Protocol):
    module_base: int
    def read_int(self, addr: int) -> int: ...
    def write_int(self, addr: int, value: int) -> None: ...


@dataclass
class TrainerEngine:
    bridge: Bridge
    config: TrainerConfig
    handlers: list[FeatureHandler] = field(default_factory=list)
    _running: bool = False

    def __post_init__(self) -> None:
        for name, cls in HANDLER_REGISTRY.items():
            if self.config.features.get(name, False):
                self.handlers.append(cls(self.bridge))
        self._log = logging.getLogger("trainer.engine")

    def run(self) -> None:
        self._running = True
        interval = 1.0 / max(1, self.config.poll_hz)
        self._log.info("engine running with %d handler(s)", len(self.handlers))
        while self._running:
            for h in self.handlers:
                try:
                    h.tick()
                except Exception as exc:  # keep the loop alive
                    self._log.warning("handler %s tick error: %s", h.name, exc)
            time.sleep(interval)

    def stop(self) -> None:
        self._running = False