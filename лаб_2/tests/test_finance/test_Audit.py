# Тесты для класса Audit

from finance.Audit import Audit

class DummyAccountant:
    pass

def test_audit_lifecycle():
    acc = DummyAccountant()
    audit = Audit("A1", acc)
    assert audit.status == "ongoing"
    audit.start_audit()
    assert audit.status == "started"
    audit.log_issue("issue1")
    audit.log_issue("issue2")
    res = audit.complete()
    assert "issue1" in res and "issue2" in res
    assert audit.status == "completed"
