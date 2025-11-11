from __future__ import annotations

class ExhibitionFull(Exception):
    def __init__(self, message: str = "Exhibition is full"):
        super().__init__(message)