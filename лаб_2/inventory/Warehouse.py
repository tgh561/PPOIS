from __future__ import annotations
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from inventory.InventoryItem import InventoryItem
    from exceptions.StorageOverflow import StorageOverflow

class Warehouse:
    def __init__(self, location: str, capacity: int):
        self.location = location
        self.capacity = capacity
        self.items: List[InventoryItem] = []

    def store(self, item: InventoryItem) -> None:
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise StorageOverflow()

    def retrieve(self, item_id: str) -> Optional[InventoryItem]:
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                return item
        return None

    def is_full(self) -> bool:
        return len(self.items) >= self.capacity