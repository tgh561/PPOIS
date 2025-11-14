from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Painting import Painting
    from management.Employee import Employee

class RestorationRecord:
    def __init__(self, painting: "Painting", restorer: "Employee", date: str, description: str = "", cost: float = 0.0):
        self.painting = painting
        self.restorer = restorer
        self.date = date
        self.description = description
        self.cost = cost
        self.status = "planned"

    def mark_completed(self) -> None:
        self.status = "completed"
        try:
            self.painting.add_restoration_record(self)
        except Exception:
            pass

    def summary(self) -> str:
        return f"Restoration of {self.painting.title} on {self.date}: {self.status} (cost: {self.cost})"
