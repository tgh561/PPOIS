from __future__ import annotations
from typing import List, TYPE_CHECKING
from .Event import Event
if TYPE_CHECKING:
    from ..management.Guide import Guide
    from ..entities.Exhibit import Exhibit
    from ..entities.GalleryHall import GalleryHall
class Tour(Event):
    def __init__(self, name: str, date: str, location: GalleryHall, guide: Guide):
        super().__init__(name, date, location)
        self.guide = guide
        self.exhibits: List[Exhibit] = []

    def conduct(self) -> str:
        return f"Tour {self.name} conducted by {self.guide.name}"

    def feedback(self, score: int) -> None:
        pass
