# Тесты для класса Expense

from finance.Expense import Expense

class DummyEmployee: pass

def test_approve_and_reject_and_id_and_status():
    emp = DummyEmployee()
    ex = Expense("EX1", 25.0, "desc", emp)
    assert ex.status == "pending"
    assert ex.approve() is True
    assert ex.status == "approved"
    # approving again returns False
    assert ex.approve() is False
    # new expense reject from pending
    ex2 = Expense("EX2", 10.0, "d", emp)
    assert ex2.reject() is True
    assert ex2.status == "rejected"
