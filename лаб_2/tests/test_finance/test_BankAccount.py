# Тесты для класса BankAccount

import pytest
from finance.BankAccount import BankAccount

class DummyGallery: pass

def test_deposit_and_withdraw_and_transfer():
    g = DummyGallery()
    a = BankAccount("N1", 100.0, g)
    assert a.deposit(50) == 150.0
    assert a.withdraw(20) == 130.0
    b = BankAccount("N2", 10.0, g)
    assert a.transfer_to(b, 30) is True
    assert a.balance == 100.0 and b.balance == 40.0

def test_withdraw_raises_on_insufficient_balance():
    g = DummyGallery()
    a = BankAccount("N3", 5.0, g)
    with pytest.raises(Exception):
        a.withdraw(10)
