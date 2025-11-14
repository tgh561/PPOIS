from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Gallery import Gallery

class Loan:
    def __init__(self, loan_id: str, amount: float, interest: float, gallery: Gallery):
        self.loan_id = loan_id
        self.amount = amount
        self.interest = interest
        self.gallery = gallery
        self.repaid = 0.0

    def repay(self, payment: float) -> float:
        self.repaid += payment
        return self.amount + self.amount * self.interest - self.repaid

    def is_fully_repaid(self) -> bool:
        return self.repaid >= self.amount + self.amount * self.interest
