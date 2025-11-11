from __future__ import annotations

class BudgetExceeded(Exception):
    def __init__(self, message: str = "Budget exceeded"):
        super().__init__(message)