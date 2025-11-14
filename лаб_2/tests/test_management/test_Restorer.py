from management.Restorer import Restorer

class DummyPainting:
    def __init__(self, title):
        self.title = title
        self.restoration_history = []

class DummyRestorationRecord:
    def __init__(self, painting, restorer, date, desc, cost):
        self.painting = painting
        self.restorer = restorer
        self.date = date
        self.desc = desc
        self.cost = cost
    def mark_completed(self):
        pass

def test_restore_painting_monkeypatch(monkeypatch):
    restorer = Restorer("R", salary=1100.0)
    painting = DummyPainting("P1")

    def fake_Record(painting_arg, restorer_arg, date_arg, desc_arg, cost_arg):
        rec = DummyRestorationRecord(painting_arg, restorer_arg, date_arg, desc_arg, cost_arg)
        painting.restoration_history.append(rec)
        return rec

    import management.Restorer as mod
    # allow creating the attribute if it's missing in the module
    monkeypatch.setattr(mod, "RestorationRecord", fake_Record, raising=False)

    rec = restorer.restore_painting(painting, "clean", 100.0, "2025-01-01")
    assert rec in painting.restoration_history
    assert rec in restorer.completed_restorations
