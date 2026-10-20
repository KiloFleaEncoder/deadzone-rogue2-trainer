from __future__ import annotations

from deadzone_trainer.feature_handlers.base import FeatureHandler
from deadzone_trainer.overlay_core import OverlayBus
from deadzone_trainer.offsets import OFFSETS


class EspHandler(FeatureHandler):
    name = "esp"

    def __init__(self, bridge) -> None:
        super().__init__(bridge)
        self.bus = OverlayBus.shared()

    def tick(self) -> None:
        if not self.enabled:
            return
        world = self.bridge.read_int(self.bridge.module_base + OFFSETS["world"])
        if world == 0:
            return
        count = self.bridge.read_int(world + OFFSETS["entity_count"])
        # push a lightweight snapshot to the overlay renderer
        self.bus.publish("esp_snapshot", {"world": world, "count": count})