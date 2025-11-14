from entities.Exhibit import Exhibit
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.RestorationRecord import RestorationRecord
    from entities.Artist import Artist


class Painting(Exhibit):
    def __init__(self, title: str, artist: "Artist", price: float = 0.0, year: int = None,
                 medium: str = "", dimensions: str = "", provenance: str = ""):
        super().__init__(title, artist)
        self.price = float(price)
        self.year = year
        self.medium = medium
        self.dimensions = dimensions
        self.provenance = provenance
        self.is_sold = False
        self.restoration_history: list["RestorationRecord"] = []

    def evaluate_price(self, factor: float = 1.0) -> float:
        base = self.price or 0.0
        age_bonus = 0
        if self.year:
            age = 2025 - self.year
            if age > 50:
                age_bonus = base * 0.2
        evaluated = (base + age_bonus) * factor
        return round(evaluated, 2)

    def mark_as_sold(self) -> None:
        if self.is_sold:
            raise Exception("PaintingAlreadySold")
        self.is_sold = True

    def add_provenance(self, note: str) -> None:
        self.provenance = (self.provenance + "; " + note).strip("; ")

    def add_restoration_record(self, record: "RestorationRecord") -> None:
        self.restoration_history.append(record)
