# Тесты для класса Security

from management.Security import Security

class DummyTicket:
    def __init__(self, used=False):
        self.is_used = used

def test_check_ticket_true_and_false():
    sec = Security("S", salary=700.0)
    t1 = DummyTicket(False)
    t2 = DummyTicket(True)
    assert sec.check_ticket(t1) is True
    assert t1 in sec.checked_tickets
    assert sec.check_ticket(t2) is False
