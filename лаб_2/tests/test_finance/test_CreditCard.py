# Тесты для класса CreditCard

from finance.CreditCard import CreditCard

class DummyVisitor:
    def __init__(self, name="Don"): self.name = name

def test_password_check_and_transfer_and_validate():
    v = DummyVisitor()
    c1 = CreditCard("1111", v, limit=100.0, password="p")
    c2 = CreditCard("2222", v, limit=50.0, password="q")
    c1.balance = 80.0
    assert c1.check_password("p") is True
    assert c1.transfer_from(30.0, c2) is True
    assert c1.balance == 50.0 and c2.balance == 30.0
    assert c1.validate() is True
    # transfer too big
    assert c1.transfer_from(100.0, c2) is False
