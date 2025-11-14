from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Visitor import Visitor

class MemberCard:
    def __init__(self, card_id: str, visitor: "Visitor", discount_rate: float = 0.1, points: int = 0):
        self.card_id = card_id
        self.visitor = visitor
        self.discount_rate = discount_rate
        self.points = points

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.discount_rate)

    def add_points(self, amount: int) -> None:
        self.points += amount

    def redeem_points(self, amount: int) -> bool:
        if self.points >= amount:
            self.points -= amount
            return True
        return False
