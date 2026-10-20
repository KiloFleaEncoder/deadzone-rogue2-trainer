# Security Policy

## Scope
This repository is a **Deadzone Rogue 2 trainer** for offline / private-server
use. It attaches to the game process via `pymem` and writes to known memory
offsets. Use at your own risk — online use may violate the game's ToS and can
result in a ban.

## Supported versions
| Game build | Trainer branch |
|------------|----------------|
| 2026.1.x   | main           |
| 2026.0.x   | legacy/2026.0  |

## Reporting a vulnerability
If you find something that could damage a user's install (e.g. a bad memory
write that corrupts save data), open a private security advisory rather than a
public issue. Include:
- game build hash
- trigger steps
- resulting corruption

We aim to respond within 72 hours.

## Out of scope
- "How do I bypass X anticheat" — not our problem, not our feature.
- Requests for online-only exploits. This trainer is for the offline sandbox.