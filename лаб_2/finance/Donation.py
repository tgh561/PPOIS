from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..entities.Visitor import Visitor
    from ..entities.Exhibit import Exhibit

class Donation:
    def __init__(self, donation_id: str, amount: float, donor: Visitor, exhibit: Exhibit = None):
        self.donation_id = donation_id
        self.amount = amount
        self.donor = donor
        self.exhibit = exhibit

    def process_donation(self) -> bool:
        return True

    def acknowledge(self) -> str:
        return f"Thank you {self.donor.name} for donation"
