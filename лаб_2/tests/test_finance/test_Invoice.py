# Тесты для класса Invoice

from finance.Invoice import Invoice

class DummyVisitor:
    def __init__(self, name): self.name = name

class DummyGallery:
    def __init__(self, name): self.name = name

def test_generate_pay_cancel_flow():
    v = DummyVisitor("Max")
    g = DummyGallery("Main")
    inv = Invoice("INV1", 50.0, v, g, "2025-01-01")
    assert "INV1" in inv.generate()
    assert inv.pay("card") is True
    assert inv.status == "paid"
    # cannot cancel after paid
    assert inv.cancel() is False
    # new invoice can be cancelled
    inv2 = Invoice("INV2", 10.0, v, g, "2025-01-02")
    assert inv2.cancel() is True
    assert inv2.status == "cancelled"
