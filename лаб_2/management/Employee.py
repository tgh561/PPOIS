from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.GalleryHall import GalleryHall

class Employee:

    def __init__(self, name: str, position: str, salary: float = 0.0, employee_id: str = None):
        self.name: str = name
        self.position: str = position
        self.salary: float = salary
        self.employee_id: str = employee_id or f"E-{id(self)}"
        self.assigned_hall: Optional["GalleryHall"] = None

    def assign_to_hall(self, hall: "GalleryHall") -> None:
        self.assigned_hall = hall

    def promote(self, new_position: str, new_salary: float = None) -> None:
        self.position = new_position
        if new_salary:
            self.salary = new_salary

    def get_info(self) -> str:
        return f"{self.name} ({self.position}), salary: {self.salary}"
