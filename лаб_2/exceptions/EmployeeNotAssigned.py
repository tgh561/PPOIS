from __future__ import annotations

class EmployeeNotAssigned(Exception):
    def __init__(self, message: str = "Employee not assigned"):
        super().__init__(message)