# Тесты для класса Visitor

from entities.Visitor import Visitor
from entities.Ticket import Ticket

class DummyExhibition:
    def __init__(self, name="Expo", ticket_price=12.5):
        self.name = name
        self.ticket_price = ticket_price

class DummyPayment:
    def __init__(self, status="completed"):
        self.status = status

class DummyMemberCard:
    def __init__(self, card_id="C1"):
        self.card_id = card_id

def test_buy_ticket_creates_ticket_with_price():
    v = Visitor("Марк")
    ex = DummyExhibition(ticket_price=20.0)
    pay = DummyPayment(status="completed")
    t = v.buy_ticket(exhibition=ex, payment=pay)
    assert isinstance(t, Ticket)
    assert t.price == 20.0
    # ticket_id формируется детерминированно по длине посещений
    assert t.ticket_id.startswith("T-")

def test_visit_exhibition_adds_once():
    v = Visitor("Марк")
    ex = DummyExhibition(name="A")
    v.visit_exhibition(ex)
    v.visit_exhibition(ex)  # повторный визит не добавляет
    assert len(v.visited_exhibitions) == 1
    assert v.visited_exhibitions[0] is ex

def test_register_member_card_sets_card():
    v = Visitor("Марк")
    card = DummyMemberCard("CARD-42")
    v.register_member_card(card)
    assert v.member_card is card
