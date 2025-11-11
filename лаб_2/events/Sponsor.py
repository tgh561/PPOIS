from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Event import Event

class Sponsor:
    def __init__(self, name: str, contribution: float, event: Event):
        self.name = name
        self.contribution = contribution
        self.event = event

    def donate(self, amount: float) -> None:
        self.contribution += amount

    def get_perks(self) -> str:
        return "VIP access"
