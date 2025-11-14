from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from finance.Expense import Expense
    from entities.Gallery import Gallery
    from exceptions.BudgetExceeded import BudgetExceeded

class Budget:
    def __init__(self, year: int, total: float, gallery: Gallery):
        self.year = year
        self.total = total
        self.gallery = gallery
        self.expenses: List[Expense] = []
        self.remaining = total

    def add_expense(self, expense: Expense) -> None:
        if self.remaining >= expense.amount:
            self.expenses.append(expense)
            self.remaining -= expense.amount
        else:
            raise BudgetExceeded()

    def check_balance(self) -> float:
        return self.remaining

    def report(self) -> str:
        return f"Budget for {self.year}: remaining {self.remaining}"
