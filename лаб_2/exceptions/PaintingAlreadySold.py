from __future__ import annotations

class PaintingAlreadySold(Exception):
    def __init__(self, message: str = "Painting is already sold"):
        super().__init__(message)