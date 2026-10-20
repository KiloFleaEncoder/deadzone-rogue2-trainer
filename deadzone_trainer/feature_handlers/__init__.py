from .aimbot import AimbotHandler
from .esp import EspHandler
from .god_mode import GodModeHandler
from .no_recoil import NoRecoilHandler
from .infinite_ammo import InfiniteAmmoHandler

HANDLER_REGISTRY = {
    "aimbot": AimbotHandler,
    "esp": EspHandler,
    "god_mode": GodModeHandler,
    "no_recoil": NoRecoilHandler,
    "infinite_ammo": InfiniteAmmoHandler,
}

__all__ = ["HANDLER_REGISTRY"]