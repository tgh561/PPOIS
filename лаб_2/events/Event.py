from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.GalleryHall import GalleryHall
    from entities.Visitor import Visitor

class Event:
    def __init__(self, name: str, date: str, location: GalleryHall):
        self.name = name
        self.date = date
        self.location = location
        self.participants: List[Visitor] = []

    def register_participant(self, visitor: Visitor) -> None:
        if visitor not in self.participants:
            self.participants.append(visitor)

    def cancel(self) -> bool:
        self.participants = []
        return True
