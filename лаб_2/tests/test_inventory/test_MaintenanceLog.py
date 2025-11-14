# Тесты для класса MaintenanceLog

import pytest
from inventory.MaintenanceLog import MaintenanceLog

class DummyTech:
    def __init__(self, name="T"): self.name = name

def test_log_and_review():
    tech = DummyTech("Alex")
    log = MaintenanceLog("2025-01-01", tech)
    log.log("Checked motor")
    log.log("Replaced filter")
    res = log.review()
    assert "Checked motor" in res and "Replaced filter" in res
    assert "; " in res

def test_log_raises_on_invalid_date(monkeypatch):
    tech = DummyTech()
    # Создадим лог с пустой датой — код должен бросить InvalidDate
    log = MaintenanceLog("", tech)
    with pytest.raises(Exception):
        log.log("attempt")
