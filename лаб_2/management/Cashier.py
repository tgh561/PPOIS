from typing import TYPE_CHECKING

from management.Employee import Employee

if TYPE_CHECKING:
    from entities.Payment import Payment


class Cashier(Employee):
    def __init__(self, name: str, position: str = "Cashier", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.processed_payments: list["Payment"] = []

    def process_payment(self, payment: "Payment") -> bool:
        self.processed_payments.append(payment)
        return True
