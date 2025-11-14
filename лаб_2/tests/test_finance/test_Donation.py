# Тесты для класса Donation

from finance.Donation import Donation

class DummyVisitor:
    def __init__(self, name): self.name = name

class DummyExhibit: pass

def test_process_and_acknowledge():
    donor = DummyVisitor("Anna")
    d = Donation("D1", 100.0, donor, DummyExhibit())
    assert d.process_donation() is True
    ack = d.acknowledge()
    assert "Thank you" in ack and "Anna" in ack
