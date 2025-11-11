from __future__ import annotations
from typing import TYPE_CHECKING

from Employee import Employee

if TYPE_CHECKING:
    from entities.Painting import Painting
    from entities.RestorationRecord import RestorationRecord


class Restorer(Employee):

    def __init__(self, name: str, position: str = "Restorer", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.completed_restorations: list[RestorationRecord] = []

    def restore_painting(self, painting: Painting, description: str, cost: float, date: str) -> RestorationRecord:
        record = RestorationRecord(painting, self, date, description, cost)
        record.mark_completed()
        self.completed_restorations.append(record)
        return record
