# Тесты для класса Cashier

from management.Cashier import Cashier

class DummyPayment:
    def __init__(self, pid):
        self.pid = pid

def test_process_payment_records_and_returns_true():
    cashier = Cashier("Bob", salary=1200.0)
    p = DummyPayment("P1")
    res = cashier.process_payment(p)
    assert res is True
    assert p in cashier.processed_payments
