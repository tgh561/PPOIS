from __future__ import annotations

class VisitorNotRegistered(Exception):
    def __init__(self, message: str = "Visitor not registered"):
        super().__init__(message)