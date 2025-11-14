# Тесты для класса Supplier

from inventory.Supplier import Supplier
from inventory.InventoryItem import InventoryItem

def test_order_and_deliver():
    s = Supplier("Acme")
    item = InventoryItem("SKU-1", "part", 3)
    s.order(item)
    assert item in s.products
    out = s.deliver()
    assert "Delivered by" in out and "Acme" in out
