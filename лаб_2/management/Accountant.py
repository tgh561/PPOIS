from __future__ import annotations
from typing import TYPE_CHECKING

from Employee import Employee  

if TYPE_CHECKING:
    from entities.Transaction import Transaction

class Accountant(Employee):
    def __init__(self, name: str, position: str = "Accountant", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.transactions_registered: list["Transaction"] = []

    def register_transaction(self, transaction: "Transaction") -> None:
        self.transactions_registered.append(transaction)