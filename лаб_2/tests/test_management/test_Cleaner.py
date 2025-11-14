# Тесты для класса Cleaner

from management.Cleaner import Cleaner

class DummyHall:
    def __init__(self, name):
        self.name = name

def test_assign_and_clean_hall():
    cleaner = Cleaner("Cli", salary=800.0)
    h = DummyHall("MainHall")
    cleaner.assign_hall(h)
    assert h in cleaner.assigned_halls
    msg = cleaner.clean_hall(h)
    assert "cleaned" in msg

def test_clean_not_assigned_returns_message():
    cleaner = Cleaner("Cli2")
    h2 = DummyHall("Other")
    msg = cleaner.clean_hall(h2)
    assert "not assigned" in msg
