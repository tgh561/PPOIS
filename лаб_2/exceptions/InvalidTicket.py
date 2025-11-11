from __future__ import annotations

class InvalidTicket(Exception):
    def __init__(self, message: str = "Ticket is invalid"):
        super().__init__(message)