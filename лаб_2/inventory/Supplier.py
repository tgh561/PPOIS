from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from inventory.InventoryItem import InventoryItem

class Supplier:
    def __init__(self, name: str):
        self.name = name
        self.products: List[InventoryItem] = []

    def order(self, item: InventoryItem) -> None:
        self.products.append(item)

    def deliver(self) -> str:
        return f"Delivered by {self.name}"