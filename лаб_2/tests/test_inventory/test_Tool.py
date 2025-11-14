# Тесты для класса Tool

import pytest
from inventory.Tool import Tool

class DummyTech:
    def __init__(self, name="Tech"): self.name = name

def test_assign_and_return(monkeypatch):
    t = Tool("Drill")
    tech = DummyTech("Bob")

    # если в проекте EmployeeNotAssigned — метод assign должен бросать при None
    with pytest.raises(Exception):
        t.assign(None)

    t.assign(tech)
    assert t.technician is tech
    assert t.status == "assigned"
    t.return_tool()
    assert t.technician is None
    assert t.status == "available"
