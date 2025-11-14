# Тесты для класса Donor

from events.Donor import Donor

class DummyExhibit:
    def __init__(self, name): self.name = name

def test_add_donation_and_thank():
    d = Donor("Don")
    ex = DummyExhibit("Ex")
    d.add_donation(ex)
    assert ex in d.donations
    assert "Thank you Don" in d.thank()
