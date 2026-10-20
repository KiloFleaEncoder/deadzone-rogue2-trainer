from __future__ import annotations

from deadzone_trainer.feature_handlers.base import FeatureHandler
from deadzone_trainer.offsets import OFFSETS


class AimbotHandler(FeatureHandler):
    name = "aimbot"

    def tick(self) -> None:
        if not self.enabled:
            return
        # target selection is handled in overlay-core; here we only force the
        # local player's aim vector toward the currently locked target.
        local = self.bridge.read_int(self.bridge.module_base + OFFSETS["local_player"])
        if local == 0:
            return
        target = self.bridge.read_int(local + OFFSETS["current_aim_target"])
        if target == 0:
            return
        self.bridge.write_int(local + OFFSETS["aim_lock_flag"], 1)