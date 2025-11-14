# Тесты для класса Loan
import pytest
from finance.Loan import Loan

class DummyGallery: pass

def test_repay_and_fully_repaid():
    g = DummyGallery()
    loan = Loan("L1", 100.0, 0.1, g)  # amount 100, interest 10%
    remaining = loan.repay(50.0)
    assert remaining == pytest.approx(100.0 + 10.0 - 50.0)
    assert loan.is_fully_repaid() is False
    loan.repay(60.0)
    assert loan.is_fully_repaid() is True
