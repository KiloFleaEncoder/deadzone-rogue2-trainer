from __future__ import annotations

from deadzone_trainer.feature_handlers.base import FeatureHandler
from deadzone_trainer.offsets import OFFSETS


class InfiniteAmmoHandler(FeatureHandler):
    name = "infinite_ammo"

    def tick(self) -> None:
        if not self.enabled:
            return
        local = self.bridge.read_int(self.bridge.module_base + OFFSETS["local_player"])
        if local == 0:
            return
        weapon = self.bridge.read_int(local + OFFSETS["active_weapon"])
        if weapon == 0:
            return
        reserve = self.bridge.read_int(weapon + OFFSETS["reserve_ammo"])
        if reserve < 999:
            self.bridge.write_int(weapon + OFFSETS["reserve_ammo"], 999)