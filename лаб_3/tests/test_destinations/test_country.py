"""Тесты для класса Country"""
import pytest
from datetime import datetime
from Destinations.Country import Country
from Exceptions.VisaRequiredException import VisaRequiredException


class TestCountry:
    """Тесты для класса Country"""
    
    @pytest.fixture
    def country(self):
        """Фикстура для создания страны"""
        return Country(
            country_id="CO001",
            name="Франция",
            capital="Париж",
            population=67000000,
            currency="EUR",
            language="Французский",
            visa_required=False,
            description="Европейская страна"
        )
    
    def test_init(self, country):
        """Тест инициализации"""
        assert country.country_id == "CO001"
        assert country.name == "Франция"
        assert country.capital == "Париж"
        assert country.population == 67000000
        assert country.currency == "EUR"
        assert country.language == "Французский"
        assert country.visa_required is False
        assert country.safety_rating == 0.0
        assert isinstance(country.cities, list)
        assert isinstance(country.tourist_seasons, list)
    
    def test_add_city(self, country):
        """Тест добавления города"""
        country.add_city("C001")
        assert "C001" in country.cities
        
        country.add_city("C002")
        assert len(country.cities) == 2
    
    def test_add_city_duplicate(self, country):
        """Тест добавления дублирующегося города"""
        country.add_city("C001")
        country.add_city("C001")
        assert country.cities.count("C001") == 1
    
    def test_add_tourist_season(self, country):
        """Тест добавления туристического сезона"""
        country.add_tourist_season("Лето")
        assert "Лето" in country.tourist_seasons
        
        country.add_tourist_season("Весна")
        assert len(country.tourist_seasons) == 2
    
    def test_check_visa_requirement_no_visa(self, country):
        """Тест проверки требования визы - не требуется"""
        country.check_visa_requirement()  # Не должно быть исключения
    
    def test_check_visa_requirement_required(self):
        """Тест проверки требования визы - требуется"""
        country = Country(
            country_id="CO002",
            name="США",
            capital="Вашингтон",
            population=330000000,
            currency="USD",
            language="English",
            visa_required=True,
            description="North American country"
        )
        with pytest.raises(VisaRequiredException):
            country.check_visa_requirement()
    
    def test_update_safety_rating(self, country):
        """Тест обновления рейтинга безопасности"""
        country.update_safety_rating(4.5)
        assert country.safety_rating == 2.25
        
        country.update_safety_rating(5.0)
        assert country.safety_rating == pytest.approx(3.625, rel=0.01)
    
    def test_get_country_info(self, country):
        """Тест получения информации о стране"""
        info = country.get_country_info()
        assert "Франция" in info
        assert "Париж" in info
        assert "EUR" in info
    
    def test_get_total_cities(self, country):
        """Тест получения общего количества городов"""
        country.add_city("C001")
        country.add_city("C002")
        total = country.get_total_cities()
        assert total == 2
