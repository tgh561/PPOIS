# Тесты для класса Sponsor

from events.Sponsor import Sponsor

class DummyEvent:
    pass

def test_donate_and_perks():
    ev = DummyEvent()
    s = Sponsor("S", 1000.0, ev)
    s.donate(500)
    assert s.contribution == 1500.0
    assert "VIP" in s.get_perks()
