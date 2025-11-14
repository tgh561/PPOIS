# Тесты для класса Exhibition

from entities.Exhibition import Exhibition

class DummyEmployee:
    def __init__(self, name):
        self.name = name

class DummyExhibit:
    def __init__(self, title):
        self.title = title
    def __eq__(self, other):
        return isinstance(other, DummyExhibit) and self.title == other.title

def test_add_and_remove_exhibit():
    curator = DummyEmployee("Anna")
    ex = Exhibition(name="Modern Art", curator=curator)
    e1 = DummyExhibit("A")
    e2 = DummyExhibit("B")
    ex.add_exhibit_to_show(e1)
    ex.add_exhibit_to_show(e2)
    assert ex.total_items() == 2
    ex.remove_exhibit_from_show(e1)
    assert ex.total_items() == 1

def test_is_running_true():
    curator = DummyEmployee("C")
    ex = Exhibition("Test", curator, start_date="2023-01-01", end_date="2023-12-31")
    assert ex.is_running("2023-06-01")

def test_is_running_false():
    curator = DummyEmployee("C")
    ex = Exhibition("Test", curator, start_date="2023-01-01", end_date="2023-12-31")
    assert not ex.is_running("2024-01-01")
