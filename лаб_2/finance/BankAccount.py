from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Gallery import Gallery
    from exceptions.BudgetExceeded import BudgetExceeded


class BankAccount:
    def __init__(self, number: str, balance: float, gallery: Gallery):
        self.number = number
        self.balance = balance
        self.gallery = gallery

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        raise BudgetExceeded()

    def transfer_to(self, other: BankAccount, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
            return True
        return False
