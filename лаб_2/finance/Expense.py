from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from management.Employee import Employee

class Expense:
    def __init__(self, expense_id: str, amount: float, description: str, employee: Employee):
        self.expense_id = expense_id
        self.amount = amount
        self.description = description
        self.employee = employee
        self.status = "pending"

    def approve(self) -> bool:
        if self.status == "pending":
            self.status = "approved"
            return True
        return False

    def reject(self) -> bool:
        if self.status == "pending":
            self.status = "rejected"
            return True
        return False
