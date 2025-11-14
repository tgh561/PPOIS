# Тесты для класса Event

from events.Event import Event

class DummyGalleryHall:
    def __init__(self, name="H"): self.name = name

class DummyVisitor:
    def __init__(self, name="V"): self.name = name

def test_register_and_cancel():
    hall = DummyGalleryHall()
    ev = Event("E1", "2025-02-02", hall)
    v = DummyVisitor()
    ev.register_participant(v)
    assert v in ev.participants
    ev.cancel()
    assert ev.participants == []
