# Тесты для класса Budget

import pytest
from finance.Budget import Budget

class DummyGallery: pass

class DummyExpense:
    def __init__(self, amount):
        self.amount = amount

def test_add_expense_and_remaining_and_report():
    g = DummyGallery()
    b = Budget(2025, 100.0, g)
    e1 = DummyExpense(30.0)
    b.add_expense(e1)
    assert b.check_balance() == 70.0
    assert "Budget for 2025" in b.report()

def test_add_expense_raises_when_exceeds():
    g = DummyGallery()
    b = Budget(2025, 50.0, g)
    e_big = DummyExpense(100.0)
    with pytest.raises(Exception):
        b.add_expense(e_big)
