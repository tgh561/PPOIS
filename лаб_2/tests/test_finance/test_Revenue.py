# Тесты для класса Revenue

from finance.Revenue import Revenue

def test_record_and_summarize():
    r = Revenue("tickets", 100.0, "2025-01-01")
    r.record(50.0)
    r.record(25.0)
    assert r.amount == 175.0
    assert r.summarize() == 175.0
