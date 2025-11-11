from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..exceptions.StorageOverflow import StorageOverflow

class InventoryItem:
    def __init__(self, item_id: str, item_type: str, quantity: int):
        self.item_id = item_id
        self.item_type = item_type
        self.quantity = quantity

    def add_stock(self, amount: int) -> int:
        self.quantity += amount
        return self.quantity

    def remove_stock(self, amount: int) -> int:
        if self.quantity >= amount:
            self.quantity -= amount
            return self.quantity
        raise StorageOverflow()