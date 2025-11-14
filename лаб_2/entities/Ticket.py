from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Exhibition import Exhibition
    from entities.Visitor import Visitor

class Ticket:
    def __init__(self, ticket_id: str, exhibition: "Exhibition", price: float, is_used: bool = False):
        self.ticket_id = ticket_id
        self.exhibition = exhibition
        self.price = price
        self.is_used = is_used

    def mark_used(self) -> None:
        self.is_used = True

    def is_valid(self) -> bool:
        return not self.is_used
