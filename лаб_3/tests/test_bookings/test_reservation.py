"""Тесты для класса Reservation"""
import pytest
from datetime import datetime, timedelta
from Bookings.Reservation import Reservation
from Users.Turist import Turist
from Destinations.Hotel import Hotel


class TestReservation:
    """Тесты для класса Reservation"""
    
    @pytest.fixture
    def reservation(self):
        """Фикстура для создания резервации"""
        return Reservation(
            reservation_id="RES001",
            client_id="ivan@example.com",
            service_type="hotel",
            service_id="H001",
            reservation_date=datetime.now(),
            start_date=datetime.now() + timedelta(days=10),
            end_date=datetime.now() + timedelta(days=13),
            price=15000.0
        )
    
    def test_init(self, reservation):
        """Тест инициализации"""
        assert reservation.reservation_id == "RES001"
        assert reservation.client_id == "ivan@example.com"
        assert reservation.service_type == "hotel"
        assert reservation.service_id == "H001"
        assert reservation.price == 15000.0
        assert reservation.status == "active"
        assert isinstance(reservation.special_requests, list)
    
    def test_add_special_request(self, reservation):
        """Тест добавления специального запроса"""
        reservation.add_special_request("Поздний заезд")
        assert "Поздний заезд" in reservation.special_requests
        
        reservation.add_special_request("Детская кроватка")
        assert len(reservation.special_requests) == 2
    
    def test_add_special_request_duplicate(self, reservation):
        """Тест добавления дублирующегося запроса"""
        reservation.add_special_request("Запрос")
        reservation.add_special_request("Запрос")
        assert reservation.special_requests.count("Запрос") == 1
    
    def test_extend_reservation(self, reservation):
        """Тест продления резервации"""
        initial_end = reservation.end_date
        initial_price = reservation.price
        
        reservation.extend_reservation(2)
        assert reservation.end_date == initial_end + timedelta(days=2)
        assert reservation.price > initial_price
    
    def test_cancel_reservation(self, reservation):
        """Тест отмены резервации"""
        reservation.cancel_reservation()
        assert reservation.status == "cancelled"
    
    def test_calculate_duration(self, reservation):
        """Тест вычисления продолжительности в днях"""
        duration = reservation.calculate_duration()
        assert duration == 3
    
    def test_is_active_true(self, reservation):
        """Тест проверки активности - да"""
        reservation.status = "active"
        reservation.end_date = datetime.now() + timedelta(days=5)
        assert reservation.is_active() is True
    
    def test_is_active_false_cancelled(self, reservation):
        """Тест проверки активности - нет (отменено)"""
        reservation.status = "cancelled"
        assert reservation.is_active() is False
    
    def test_is_active_false_expired(self):
        """Тест проверки активности - нет (истекло)"""
        reservation = Reservation(
            reservation_id="RES002",
            client_id="test@example.com",
            service_type="hotel",
            service_id="H001",
            reservation_date=datetime.now() - timedelta(days=10),
            start_date=datetime.now() - timedelta(days=5),
            end_date=datetime.now() - timedelta(days=2),
            price=10000.0
        )
        assert reservation.is_active() is False
    
    def test_link_to_turist(self, reservation):
        """Тест связи с туристом (ассоциация)"""
        turist = Turist(
            name="Петр",
            surname="Петров",
            email="petr@example.com",
            phone="+1234567890",
            birth_date=datetime(1990, 1, 1),
            password="password",
            registration_date=datetime.now()
        )
        reservation.link_to_turist(turist)
        assert reservation.client_id == "petr@example.com"
    
    def test_assign_hotel_hotel_service(self, reservation):
        """Тест назначения отеля - тип hotel"""
        hotel = Hotel(
            hotel_id="H002",
            name="Test Hotel",
            location="Paris",
            stars=4,
            total_rooms=50,
            price_per_night=5000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
        reservation.assign_hotel(hotel)
        assert reservation.service_id == "H002"
    
    def test_assign_hotel_other_service(self, reservation):
        """Тест назначения отеля - другой тип"""
        reservation.service_type = "flight"
        hotel = Hotel(
            hotel_id="H002",
            name="Test Hotel",
            location="Paris",
            stars=4,
            total_rooms=50,
            price_per_night=5000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
        initial_id = reservation.service_id
        reservation.assign_hotel(hotel)
        assert reservation.service_id == initial_id



