from __future__ import annotations

import logging

try:
    import pymem  # type: ignore
except ImportError:  # allow tests / dev on non-Windows
    pymem = None


class ProcessBridge:
    """Thin wrapper over pymem for a single attached game process."""

    def __init__(self, process_name: str) -> None:
        self.process_name = process_name
        self.pm = None
        self.module_base = 0
        self._log = logging.getLogger("trainer.bridge")

    def attach(self) -> None:
        if pymem is None:
            raise RuntimeError("pymem not installed")
        try:
            self.pm = pymem.Pymem(self.process_name)
        except Exception as exc:
            raise RuntimeError(f"cannot attach to {self.process_name}: {exc}") from exc
        mod = pymem.process.module_from_name(
            self.pm.process_handle, self.process_name
        )
        self.module_base = mod.lpBaseOfDll
        self._log.info("attached to %s base=0x%X", self.process_name, self.module_base)

    def detach(self) -> None:
        if self.pm is not None:
            try:
                self.pm.close_process()
            except Exception:
                pass
            self.pm = None

    def read_int(self, addr: int) -> int:
        assert self.pm is not None
        return int(self.pm.read_int(addr))

    def write_int(self, addr: int, value: int) -> None:
        assert self.pm is not None
        self.pm.write_int(addr, value)