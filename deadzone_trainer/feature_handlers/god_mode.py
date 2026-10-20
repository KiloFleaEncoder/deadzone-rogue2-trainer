from __future__ import annotations

from deadzone_trainer.feature_handlers.base import FeatureHandler
from deadzone_trainer.offsets import OFFSETS


class GodModeHandler(FeatureHandler):
    name = "god_mode"

    def tick(self) -> None:
        if not self.enabled:
            return
        local = self.bridge.read_int(self.bridge.module_base + OFFSETS["local_player"])
        if local == 0:
            return
        hp = self.bridge.read_int(local + OFFSETS["health"])
        max_hp = self.bridge.read_int(local + OFFSETS["max_health"])
        if hp < max_hp:
            self.bridge.write_int(local + OFFSETS["health"], max_hp)