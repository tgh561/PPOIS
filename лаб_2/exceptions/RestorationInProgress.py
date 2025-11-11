from __future__ import annotations

class RestorationInProgress(Exception):
    def __init__(self, message: str = "Restoration in progress"):
        super().__init__(message)