from __future__ import annotations
from typing import List, TYPE_CHECKING

from Employee import Employee 
if TYPE_CHECKING:
    from entities.Exhibition import Exhibition

class Curator(Employee):

    def __init__(self, name: str, position: str = "Curator", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.organized_exhibitions: List["Exhibition"] = []

    def add_exhibition(self, exhibition: "Exhibition") -> None:
        if exhibition not in self.organized_exhibitions:
            self.organized_exhibitions.append(exhibition)

    def list_exhibitions(self) -> List[str]:
        return [ex.name for ex in self.organized_exhibitions]
