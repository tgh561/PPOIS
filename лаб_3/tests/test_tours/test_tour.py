"""Тесты для класса Tour"""
import pytest
from datetime import datetime, timedelta
from Tours.Tour import Tour
from Destinations.Destination import Destination
from Users.Guide import Guide
from Bookings.Booking import Booking
from Transport.Flight import Flight
from Destinations.Hotel import Hotel
from Exceptions.TourFullException import TourFullException


class TestTour:
    """Тесты для класса Tour"""
    
    @pytest.fixture
    def tour(self):
        """Фикстура для создания тура"""
        return Tour(
            tour_id="T001",
            name="Отдых в Париже",
            description="Прекрасный отдых в Париже",
            destination="Париж",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 7),
            price=50000.0,
            max_participants=20
        )
    
    def test_init(self, tour):
        """Тест инициализации"""
        assert tour.tour_id == "T001"
        assert tour.name == "Отдых в Париже"
        assert tour.description == "Прекрасный отдых в Париже"
        assert tour.destination == "Париж"
        assert tour.price == 50000.0
        assert tour.max_participants == 20
        assert tour.current_participants == 0
        assert tour.duration_days == 6
        assert tour.is_active is True
        assert tour.rating == 0.0
        assert isinstance(tour.bookings, list)
    
    def test_check_availability_success(self, tour):
        """Тест проверки доступности - успех"""
        result = tour.check_availability()
        assert result is True
    
    def test_check_availability_full(self, tour):
        """Тест проверки доступности - переполнен"""
        tour.current_participants = 20
        with pytest.raises(TourFullException):
            tour.check_availability()
    
    def test_add_participant_success(self, tour):
        """Тест добавления участника - успех"""
        initial_count = tour.current_participants
        tour.add_participant()
        assert tour.current_participants == initial_count + 1
    
    def test_add_participant_full(self, tour):
        """Тест добавления участника - переполнен"""
        tour.current_participants = 20
        with pytest.raises(TourFullException):
            tour.add_participant()
    
    def test_remove_participant_success(self, tour):
        """Тест удаления участника - успех"""
        tour.current_participants = 5
        tour.remove_participant()
        assert tour.current_participants == 4
    
    def test_remove_participant_zero(self, tour):
        """Тест удаления участника при нуле"""
        tour.current_participants = 0
        tour.remove_participant()
        assert tour.current_participants == 0
    
    def test_calculate_total_revenue(self, tour):
        """Тест вычисления общей выручки"""
        tour.current_participants = 10
        revenue = tour.calculate_total_revenue()
        assert revenue == 10 * 50000.0
    
    def test_get_available_spots(self, tour):
        """Тест получения доступных мест"""
        tour.current_participants = 5
        available = tour.get_available_spots()
        assert available == 15
    
    def test_update_rating(self, tour):
        """Тест обновления рейтинга"""
        tour.rating = 4.0
        tour.update_rating(5.0)
        assert tour.rating == 4.5
        
        tour.update_rating(3.0)
        assert tour.rating == 3.75
    
    def test_assign_destination(self, tour):
        """Тест назначения направления (ассоциация)"""
        destination = Destination(
            destination_id="D001",
            name="Париж",
            country="Франция",
            city="Париж",
            description="Красивый город",
            climate="Умеренный",
            currency="EUR",
            visa_required=False
        )
        tour.assign_destination(destination)
        assert tour.destination == "Париж"
    
    def test_assign_guide(self, tour):
        """Тест назначения гида (ассоциация)"""
        guide = Guide(
            name="Иван",
            surname="Иванов",
            guide_id="G001",
            languages=["Русский", "Французский"],
            certification_date=datetime(2020, 1, 1),
            rating=4.5,
            hourly_rate=1000.0
        )
        tour.assign_guide(guide)
        assert tour.guide_id == "G001"
    
    def test_link_to_booking_same_tour(self, tour):
        """Тест связи с бронированием - тот же тур"""
        booking = Booking(
            booking_id="B001",
            turist_id="ivan@example.com",
            tour_id="T001",
            booking_date=datetime.now(),
            travel_date=datetime(2024, 6, 1),
            number_of_people=1,
            total_price=50000.0
        )
        initial_participants = tour.current_participants
        tour.link_to_booking(booking)
        assert tour.current_participants == initial_participants + 1
    
    def test_link_to_booking_different_tour(self, tour):
        """Тест связи с бронированием - другой тур"""
        booking = Booking(
            booking_id="B001",
            turist_id="ivan@example.com",
            tour_id="T002",
            booking_date=datetime.now(),
            travel_date=datetime(2024, 6, 1),
            number_of_people=1,
            total_price=50000.0
        )
        initial_participants = tour.current_participants
        tour.link_to_booking(booking)
        assert tour.current_participants == initial_participants
    
    def test_assign_flight(self, tour):
        """Тест назначения рейса (ассоциация)"""
        flight = Flight(
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
        tour.assign_flight(flight)
        assert tour.flight_id == "F001"
    
    def test_assign_hotel(self, tour):
        """Тест назначения отеля (ассоциация)"""
        hotel = Hotel(
            hotel_id="H001",
            name="Hotel Paris",
            location="Париж",
            stars=4,
            total_rooms=50,
            price_per_night=5000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
        tour.assign_hotel(hotel)
        assert tour.hotel_id == "H001"



