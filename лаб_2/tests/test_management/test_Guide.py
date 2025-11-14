# Тесты для класса Guide

from management.Guide import Guide

class DummyEx:
    def __init__(self, name):
        self.name = name

def test_assign_and_conduct_tour():
    guide = Guide("G", salary=900.0)
    ex = DummyEx("Expo")
    guide.assign_tour(ex)
    assert ex in guide.tours_assigned
    msg = guide.conduct_tour(ex)
    assert "conducting a tour" in msg
    # not assigned case
    other = DummyEx("X")
    msg2 = guide.conduct_tour(other)
    assert "not assigned" in msg2
