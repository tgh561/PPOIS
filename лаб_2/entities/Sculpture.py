from Exhibit import Exhibit
from Artist import Artist
from GalleryHall import GalleryHall
class Sculpture(Exhibit):
    def __init__(self, title: str, artist: "Artist", material: str = "", weight: float = 0.0, height: float = 0.0):
        super().__init__(title, artist)
        self.material = material
        self.weight = weight
        self.height = height
        self.is_installed = False

    def install(self, hall: "GalleryHall") -> None:
        self.is_installed = True
        self.assign_location(hall)

    def uninstall(self) -> None:
        self.is_installed = False
        self.location = None

    def estimate_insurance_value(self) -> float:
        return round(self.weight * 100 + self.height * 10, 2)
