"""Тесты для класса Ticket (Documents)"""
import pytest
from datetime import datetime, timedelta
from Documents.Ticket import Ticket


class TestTicket:
    """Тесты для класса Ticket"""
    
    @pytest.fixture
    def ticket(self):
        """Фикстура для создания билета"""
        return Ticket(
            ticket_id="TIC001",
            ticket_type="event",
            holder_name="Иван Иванов",
            event_name="Концерт",
            venue="Концертный зал",
            event_date=datetime.now() + timedelta(days=10),
            price=3000.0,
            seat_number="A15"
        )
    
    def test_init(self, ticket):
        """Тест инициализации"""
        assert ticket.ticket_id == "TIC001"
        assert ticket.ticket_type == "event"
        assert ticket.holder_name == "Иван Иванов"
        assert ticket.event_name == "Концерт"
        assert ticket.venue == "Концертный зал"
        assert ticket.price == 3000.0
        assert ticket.seat_number == "A15"
        assert ticket.is_used is False
        assert ticket.qr_code is None
        assert isinstance(ticket.purchase_date, datetime)
    
    def test_validate_ticket_valid(self, ticket):
        """Тест валидации валидного билета"""
        result = ticket.validate_ticket()
        assert result is True
    
    def test_validate_ticket_used(self, ticket):
        """Тест валидации использованного билета"""
        ticket.is_used = True
        result = ticket.validate_ticket()
        assert result is False
    
    def test_validate_ticket_expired(self):
        """Тест валидации просроченного билета"""
        ticket = Ticket(
            ticket_id="TIC002",
            ticket_type="event",
            holder_name="Test",
            event_name="Past Event",
            venue="Venue",
            event_date=datetime.now() - timedelta(days=1),
            price=2000.0
        )
        result = ticket.validate_ticket()
        assert result is False
    
    def test_use_ticket_success(self, ticket):
        """Тест успешного использования билета"""
        ticket.use_ticket()
        assert ticket.is_used is True
    
    def test_use_ticket_invalid(self):
        """Тест использования невалидного билета"""
        ticket = Ticket(
            ticket_id="TIC003",
            ticket_type="event",
            holder_name="Test",
            event_name="Past Event",
            venue="Venue",
            event_date=datetime.now() - timedelta(days=1),
            price=2000.0
        )
        with pytest.raises(ValueError, match="Билет недействителен"):
            ticket.use_ticket()
    
    def test_set_qr_code(self, ticket):
        """Тест установки QR-кода"""
        qr_code = "QR123456789"
        ticket.set_qr_code(qr_code)
        assert ticket.qr_code == qr_code
    
    def test_calculate_days_until_event(self, ticket):
        """Тест вычисления дней до события"""
        days = ticket.calculate_days_until_event()
        assert isinstance(days, int)
        assert days >= 0
    
    def test_is_expired_false(self, ticket):
        """Тест проверки истечения - нет"""
        assert ticket.is_expired() is False
    
    def test_is_expired_true(self):
        """Тест проверки истечения - да"""
        ticket = Ticket(
            ticket_id="TIC004",
            ticket_type="event",
            holder_name="Test",
            event_name="Past Event",
            venue="Venue",
            event_date=datetime.now() - timedelta(days=1),
            price=2000.0
        )
        assert ticket.is_expired() is True
    
    def test_get_ticket_info(self, ticket):
        """Тест получения информации о билете"""
        info = ticket.get_ticket_info()
        assert "TIC001" in info
        assert "Концерт" in info
        assert "Концертный зал" in info



