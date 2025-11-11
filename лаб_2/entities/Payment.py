from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from Visitor import Visitor 
if TYPE_CHECKING:
    from management.Cashier import Cashier


class Payment:
    def __init__(self, payment_id: str, amount: float, visitor: Visitor, cashier: Cashier, date: str, method: str = "card"):
        self.payment_id = payment_id
        self.amount = amount
        self.visitor = visitor
        self.cashier = cashier
        self.date = date
        self.status = "pending"
        self.method = method

    def process(self) -> bool:
        if self.status == "pending":
            self.status = "completed"
            try:
                self.cashier.process_payment(self)
            except Exception:
                self.status = "failed"
                return False
            return True
        return False

    def cancel(self) -> bool:
        if self.status == "pending":
            self.status = "cancelled"
            return True
        return False

    def get_status(self) -> str:
        return self.status
