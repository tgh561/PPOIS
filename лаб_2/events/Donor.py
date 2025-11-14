from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Exhibit import Exhibit

class Donor:
    def __init__(self, name: str):
        self.name = name
        self.donations: List[Exhibit] = []

    def add_donation(self, exhibit: Exhibit) -> None:
        self.donations.append(exhibit)

    def thank(self) -> str:
        return f"Thank you {self.name}"
