from __future__ import annotations
from typing import TYPE_CHECKING

from management.Employee import Employee

if TYPE_CHECKING:
    from entities.Exhibition import Exhibition

class Guide(Employee):

    def __init__(self, name: str, position: str = "Guide", salary: float = 0.0):
        super().__init__(name, position, salary)
        self.tours_assigned: list["Exhibition"] = []

    def assign_tour(self, exhibition: "Exhibition") -> None:
        if exhibition not in self.tours_assigned:
            self.tours_assigned.append(exhibition)

    def conduct_tour(self, exhibition: "Exhibition") -> str:
        if exhibition in self.tours_assigned:
            return f"{self.name} is conducting a tour for {exhibition.name}"
        return f"{self.name} is not assigned to {exhibition.name}"
