"""Тесты для класса Destination"""
import pytest
from datetime import datetime
from Destinations.Destination import Destination
from Destinations.Hotel import Hotel
from Destinations.Attraction import Attraction
from Destinations.City import City
from Destinations.Country import Country
from Exceptions.VisaRequiredException import VisaRequiredException


class TestDestination:
    """Тесты для класса Destination"""
    
    @pytest.fixture
    def destination(self):
        """Фикстура для создания направления"""
        return Destination(
            destination_id="D001",
            name="Париж",
            country="Франция",
            city="Париж",
            description="Красивый город",
            climate="Умеренный",
            currency="EUR",
            visa_required=False
        )
    
    def test_init(self, destination):
        """Тест инициализации"""
        assert destination.destination_id == "D001"
        assert destination.name == "Париж"
        assert destination.country == "Франция"
        assert destination.city == "Париж"
        assert destination.description == "Красивый город"
        assert destination.climate == "Умеренный"
        assert destination.currency == "EUR"
        assert destination.visa_required is False
        assert destination.popularity_rating == 0.0
        assert isinstance(destination.attractions, list)
        assert isinstance(destination.hotels, list)
    
    def test_add_attraction(self, destination):
        """Тест добавления достопримечательности"""
        destination.add_attraction("Эйфелева башня")
        assert "Эйфелева башня" in destination.attractions
        
        destination.add_attraction("Лувр")
        assert len(destination.attractions) == 2
    
    def test_add_attraction_duplicate(self, destination):
        """Тест добавления дублирующейся достопримечательности"""
        destination.add_attraction("Музей")
        destination.add_attraction("Музей")
        assert destination.attractions.count("Музей") == 1
    
    def test_check_visa_requirement_no_visa(self, destination):
        """Тест проверки требования визы - не требуется"""
        destination.visa_required = False
        destination.check_visa_requirement()  # Не должно быть исключения
    
    def test_check_visa_requirement_required(self):
        """Тест проверки требования визы - требуется"""
        destination = Destination(
            destination_id="D002",
            name="США",
            country="США",
            city="Нью-Йорк",
            description="Big Apple",
            climate="Умеренный",
            currency="USD",
            visa_required=True
        )
        with pytest.raises(VisaRequiredException):
            destination.check_visa_requirement()
    
    def test_add_hotel(self, destination):
        """Тест добавления отеля"""
        destination.add_hotel("Grand Hotel")
        assert "Grand Hotel" in destination.hotels
        
        destination.add_hotel("Plaza Hotel")
        assert len(destination.hotels) == 2
    
    def test_add_hotel_duplicate(self, destination):
        """Тест добавления дублирующегося отеля"""
        destination.add_hotel("Hotel A")
        destination.add_hotel("Hotel A")
        assert destination.hotels.count("Hotel A") == 1
    
    def test_update_popularity(self, destination):
        """Тест обновления рейтинга популярности"""
        destination.update_popularity(4.5)
        assert destination.popularity_rating == 2.25
        
        destination.update_popularity(5.0)
        assert destination.popularity_rating == pytest.approx(3.625, rel=0.01)
    
    def test_get_location_info(self, destination):
        """Тест получения информации о местоположении"""
        info = destination.get_location_info()
        assert info == "Париж, Франция"
    
    def test_add_hotel_object_same_city(self, destination):
        """Тест добавления объекта отеля - тот же город"""
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
        destination.add_hotel_object(hotel)
        assert "H001" in destination.hotels
    
    def test_add_hotel_object_different_city(self, destination):
        """Тест добавления объекта отеля - другой город"""
        hotel = Hotel(
            hotel_id="H002",
            name="Hotel London",
            location="Лондон",
            stars=4,
            total_rooms=50,
            price_per_night=5000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
        initial_count = len(destination.hotels)
        destination.add_hotel_object(hotel)
        assert len(destination.hotels) == initial_count
    
    def test_add_attraction_object_same_city(self, destination):
        """Тест добавления объекта достопримечательности - тот же город"""
        attraction = Attraction(
            attraction_id="ATT001",
            name="Эйфелева башня",
            location="Париж",
            description="Famous tower",
            entry_price=25.0,
            opening_hours="09:00-23:00",
            category="monument",
            popularity_score=9.5
        )
        destination.add_attraction_object(attraction)
        assert "ATT001" in destination.attractions
    
    def test_add_attraction_object_different_city(self, destination):
        """Тест добавления объекта достопримечательности - другой город"""
        attraction = Attraction(
            attraction_id="ATT002",
            name="Big Ben",
            location="Лондон",
            description="Famous clock",
            entry_price=20.0,
            opening_hours="09:00-18:00",
            category="monument",
            popularity_score=9.0
        )
        initial_count = len(destination.attractions)
        destination.add_attraction_object(attraction)
        assert len(destination.attractions) == initial_count
    
    def test_assign_to_city(self, destination):
        """Тест назначения города (ассоциация)"""
        city = City(
            city_id="C001",
            name="Лондон",
            country="Великобритания",
            population=9000000,
            timezone="UTC+0",
            language="English",
            description="Capital",
            coordinates=(51.5074, -0.1278)
        )
        destination.assign_to_city(city)
        assert destination.city == "Лондон"
        assert destination.country == "Великобритания"
    
    def test_link_to_country(self, destination):
        """Тест связи со страной (ассоциация)"""
        country = Country(
            country_id="CO001",
            name="Италия",
            capital="Рим",
            population=60000000,
            currency="EUR",
            language="Italian",
            visa_required=False,
            description="Beautiful country"
        )
        destination.link_to_country(country)
        assert destination.country == "Италия"



