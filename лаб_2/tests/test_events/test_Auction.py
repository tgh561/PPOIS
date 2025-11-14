# Тесты для класса Auction

from events.Auction import Auction
from events.Bid import Bid

class DummyGalleryHall:
    def __init__(self, name="Hall"): self.name = name

class DummyPainting:
    def __init__(self, title): self.title = title

class DummyBid:
    def __init__(self, amount): self.amount = amount

def test_place_and_close_auction():
    hall = DummyGalleryHall()
    a = Auction("A1", "2025-01-01", hall)
    assert a.name == "A1"
    b = DummyBid(100)
    a.place_bid(b)
    assert b in a.bids
    assert "closed" in a.close_auction()
