from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Exhibit import Exhibit
    from management.Employee import Employee


class Exhibition:
    def __init__(self, name: str, curator: "Employee", start_date: str = "", end_date: str = "", ticket_price: float = 0.0):
        self.name = name
        self.curator = curator
        self.exhibits: List["Exhibit"] = []
        self.start_date = start_date
        self.end_date = end_date
        self.ticket_price = ticket_price

    def add_exhibit_to_show(self, exhibit: "Exhibit") -> None:
        if exhibit not in self.exhibits:
            self.exhibits.append(exhibit)

    def remove_exhibit_from_show(self, exhibit: "Exhibit") -> None:
        if exhibit in self.exhibits:
            self.exhibits.remove(exhibit)

    def is_running(self, date: str) -> bool:
        if self.start_date and self.end_date:
            return self.start_date <= date <= self.end_date
        return False

    def total_items(self) -> int:
        return len(self.exhibits)
