from __future__ import annotations

class HallCapacityExceeded(Exception):
    def __init__(self, message: str = "Hall capacity exceeded"):
        super().__init__(message)