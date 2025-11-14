from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Visitor import Visitor

class CreditCard:
    def __init__(self, number: str, holder: Visitor, limit: float, password: str):
        self.number = number
        self.holder = holder
        self.limit = limit
        self.password = password
        self.balance = 0.0

    def check_password(self, input_pass: str) -> bool:
        return self.password == input_pass

    def transfer_from(self, amount: float, to_card: CreditCard) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            to_card.balance += amount
            return True
        return False

    def validate(self) -> bool:
        return self.balance <= self.limit
