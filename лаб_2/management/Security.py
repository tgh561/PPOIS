from __future__ import annotations
from typing import TYPE_CHECKING

from Employee import Employee 

if TYPE_CHECKING:
    from entities.Ticket import Ticket

class Security(Employee):

    def __init__(self, name: str, position: str = "Security", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.checked_tickets: list["Ticket"] = []

    def check_ticket(self, ticket: "Ticket") -> bool:
        if ticket.is_used:
            return False
        self.checked_tickets.append(ticket)
        return True
