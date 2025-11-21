"""Тесты для класса City"""
import pytest
from datetime import datetime
from Destinations.City import City


class TestCity:
    """Тесты для класса City"""
    
    @pytest.fixture
    def city(self):
        """Фикстура для создания города"""
        return City(
            city_id="C001",
            name="Париж",
            country="Франция",
            population=2000000,
            timezone="UTC+1",
            language="Французский",
            description="Столица Франции",
            coordinates=(48.8566, 2.3522)
        )
    
    def test_init(self, city):
        """Тест инициализации"""
        assert city.city_id == "C001"
        assert city.name == "Париж"
        assert city.country == "Франция"
        assert city.population == 2000000
        assert city.timezone == "UTC+1"
        assert city.language == "Французский"
        assert city.coordinates == (48.8566, 2.3522)
        assert city.tourism_rating == 0.0
        assert isinstance(city.attractions_list, list)
        assert isinstance(city.hotels_list, list)
        assert isinstance(city.restaurants_list, list)
    
    def test_add_attraction(self, city):
        """Тест добавления достопримечательности"""
        city.add_attraction("ATT001")
        assert "ATT001" in city.attractions_list
        
        city.add_attraction("ATT002")
        assert len(city.attractions_list) == 2
    
    def test_add_attraction_duplicate(self, city):
        """Тест добавления дублирующейся достопримечательности"""
        city.add_attraction("ATT001")
        city.add_attraction("ATT001")
        assert city.attractions_list.count("ATT001") == 1
    
    def test_add_hotel(self, city):
        """Тест добавления отеля"""
        city.add_hotel("H001")
        assert "H001" in city.hotels_list
        
        city.add_hotel("H002")
        assert len(city.hotels_list) == 2
    
    def test_add_restaurant(self, city):
        """Тест добавления ресторана"""
        city.add_restaurant("RES001")
        assert "RES001" in city.restaurants_list
    
    def test_get_total_attractions(self, city):
        """Тест получения общего количества достопримечательностей"""
        city.add_attraction("ATT001")
        city.add_attraction("ATT002")
        total = city.get_total_attractions()
        assert total == 2
    
    def test_update_tourism_rating(self, city):
        """Тест обновления рейтинга туризма"""
        city.update_tourism_rating(4.5)
        assert city.tourism_rating == 2.25
        
        city.update_tourism_rating(5.0)
        assert city.tourism_rating == pytest.approx(3.625, rel=0.01)
    
    def test_get_city_info(self, city):
        """Тест получения информации о городе"""
        info = city.get_city_info()
        assert "Париж" in info
        assert "Франция" in info
        assert "2000000" in info
