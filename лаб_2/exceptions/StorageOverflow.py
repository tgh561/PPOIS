from __future__ import annotations

class StorageOverflow(Exception):
    def __init__(self, message: str = "Storage is overflowed"):
        super().__init__(message)