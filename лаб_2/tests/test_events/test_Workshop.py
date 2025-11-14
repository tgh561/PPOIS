# Тесты для класса Workshop

from events.Workshop import Workshop

class DummyInstructor:
    def __init__(self, name="I"): self.name = name

class DummyGalleryHall:
    def __init__(self, name="H"): self.name = name

def test_start_and_end_and_materials():
    instr = DummyInstructor("Inst")
    hall = DummyGalleryHall()
    w = Workshop("W1", "2025-04-01", hall, instr)
    assert "started" in w.start()
    assert "ended" in w.end()
    w.materials.append("paper")
    assert "paper" in w.materials
