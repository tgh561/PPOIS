from __future__ import annotations
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from ..entities.Visitor import Visitor
    from ..entities.Gallery import Gallery

class Invoice:
    def __init__(self, invoice_id: str, amount: float, visitor: Visitor, gallery: Gallery, date: str, status: str = "unpaid"):
        self.invoice_id = invoice_id
        self.amount = amount
        self.visitor = visitor
        self.gallery = gallery
        self.date = date
        self.status = status

    def generate(self) -> str:
        return f"Invoice {self.invoice_id} generated for {self.amount}"

    def pay(self, payment_method: str) -> bool:
        if self.status == "unpaid":
            self.status = "paid"
            return True
        return False

    def cancel(self) -> bool:
        if self.status == "unpaid":
            self.status = "cancelled"
            return True
        return False
