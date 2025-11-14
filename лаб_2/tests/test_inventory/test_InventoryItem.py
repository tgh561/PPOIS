# Тесты для класса InventoryItem

import pytest
from inventory.InventoryItem import InventoryItem

class DummyOverflow(Exception):
    pass

def test_add_and_remove_stock_normal():
    item = InventoryItem("I-1", "widget", 10)
    assert item.quantity == 10
    q = item.add_stock(5)
    assert q == 15 and item.quantity == 15
    q2 = item.remove_stock(4)
    assert q2 == 11 and item.quantity == 11

def test_remove_too_much_raises(monkeypatch):
    # если в твоём проекте StorageOverflow — конкретный класс, но тест проверяет поведение
    class FakeStorageOverflow(Exception):
        pass

    # подменяем исключение, если проект действительно импортирует exceptions.StorageOverflow,
    # то можно подменить в модуле; если нет — этот тест всё равно проверяет raise
    monkeypatch.setitem(__import__("sys").modules, 'exceptions.StorageOverflow', FakeStorageOverflow)
    item = InventoryItem("I-2", "gadget", 2)
    with pytest.raises(Exception):
        item.remove_stock(5)
