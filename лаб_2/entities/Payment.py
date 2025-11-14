from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Visitor import Visitor
    from management.Cashier import Cashier


class Payment:
    def __init__(self, payment_id: str, amount: float, visitor: "Visitor", cashier: "Cashier", date: str, method: str = "card"):
        self.payment_id = payment_id
        self.amount = amount
        self.visitor = visitor
        self.cashier = cashier
        self.date = date
        self.method = method
        self.status = "pending"

    def process(self) -> bool:
        try:
            # объект cashier передаётся извне, метод вызывается на нём
            self.cashier.process_payment(self)
            self.status = "completed"
            return True
        except Exception:
            self.status = "failed"
            return False

    def cancel(self) -> bool:
        if self.status == "pending":
            self.status = "cancelled"
            return True
        return False

    def get_status(self) -> str:
        return self.status
