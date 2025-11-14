# Тесты для класса GalleryHall

import pytest
from entities.GalleryHall import GalleryHall
from entities.Artist import Artist
from entities.Exhibit import Exhibit

def test_add_remove_exhibit():
    hall = GalleryHall("Hall", capacity=1)
    artist = Artist("Моне", 1840)
    ex = Exhibit("Кувшинки", artist)
    hall.add_exhibit(ex)
    assert ex in hall.exhibits
    hall.remove_exhibit(ex)
    assert ex not in hall.exhibits

def test_capacity_limit():
    hall = GalleryHall("Hall", capacity=1)
    artist = Artist("Моне", 1840)
    ex1 = Exhibit("A", artist)
    ex2 = Exhibit("B", artist)
    hall.add_exhibit(ex1)
    with pytest.raises(Exception):
        hall.add_exhibit(ex2)
