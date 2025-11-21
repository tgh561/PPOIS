"""Тесты для класса Complaint"""
import pytest
from datetime import datetime, timedelta
from Support.Complaint import Complaint
from Users.Turist import Turist
from Bookings.Booking import Booking
from Users.Support import Support


class TestComplaint:
    """Тесты для класса Complaint"""
    
    @pytest.fixture
    def complaint(self):
        """Фикстура для создания жалобы"""
        return Complaint(
            complaint_id="COMP001",
            client_id="ivan@example.com",
            complaint_type="service",
            description="Плохое обслуживание",
            complaint_date=datetime.now(),
            priority="medium"
        )
    
    def test_init(self, complaint):
        """Тест инициализации"""
        assert complaint.complaint_id == "COMP001"
        assert complaint.client_id == "ivan@example.com"
        assert complaint.complaint_type == "service"
        assert complaint.description == "Плохое обслуживание"
        assert complaint.priority == "medium"
        assert complaint.status == "open"
        assert complaint.assigned_to is None
        assert complaint.resolution_date is None
        assert complaint.resolution_notes == ""
    
    def test_assign_to_staff(self, complaint):
        """Тест назначения сотрудника"""
        complaint.assign_to_staff("STAFF001")
        assert complaint.assigned_to == "STAFF001"
    
    def test_resolve(self, complaint):
        """Тест решения жалобы"""
        resolution_notes = "Проблема решена"
        complaint.resolve(resolution_notes)
        assert complaint.status == "resolved"
        assert complaint.resolution_notes == resolution_notes
        assert complaint.resolution_date is not None
    
    def test_escalate(self, complaint):
        """Тест эскалации жалобы"""
        complaint.escalate()
        assert complaint.priority == "high"
    
    def test_set_priority(self, complaint):
        """Тест установки приоритета"""
        complaint.set_priority("low")
        assert complaint.priority == "low"
        
        complaint.set_priority("urgent")
        assert complaint.priority == "urgent"
    
    def test_calculate_resolution_time_with_resolution(self, complaint):
        """Тест вычисления времени решения - есть решение"""
        complaint.resolution_date = datetime.now() + timedelta(days=3)
        resolution_time = complaint.calculate_resolution_time()
        assert resolution_time == 3
    
    def test_calculate_resolution_time_no_resolution(self, complaint):
        """Тест вычисления времени решения - нет решения"""
        resolution_time = complaint.calculate_resolution_time()
        assert resolution_time is None
    
    def test_is_resolved_true(self, complaint):
        """Тест проверки решения - да"""
        complaint.status = "resolved"
        assert complaint.is_resolved() is True
    
    def test_is_resolved_false(self, complaint):
        """Тест проверки решения - нет"""
        complaint.status = "open"
        assert complaint.is_resolved() is False
    
    def test_link_to_turist(self, complaint):
        """Тест связи с туристом (ассоциация)"""
        turist = Turist(
            name="Иван",
            surname="Иванов",
            email="petr@example.com",
            phone="+1234567890",
            birth_date=datetime(1990, 1, 1),
            password="password",
            registration_date=datetime.now()
        )
        complaint.link_to_turist(turist)
        assert complaint.client_id == "petr@example.com"
    
    def test_link_to_booking_same_client(self, complaint):
        """Тест связи с бронированием - тот же клиент"""
        booking = Booking(
            booking_id="B001",
            turist_id="ivan@example.com",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime.now() + timedelta(days=30),
            number_of_people=2,
            total_price=10000.0
        )
        complaint.link_to_booking(booking)
        assert complaint.booking_reference == "B001"
    
    def test_link_to_booking_different_client(self, complaint):
        """Тест связи с бронированием - другой клиент"""
        booking = Booking(
            booking_id="B001",
            turist_id="other@example.com",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime.now() + timedelta(days=30),
            number_of_people=2,
            total_price=10000.0
        )
        complaint.link_to_booking(booking)
        assert not hasattr(complaint, 'booking_reference') or getattr(complaint, 'booking_reference', None) != "B001"
    
    def test_assign_to_support_staff(self, complaint):
        """Тест назначения сотрудника поддержки (ассоциация)"""
        support = Support(
            name="Анна",
            surname="Петрова",
            employee_id="SUP001",
            shift="day",
            hire_date=datetime.now(),
            salary=50000.0,
            languages=["Русский", "Английский"]
        )
        complaint.assign_to_support_staff(support)
        assert complaint.assigned_to == "SUP001"



