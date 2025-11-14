from __future__ import annotations
from typing import List, TYPE_CHECKING
from .Event import Event
if TYPE_CHECKING:
    from ..entities.Painting import Painting
    from .Bid import Bid
    from ..entities.GalleryHall import GalleryHall

class Auction(Event):
    def __init__(self, name: str, date: str, location: GalleryHall):
        super().__init__(name, date, location)
        self.items: List[Painting] = []
        self.bids: List[Bid] = []

    def place_bid(self, bid: Bid) -> None:
        self.bids.append(bid)

    def close_auction(self) -> str:
        return f"Auction {self.name} closed"