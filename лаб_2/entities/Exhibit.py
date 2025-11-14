from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Artist import Artist
    from entities.GalleryHall import GalleryHall


class Exhibit:
    def __init__(self, title: str, artist: "Artist", accession_id: str = "", description: str = ""):
        self.title = title
        self.artist = artist
        self.accession_id = accession_id or f"ACC-{id(self)}"
        self.description = description
        self.location: Optional["GalleryHall"] = None

        try:
            artist.add_painting(self)
        except Exception:
            pass

    def assign_location(self, location: "GalleryHall") -> None:
        self.location = location

    def basic_info(self) -> str:
        return f"{self.title} by {self.artist.name} ({self.accession_id})"
