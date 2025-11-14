from typing import List, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Exhibit import Exhibit

class GalleryHall:
    def __init__(self, name: str, capacity: int = 50, floor: int = 1):
        self.name = name
        self.capacity = capacity
        self.floor = floor
        self.exhibits: List["Exhibit"] = []
        self.is_open = True

    def add_exhibit(self, exhibit: "Exhibit") -> None:
        if len(self.exhibits) >= self.capacity:
            raise Exception("ExhibitionFull")
        if exhibit not in self.exhibits:
            self.exhibits.append(exhibit)
            exhibit.assign_location(self)

    def remove_exhibit(self, exhibit: "Exhibit") -> None:
        if exhibit in self.exhibits:
            self.exhibits.remove(exhibit)
            exhibit.location = None

    def find_exhibit_by_title(self, title: str) -> Optional["Exhibit"]:
        for ex in self.exhibits:
            if ex.title == title:
                return ex
        return None

    def open_hall(self) -> None:
        self.is_open = True

    def close_hall(self) -> None:
        self.is_open = False
