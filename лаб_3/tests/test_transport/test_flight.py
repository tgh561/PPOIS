"""Тесты для класса Flight"""
import pytest
from datetime import datetime, timedelta
from Transport.Flight import Flight
from Bookings.Booking import Booking
from Tours.Tour import Tour
from Bookings.Reservation import Reservation


class TestFlight:
    """Тесты для класса Flight"""
    
    @pytest.fixture
    def flight(self):
        """Фикстура для создания рейса"""
        return Flight(
            flight_id="F001",
            airline="Aeroflot",
            flight_number="SU123",
            departure_airport="MOW",
            arrival_airport="CDG",
            departure_time=datetime(2024, 6, 1, 10, 0),
            arrival_time=datetime(2024, 6, 1, 14, 0),
            price=30000.0,
            available_seats=150
        )
    
    def test_init(self, flight):
        """Тест инициализации"""
        assert flight.flight_id == "F001"
        assert flight.airline == "Aeroflot"
        assert flight.flight_number == "SU123"
        assert flight.departure_airport == "MOW"
        assert flight.arrival_airport == "CDG"
        assert flight.price == 30000.0
        assert flight.available_seats == 150
        assert flight.total_seats == 150
        assert flight.booking_count == 0
        assert flight.baggage_allowance == 20.0
    
    def test_book_seat_success(self, flight):
        """Тест бронирования места - успех"""
        initial_available = flight.available_seats
        initial_bookings = flight.booking_count
        
        flight.book_seat()
        assert flight.available_seats == initial_available - 1
        assert flight.booking_count == initial_bookings + 1
    
    def test_book_seat_full(self):
        """Тест бронирования места - переполнен"""
        flight = Flight(
            flight_id="F002",
            airline="Test",
            flight_number="TT001",
            departure_airport="A",
            arrival_airport="B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=2),
            price=1000.0,
            available_seats=0
        )
        with pytest.raises(ValueError, match="Нет доступных мест"):
            flight.book_seat()
    
    def test_cancel_seat(self, flight):
        """Тест отмены места"""
        flight.book_seat()
        initial_available = flight.available_seats
        initial_bookings = flight.booking_count
        
        flight.cancel_seat()
        assert flight.available_seats == initial_available + 1
        assert flight.booking_count == initial_bookings - 1
    
    def test_cancel_seat_at_capacity(self, flight):
        """Тест отмены места при полной заполненности"""
        flight.cancel_seat()
        assert flight.available_seats <= flight.total_seats
    
    def test_calculate_duration(self, flight):
        """Тест вычисления продолжительности в часах"""
        duration = flight.calculate_duration()
        assert duration == 4
    
    def test_calculate_revenue(self, flight):
        """Тест вычисления выручки"""
        flight.book_seat()
        flight.book_seat()
        revenue = flight.calculate_revenue()
        assert revenue == 2 * 30000.0
    
    def test_is_full_true(self):
        """Тест проверки заполненности - да"""
        flight = Flight(
            flight_id="F003",
            airline="Test",
            flight_number="TT002",
            departure_airport="A",
            arrival_airport="B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=2),
            price=1000.0,
            available_seats=0
        )
        assert flight.is_full() is True
    
    def test_is_full_false(self, flight):
        """Тест проверки заполненности - нет"""
        assert flight.is_full() is False
    
    def test_get_seat_occupancy_rate(self, flight):
        """Тест получения процента занятости"""
        flight.book_seat()
        rate = flight.get_seat_occupancy_rate()
        expected = 1 / 150
        assert abs(rate - expected) < 0.01
    
    def test_link_to_booking(self, flight):
        """Тест связи с бронированием (ассоциация)"""
        booking = Booking(
            booking_id="B001",
            turist_id="test@example.com",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime.now() + timedelta(days=30),
            number_of_people=1,
            total_price=30000.0
        )
        initial_available = flight.available_seats
        flight.link_to_booking(booking)
        assert flight.available_seats == initial_available - 1
    
    def test_assign_to_tour(self, flight):
        """Тест назначения тура (ассоциация)"""
        tour = Tour(
            tour_id="T001",
            name="Test Tour",
            description="Description",
            destination="Paris",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 7),
            price=50000.0,
            max_participants=20
        )
        flight.assign_to_tour(tour)
        assert tour.flight_id == "F001"
    
    def test_link_to_reservation_flight_service(self, flight):
        """Тест связи с резервацией - тип flight"""
        reservation = Reservation(
            reservation_id="RES001",
            client_id="client@example.com",
            service_type="flight",
            service_id="F001",
            reservation_date=datetime.now(),
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=1),
            price=30000.0
        )
        initial_available = flight.available_seats
        flight.link_to_reservation(reservation)
        assert flight.available_seats == initial_available - 1
    
    def test_link_to_reservation_other_service(self, flight):
        """Тест связи с резервацией - другой тип"""
        reservation = Reservation(
            reservation_id="RES002",
            client_id="client@example.com",
            service_type="hotel",
            service_id="H001",
            reservation_date=datetime.now(),
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=3),
            price=50000.0
        )
        initial_available = flight.available_seats
        flight.link_to_reservation(reservation)
        assert flight.available_seats == initial_available



