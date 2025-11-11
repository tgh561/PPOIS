from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Payment import Payment
    from management.Accountant import Accountant


class Transaction:
    def __init__(self, transaction_id: str, payment: Payment, accountant: Accountant, timestamp: str, description: str = "", amount: float = 0.0):
        self.transaction_id = transaction_id
        self.payment = payment
        self.accountant = accountant
        self.timestamp = timestamp
        self.description = description
        self.amount = amount

    def register(self) -> bool:
        if self.payment.status == "completed":
            try:
                self.accountant.register_transaction(self)
                return True
            except Exception:
                return False
        return False

    def get_details(self) -> str:
        return f"Transaction {self.transaction_id}: {self.description} (Amount: {self.amount}, Status: {self.payment.status})"
