from __future__ import annotations
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from ..entities.Painting import Painting

class Collector:
    def __init__(self, name: str):
        self.name = name
        self.collection: List[Painting] = []

    def buy_painting(self, painting: Painting) -> None:
        self.collection.append(painting)

    def sell(self, painting: Painting) -> bool:
        if painting in self.collection:
            self.collection.remove(painting)
            return True
        return False
