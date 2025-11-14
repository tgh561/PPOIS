# Тесты для класса Curator

from management.Curator import Curator

class DummyEx:
    def __init__(self, name):
        self.name = name

def test_add_and_list_exhibitions():
    curator = Curator("Cur", salary=1500.0)
    ex1 = DummyEx("Expo1")
    ex2 = DummyEx("Expo2")
    curator.add_exhibition(ex1)
    curator.add_exhibition(ex2)
    curator.add_exhibition(ex1)  # duplicate ignored
    names = curator.list_exhibitions()
    assert "Expo1" in names and "Expo2" in names
    assert len(names) == 2
