from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from management.Technician import Technician
    from exceptions.InvalidDate import InvalidDate

class MaintenanceLog:
    def __init__(self, date: str, technician: Technician):
        self.date = date
        self.technician = technician
        self.entries: List[str] = []

    def log(self, description: str) -> None:
        if not self.date:
            raise InvalidDate()
        self.entries.append(description)

    def review(self) -> str:
        return "; ".join(self.entries)
