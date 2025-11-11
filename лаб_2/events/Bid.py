from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..entities.Visitor import Visitor
    from ..entities.Painting import Painting

class Bid:
    def __init__(self, amount: float, bidder: Visitor, item: Painting):
        self.amount = amount
        self.bidder = bidder
        self.item = item

    def validate(self) -> bool:
        return self.amount > 0

    def withdraw(self) -> bool:
        return True
