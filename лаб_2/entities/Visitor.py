from typing import List, Optional, TYPE_CHECKING
from entities.Ticket import Ticket

if TYPE_CHECKING:
    from entities.MemberCard import MemberCard
    from entities.Exhibition import Exhibition
    from entities.Payment import Payment

class Visitor:
    def __init__(self, name: str, email: str = "", phone: str = "", member_card: "MemberCard" = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.member_card: Optional["MemberCard"] = member_card
        self.visited_exhibitions: List["Exhibition"] = []

    def buy_ticket(self, exhibition: "Exhibition", payment: "Payment") -> "Ticket":
        ticket = Ticket(ticket_id=f"T-{id(self)}-{len(self.visited_exhibitions)}", exhibition=exhibition, price=exhibition.ticket_price)
        return ticket

    def visit_exhibition(self, exhibition: "Exhibition") -> None:
        if exhibition not in self.visited_exhibitions:
            self.visited_exhibitions.append(exhibition)

    def register_member_card(self, card: "MemberCard") -> None:
        self.member_card = card
