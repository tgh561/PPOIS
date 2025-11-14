from events.Collector import Collector

class DummyPainting:
    def __init__(self, title): self.title = title

def test_buy_and_sell_collection():
    c = Collector("Col")
    p1 = DummyPainting("P1")
    p2 = DummyPainting("P2")
    c.buy_painting(p1)
    c.buy_painting(p2)
    assert p1 in c.collection and p2 in c.collection
    assert c.sell(p1) is True
    assert p1 not in c.collection
    assert c.sell(p1) is False
