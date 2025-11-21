"""Тесты для класса Ticket (Support)"""
import pytest
from datetime import datetime, timedelta
from Support.Ticket import Ticket


class TestTicket:
    """Тесты для класса Ticket"""
    
    @pytest.fixture
    def ticket(self):
        """Фикстура для создания тикета"""
        return Ticket(
            ticket_id="TICK001",
            client_id="ivan@example.com",
            subject="Проблема с бронированием",
            description="Не могу забронировать тур",
            ticket_date=datetime.now(),
            category="booking",
            priority="medium"
        )
    
    def test_init(self, ticket):
        """Тест инициализации"""
        assert ticket.ticket_id == "TICK001"
        assert ticket.client_id == "ivan@example.com"
        assert ticket.subject == "Проблема с бронированием"
        assert ticket.description == "Не могу забронировать тур"
        assert ticket.category == "booking"
        assert ticket.priority == "medium"
        assert ticket.status == "open"
        assert ticket.assigned_to is None
        assert ticket.resolution_date is None
        assert isinstance(ticket.messages, list)
        assert ticket.satisfaction_rating is None
    
    def test_assign_to_support(self, ticket):
        """Тест назначения сотрудника поддержки"""
        ticket.assign_to_support("SUP001")
        assert ticket.assigned_to == "SUP001"
    
    def test_add_message(self, ticket):
        """Тест добавления сообщения"""
        ticket.add_message("Привет, могу помочь", "CLIENT001", False)
        assert len(ticket.messages) == 1
        assert ticket.messages[0]["text"] == "Привет, могу помочь"
        assert ticket.messages[0]["sender_id"] == "CLIENT001"
        assert ticket.messages[0]["is_staff"] is False
    
    def test_add_message_staff(self, ticket):
        """Тест добавления сообщения от сотрудника"""
        ticket.add_message("Мы решим проблему", "STAFF001", True)
        assert ticket.messages[0]["is_staff"] is True
    
    def test_resolve_ticket(self, ticket):
        """Тест решения тикета"""
        ticket.assigned_to = "SUP001"
        resolution_notes = "Проблема решена"
        ticket.resolve_ticket(resolution_notes)
        assert ticket.status == "resolved"
        assert ticket.resolution_date is not None
        assert len(ticket.messages) == 1
        assert ticket.messages[0]["is_staff"] is True
    
    def test_close_ticket(self, ticket):
        """Тест закрытия тикета"""
        ticket.close_ticket()
        assert ticket.status == "closed"
    
    def test_set_satisfaction_rating_valid(self, ticket):
        """Тест установки валидного рейтинга"""
        ticket.set_satisfaction_rating(4.5)
        assert ticket.satisfaction_rating == 4.5
        
        ticket.set_satisfaction_rating(5.0)
        assert ticket.satisfaction_rating == 5.0
    
    def test_set_satisfaction_rating_invalid_low(self, ticket):
        """Тест установки слишком низкого рейтинга"""
        with pytest.raises(ValueError, match="Рейтинг должен быть от 1 до 5"):
            ticket.set_satisfaction_rating(0.5)
    
    def test_set_satisfaction_rating_invalid_high(self, ticket):
        """Тест установки слишком высокого рейтинга"""
        with pytest.raises(ValueError, match="Рейтинг должен быть от 1 до 5"):
            ticket.set_satisfaction_rating(6.0)
    
    def test_calculate_resolution_time_with_resolution(self, ticket):
        """Тест вычисления времени решения - есть решение"""
        ticket.resolution_date = datetime.now() + timedelta(days=3)
        resolution_time = ticket.calculate_resolution_time()
        assert resolution_time == 3
    
    def test_calculate_resolution_time_no_resolution(self, ticket):
        """Тест вычисления времени решения - нет решения"""
        resolution_time = ticket.calculate_resolution_time()
        assert resolution_time is None
    
    def test_escalate_priority_low(self, ticket):
        """Тест повышения приоритета с low"""
        ticket.priority = "low"
        ticket.escalate_priority()
        assert ticket.priority == "medium"
    
    def test_escalate_priority_medium(self, ticket):
        """Тест повышения приоритета с medium"""
        ticket.escalate_priority()
        assert ticket.priority == "high"
    
    def test_escalate_priority_high(self, ticket):
        """Тест повышения приоритета с high"""
        ticket.priority = "high"
        ticket.escalate_priority()
        assert ticket.priority == "urgent"
    
    def test_escalate_priority_urgent(self, ticket):
        """Тест повышения приоритета с urgent (максимум)"""
        ticket.priority = "urgent"
        ticket.escalate_priority()
        assert ticket.priority == "urgent"  # Не может быть выше
    
    def test_is_resolved_true_resolved(self, ticket):
        """Тест проверки решения - resolved"""
        ticket.status = "resolved"
        assert ticket.is_resolved() is True
    
    def test_is_resolved_true_closed(self, ticket):
        """Тест проверки решения - closed"""
        ticket.status = "closed"
        assert ticket.is_resolved() is True
    
    def test_is_resolved_false(self, ticket):
        """Тест проверки решения - нет"""
        ticket.status = "open"
        assert ticket.is_resolved() is False



