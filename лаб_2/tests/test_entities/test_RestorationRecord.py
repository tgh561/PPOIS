# Тесты для класса RestorationRecord

from entities.RestorationRecord import RestorationRecord
from entities.Artist import Artist
from entities.Painting import Painting
from management.Employee import Employee

class DummyEmployee(Employee):
    def __init__(self): pass

def test_mark_completed_and_summary():
    artist = Artist("Моне", 1840)
    p = Painting("Кувшинки", artist)
    emp = DummyEmployee()
    r = RestorationRecord(p, emp, "2025-01-01", "Cleaning", 100.0)
    r.mark_completed()
    assert "completed" in r.summary()
    assert r in p.restoration_history
