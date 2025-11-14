# Тесты для класса Payment

from entities.Payment import Payment
from entities.Visitor import Visitor

class DummyCashier:
    def process_payment(self, payment): return True

def test_process_and_cancel():
    v = Visitor("Иван")
    cashier = DummyCashier()
    p = Payment("P1", 100, v, cashier, "2025-01-01")
    assert p.process()
    assert p.get_status() == "completed"
    p2 = Payment("P2", 50, v, cashier, "2025-01-01")
    assert p2.cancel()
    assert p2.get_status() == "cancelled"
