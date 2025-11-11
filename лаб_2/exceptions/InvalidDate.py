from __future__ import annotations

class InvalidDate(Exception):
    def __init__(self, message: str = "Invalid date"):
        super().__init__(message)