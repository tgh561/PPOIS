from entities.Gallery import Gallery
from entities.Painting import Painting
from entities.Artist import Artist

class DummyAddress: pass
class DummyHall:
    def __init__(self, exhibits): self.exhibits = exhibits
    def find_exhibit_by_title(self, title):
        for e in self.exhibits:
            if e.title == title: return e

def test_find_painting_in_halls_and_collections():
    artist = Artist("Моне", 1840)
    p1 = Painting("Sunset", artist)
    hall = DummyHall([p1])
    g = Gallery("G", DummyAddress())
    g.add_hall(hall)
    assert g.find_painting("Sunset") == p1

    p2 = Painting("Moonlight", artist)
    g.collections.append(p2)
    assert g.find_painting("Moonlight") == p2

def test_list_all_exhibits():
    artist = Artist("Моне", 1840)
    p1 = Painting("A", artist)
    p2 = Painting("B", artist)
    hall = DummyHall([p1])
    g = Gallery("G", DummyAddress())
    g.add_hall(hall)
    g.collections.append(p2)
    all_ex = g.list_all_exhibits()
    assert p1 in all_ex and p2 in all_ex
