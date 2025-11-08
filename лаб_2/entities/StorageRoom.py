from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Exhibit import Exhibit

class StorageRoom:
    def __init__(self, capacity: int = 100, climate_control: bool = True):
        self.capacity = capacity
        self.climate_control = climate_control
        self.current_items: List["Exhibit"] = []

    def store_exhibit(self, exhibit: "Exhibit") -> None:
        if len(self.current_items) >= self.capacity:
            raise Exception("StorageOverflow")
        if exhibit not in self.current_items:
            self.current_items.append(exhibit)
            exhibit.assign_location(self)

    def remove_exhibit(self, exhibit: "Exhibit") -> None:
        if exhibit in self.current_items:
            self.current_items.remove(exhibit)
            exhibit.location = None

    def is_full(self) -> bool:
        return len(self.current_items) >= self.capacity
