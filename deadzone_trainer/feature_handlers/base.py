from __future__ import annotations

from abc import ABC, abstractmethod


class FeatureHandler(ABC):
    name: str = "base"

    def __init__(self, bridge) -> None:
        self.bridge = bridge
        self.enabled = False

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    @abstractmethod
    def tick(self) -> None:
        """Called every engine poll tick."""