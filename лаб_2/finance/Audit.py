from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from management.Accountant import Accountant

class Audit:
    def __init__(self, audit_id: str, accountant: Accountant):
        self.audit_id = audit_id
        self.accountant = accountant
        self.results: List[str] = []
        self.status = "ongoing"

    def start_audit(self) -> None:
        self.status = "started"

    def log_issue(self, issue: str) -> None:
        self.results.append(issue)

    def complete(self) -> str:
        self.status = "completed"
        return "; ".join(self.results)
