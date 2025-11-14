# Тесты для класса Painting

import pytest
from entities.Painting import Painting
from entities.Artist import Artist

def test_evaluate_price_and_provenance():
    artist = Artist("Моне", 1840)
    p = Painting("Кувшинки", artist, price=1000, year=1900)
    assert p.evaluate_price() >= 1000
    p.add_provenance("Museum")
    assert "Museum" in p.provenance

def test_mark_as_sold():
    artist = Artist("Моне", 1840)
    p = Painting("Кувшинки", artist)
    p.mark_as_sold()
    with pytest.raises(Exception):
        p.mark_as_sold()
