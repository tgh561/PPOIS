import pytest
from entities.StorageRoom import StorageRoom

class DummyExhibit:
    def __init__(self, title="E"):
        self.title = title
        self.location = None
    def assign_location(self, loc):
        self.location = loc

def test_store_and_remove_exhibit_sets_location():
    room = StorageRoom(capacity=2)
    ex = DummyExhibit("A")
    room.store_exhibit(ex)
    assert ex in room.current_items
    assert ex.location is room

    room.remove_exhibit(ex)
    assert ex not in room.current_items
    assert ex.location is None

def test_store_ignores_duplicates():
    room = StorageRoom(capacity=2)
    ex = DummyExhibit("A")
    room.store_exhibit(ex)
    room.store_exhibit(ex)  # повторно
    assert len(room.current_items) == 1

def test_is_full_and_overflow():
    room = StorageRoom(capacity=1)
    ex1 = DummyExhibit("A")
    ex2 = DummyExhibit("B")
    room.store_exhibit(ex1)
    assert room.is_full() is True
    with pytest.raises(Exception) as e:
        room.store_exhibit(ex2)
    assert "StorageOverflow" in str(e.value)
