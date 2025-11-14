# Тесты для класса Tour

from events.Tour import Tour

class DummyGuide:
    def __init__(self, name="G"): self.name = name

class DummyGalleryHall:
    def __init__(self, name="H"): self.name = name

class DummyExhibit:
    def __init__(self, name): self.name = name

def test_conduct_and_feedback_and_exhibits():
    guide = DummyGuide("Gina")
    hall = DummyGalleryHall()
    t = Tour("T1", "2025-03-01", hall, guide)
    assert "conducted" in t.conduct()
    ex = DummyExhibit("Ex")
    t.exhibits.append(ex)
    # feedback just shouldn't raise
    t.feedback(5)
