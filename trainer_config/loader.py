from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class TrainerConfig:
    process_name: str = "DeadzoneRogue2-Win64-Shipping.exe"
    hotkey_menu: str = "INSERT"
    hotkey_aimbot: str = "F1"
    hotkey_esp: str = "F2"
    hotkey_god: str = "F3"
    poll_hz: int = 60
    log_level: str = "INFO"
    features: dict[str, bool] = field(default_factory=dict)


def load_config(path: str | Path = "trainer_config/features.toml") -> TrainerConfig:
    p = Path(path)
    if not p.exists():
        return TrainerConfig()
    data = tomllib.loads(p.read_text(encoding="utf-8"))
    proc = data.get("process", {})
    hotkeys = data.get("hotkeys", {})
    return TrainerConfig(
        process_name=proc.get("name", TrainerConfig.process_name),
        hotkey_menu=hotkeys.get("menu", "INSERT"),
        hotkey_aimbot=hotkeys.get("aimbot", "F1"),
        hotkey_esp=hotkeys.get("esp", "F2"),
        hotkey_god=hotkeys.get("god", "F3"),
        poll_hz=int(data.get("poll_hz", 60)),
        log_level=data.get("log_level", "INFO"),
        features=data.get("features", {}),
    )