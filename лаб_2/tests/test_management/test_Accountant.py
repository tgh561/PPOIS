from management.Accountant import Accountant

class DummyTx:
    def __init__(self, tid):
        self.tid = tid

def test_register_transaction_appends():
    acc = Accountant("Ann", salary=2000.0)
    tx = DummyTx("TX1")
    acc.register_transaction(tx)
    assert tx in acc.transactions_registered
