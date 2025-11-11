from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..management.Director import Director

class FinancialReport:
    def __init__(self, period: str, data: str):
        self.period = period
        self.data = data

    def generate_pdf(self) -> str:
        return f"PDF generated for {self.period}"

    def send_to_director(self, director: Director) -> bool:
        return True
