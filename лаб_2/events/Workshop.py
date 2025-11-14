from __future__ import annotations
from typing import List, TYPE_CHECKING
from .Event import Event
if TYPE_CHECKING:
    from ..management.Employee import Employee
    from ..entities.GalleryHall import GalleryHall
class Workshop(Event):
    def __init__(self, name: str, date: str, location: GalleryHall, instructor: Employee):
        super().__init__(name, date, location)
        self.instructor = instructor
        self.materials: List[str] = []

    def start(self) -> str:
        return f"Workshop {self.name} started"

    def end(self) -> str:
        return f"Workshop {self.name} ended"
