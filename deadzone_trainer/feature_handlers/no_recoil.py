from __future__ import annotations

from deadzone_trainer.feature_handlers.base import FeatureHandler
from deadzone_trainer.offsets import OFFSETS


class NoRecoilHandler(FeatureHandler):
    name = "no_recoil"

    def tick(self) -> None:
        if not self.enabled:
            return
        local = self.bridge.read_int(self.bridge.module_base + OFFSETS["local_player"])
        if local == 0:
            return
        weapon = self.bridge.read_int(local + OFFSETS["active_weapon"])
        if weapon == 0:
            return
        self.bridge.write_int(weapon + OFFSETS["recoil_accumulator"], 0)