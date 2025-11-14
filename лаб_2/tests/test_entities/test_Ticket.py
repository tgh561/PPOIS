# Тесты для класса Ticket

from entities.Ticket import Ticket

class DummyExhibition:
    def __init__(self, name="Expo", ticket_price=10.0):
        self.name = name
        self.ticket_price = ticket_price

class DummyVisitor:
    def __init__(self, name="Mark"):
        self.name = name

def test_ticket_initial_state_and_validity():
    ex = DummyExhibition(ticket_price=15.0)
    v = DummyVisitor()
    t = Ticket(ticket_id="T1", exhibition=ex, price=ex.ticket_price)
    assert t.ticket_id == "T1"
    assert t.exhibition is ex
    assert t.price == 15.0
    assert t.is_valid() is True

def test_mark_used_changes_validity():
    ex = DummyExhibition()
    t = Ticket(ticket_id="T2", exhibition=ex, price=ex.ticket_price)
    t.mark_used()
    assert t.is_used is True
    assert t.is_valid() is False
