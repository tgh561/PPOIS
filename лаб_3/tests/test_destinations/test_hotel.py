"""Тесты для класса Hotel"""
import pytest
from datetime import datetime, timedelta
from Destinations.Hotel import Hotel
from Destinations.Destination import Destination
from Destinations.City import City
from Bookings.Reservation import Reservation
from Exceptions.HotelFullException import HotelFullException


class TestHotel:
    """Тесты для класса Hotel"""
    
    @pytest.fixture
    def hotel(self):
        """Фикстура для создания отеля"""
        return Hotel(
            hotel_id="H001",
            name="Grand Hotel",
            location="Paris",
            stars=5,
            total_rooms=50,
            price_per_night=10000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
    
    def test_init(self, hotel):
        """Тест инициализации"""
        assert hotel.hotel_id == "H001"
        assert hotel.name == "Grand Hotel"
        assert hotel.location == "Paris"
        assert hotel.stars == 5
        assert hotel.total_rooms == 50
        assert hotel.price_per_night == 10000.0
        assert hotel.available_rooms == 50
        assert hotel.rating == 0.0
        assert isinstance(hotel.amenities, list)
        assert isinstance(hotel.bookings, list)
    
    def test_check_availability_success(self, hotel):
        """Тест проверки доступности - успех"""
        result = hotel.check_availability(datetime.now(), datetime.now() + timedelta(days=3))
        assert result is True
    
    def test_check_availability_full(self):
        """Тест проверки доступности - переполнен"""
        hotel = Hotel(
            hotel_id="H002",
            name="Full Hotel",
            location="London",
            stars=4,
            total_rooms=10,
            price_per_night=8000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
        hotel.available_rooms = 0
        with pytest.raises(HotelFullException):
            hotel.check_availability(datetime.now(), datetime.now() + timedelta(days=3))
    
    def test_book_room(self, hotel):
        """Тест бронирования номера"""
        initial_available = hotel.available_rooms
        hotel.book_room(datetime.now(), 3)
        assert hotel.available_rooms == initial_available - 1
    
    def test_release_room(self, hotel):
        """Тест освобождения номера"""
        hotel.available_rooms = 45
        hotel.release_room()
        assert hotel.available_rooms == 46
    
    def test_release_room_at_capacity(self, hotel):
        """Тест освобождения номера при полной заполненности"""
        hotel.available_rooms = 50
        hotel.release_room()
        assert hotel.available_rooms == 50  # Не больше максимума
    
    def test_calculate_total_price(self, hotel):
        """Тест вычисления общей цены"""
        nights = 5
        total = hotel.calculate_total_price(nights)
        assert total == 10000.0 * 5
    
    def test_add_amenity(self, hotel):
        """Тест добавления удобства"""
        hotel.add_amenity("WiFi")
        assert "WiFi" in hotel.amenities
        
        hotel.add_amenity("Бассейн")
        assert len(hotel.amenities) == 2
    
    def test_add_amenity_duplicate(self, hotel):
        """Тест добавления дублирующегося удобства"""
        hotel.add_amenity("WiFi")
        hotel.add_amenity("WiFi")
        assert hotel.amenities.count("WiFi") == 1
    
    def test_update_rating(self, hotel):
        """Тест обновления рейтинга"""
        hotel.rating = 4.0
        hotel.update_rating(5.0)
        assert hotel.rating == 4.5
    
    def test_assign_to_destination(self, hotel):
        """Тест назначения направления (ассоциация)"""
        destination = Destination(
            destination_id="D001",
            name="Paris",
            country="France",
            city="Paris",
            description="Beautiful city",
            climate="Temperate",
            currency="EUR",
            visa_required=False
        )
        hotel.assign_to_destination(destination)
        assert hotel.location == "Paris"
    
    def test_process_reservation_hotel_service(self, hotel):
        """Тест обработки резервации - тип hotel"""
        reservation = Reservation(
            reservation_id="RES001",
            client_id="client@example.com",
            service_type="hotel",
            service_id="H001",
            reservation_date=datetime.now(),
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=3),
            price=30000.0
        )
        initial_available = hotel.available_rooms
        hotel.process_reservation(reservation)
        assert hotel.available_rooms == initial_available - 1
    
    def test_process_reservation_other_service(self, hotel):
        """Тест обработки резервации - другой тип"""
        reservation = Reservation(
            reservation_id="RES002",
            client_id="client@example.com",
            service_type="flight",
            service_id="F001",
            reservation_date=datetime.now(),
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=1),
            price=20000.0
        )
        initial_available = hotel.available_rooms
        hotel.process_reservation(reservation)
        assert hotel.available_rooms == initial_available
    
    def test_assign_to_city(self, hotel):
        """Тест назначения города (ассоциация)"""
        city = City(
            city_id="C001",
            name="London",
            country="UK",
            population=9000000,
            timezone="UTC+0",
            language="English",
            description="Capital city",
            coordinates=(51.5074, -0.1278)
        )
        hotel.assign_to_city(city)
        assert hotel.location == "London"



