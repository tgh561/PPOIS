from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from management.Technician import Technician
    from exceptions.EmployeeNotAssigned import EmployeeNotAssigned

class Tool:
    def __init__(self, name: str, technician: Technician = None):
        self.name = name
        self.technician = technician
        self.status = "available"

    def assign(self, tech: Technician) -> None:
        if tech is None:
            raise EmployeeNotAssigned()
        self.technician = tech
        self.status = "assigned"

    def return_tool(self) -> None:
        self.technician = None
        self.status = "available"
