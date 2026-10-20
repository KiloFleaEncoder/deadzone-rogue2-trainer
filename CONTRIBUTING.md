# Contributing to deadzone-rogue2-trainer

Thanks for helping out. This trainer targets **Deadzone Rogue 2** on Windows
(Steam build, 2026). It is a hobbyist, educational reverse-engineering project
shared with the modding community.

## Ground rules
- Do **not** commit offsets that were not verified on a fresh game launch.
- Keep trainer features behind a feature flag in `trainer_config/features.toml`.
- Never merge code that patches anticheat-protected memory regions blindly.
- All PRs must rebuild `dumps/offsets.json` via `tools/dump_offsets.py`.

## Dev setup
```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m deadzone_trainer.bootstrap
```

## Style
- `ruff` + `black` defaults.
- No wildcard imports.
- Every handler in `feature_handlers/` exposes `enable()` / `disable()` / `tick()`.

## Testing
`pytest tests/` — tests use the memory stubs in `tests/fake_process.py`
so no live game process is required.

## Reporting issues
Attach the `logs/trainer.log` tail and your game build hash from
`dumps/offsets.json` -> `build_hash`.