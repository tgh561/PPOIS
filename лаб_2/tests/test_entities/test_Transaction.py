# Тесты для класса Transaction

from entities.Transaction import Transaction

class DummyPayment:
    def __init__(self, status="pending"):
        self.status = status

class DummyAccountant:
    def __init__(self, should_raise=False):
        self.records = []
        self.should_raise = should_raise
    def register_transaction(self, tx):
        if self.should_raise:
            raise RuntimeError("db error")
        self.records.append(tx)

def test_register_success_when_payment_completed():
    payment = DummyPayment(status="completed")
    accountant = DummyAccountant()
    tx = Transaction(
        transaction_id="TX1",
        payment=payment,
        accountant=accountant,
        timestamp="2025-01-01 12:00",
        description="Ticket sale",
        amount=20.0,
    )
    assert tx.register() is True
    assert accountant.records[-1] is tx

def test_register_fail_on_accountant_error():
    payment = DummyPayment(status="completed")
    accountant = DummyAccountant(should_raise=True)
    tx = Transaction("TX2", payment, accountant, "2025-01-02 10:00", "Sale", 30.0)
    assert tx.register() is False

def test_register_returns_false_if_payment_not_completed():
    payment = DummyPayment(status="pending")
    accountant = DummyAccountant()
    tx = Transaction("TX3", payment, accountant, "2025-01-03 09:00", "Sale", 40.0)
    assert tx.register() is False
    assert len(accountant.records) == 0

def test_get_details_contains_core_fields():
    payment = DummyPayment(status="completed")
    accountant = DummyAccountant()
    tx = Transaction("TX4", payment, accountant, "2025-01-04 08:00", "Desc", 50.0)
    details = tx.get_details()
    assert "TX4" in details
    assert "Desc" in details
    assert "Amount: 50.0" in details
    assert "completed" in details
