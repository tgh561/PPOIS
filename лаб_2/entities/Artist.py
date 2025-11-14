from typing import List, Optional, TYPE_CHECKING
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.ArtStyle import ArtStyle
    from entities.Painting import Painting

class Artist:
    def __init__(self, name: str, birth_year: int, death_year: Optional[int] = None, bio: str = ""):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.bio = bio
        self.styles: List["ArtStyle"] = []
        self.paintings: List["Painting"] = []

    def add_style(self, style: "ArtStyle") -> None:
        if style not in self.styles:
            self.styles.append(style)

    def add_painting(self, painting: "Painting") -> None:
        if painting not in self.paintings:
            self.paintings.append(painting)

    def is_deceased(self) -> bool:
        return self.death_year is not None

    def summary(self) -> str:
        return f"{self.name} ({self.birth_year}{'–' + str(self.death_year) if self.death_year else ''})"
