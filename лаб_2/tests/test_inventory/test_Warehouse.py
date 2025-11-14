# Тесты для класса Warehouse

import pytest
from inventory.Warehouse import Warehouse
from inventory.InventoryItem import InventoryItem

def test_store_and_retrieve_and_full():
    w = Warehouse("Main", capacity=2)
    item1 = InventoryItem("A1", "typeA", 1)
    item2 = InventoryItem("A2", "typeA", 2)
    w.store(item1)
    w.store(item2)
    assert w.is_full() is True
    # retrieval returns the item and removes it
    r = w.retrieve("A1")
    assert r is not None and r.item_id == "A1"
    assert w.is_full() is False

def test_store_overflow_raises(monkeypatch):
    w = Warehouse("W", capacity=1)
    item1 = InventoryItem("B1", "t", 1)
    item2 = InventoryItem("B2", "t", 1)
    w.store(item1)
    with pytest.raises(Exception):
        w.store(item2)
