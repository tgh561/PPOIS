# Тесты для класса Bid

from events.Bid import Bid

class DummyVisitor:
    def __init__(self, name="V"): self.name = name

class DummyPainting:
    def __init__(self, title="P"): self.title = title

def test_validate_and_withdraw():
    v = DummyVisitor()
    p = DummyPainting()
    bid = Bid(50.0, v, p)
    assert bid.validate() is True
    assert bid.withdraw() is True
    bad = Bid(0.0, v, p)
    assert bad.validate() is False
