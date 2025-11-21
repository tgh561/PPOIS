"""Тесты для класса Driver"""
import pytest
from datetime import datetime, timedelta
from Users.Driver import Driver


class TestDriver:
    """Тесты для класса Driver"""
    
    @pytest.fixture
    def driver(self):
        """Фикстура для создания водителя"""
        return Driver(
            name="Петр",
            surname="Петров",
            driver_id="DRV001",
            license_number="DL123456",
            license_expiry=datetime.now() + timedelta(days=365),
            experience_years=5,
            hourly_rate=2000.0
        )
    
    def test_init(self, driver):
        """Тест инициализации"""
        assert driver.name == "Петр"
        assert driver.surname == "Петров"
        assert driver.driver_id == "DRV001"
        assert driver.license_number == "DL123456"
        assert driver.experience_years == 5
        assert driver.hourly_rate == 2000.0
        assert driver.total_trips == 0
        assert driver.total_distance == 0.0
        assert driver.safety_rating == 5.0
        assert driver.is_available is True
    
    def test_check_license_validity_valid(self, driver):
        """Тест проверки действительной лицензии"""
        assert driver.check_license_validity() is True
    
    def test_check_license_validity_expired(self):
        """Тест проверки просроченной лицензии"""
        driver = Driver(
            name="Test",
            surname="Test",
            driver_id="DRV002",
            license_number="DL999",
            license_expiry=datetime.now() - timedelta(days=1),
            experience_years=3,
            hourly_rate=1500.0
        )
        assert driver.check_license_validity() is False
    
    def test_add_trip(self, driver):
        """Тест добавления поездки"""
        initial_trips = driver.total_trips
        initial_distance = driver.total_distance
        
        driver.add_trip(100.5)
        assert driver.total_trips == initial_trips + 1
        assert driver.total_distance == initial_distance + 100.5
        
        driver.add_trip(200.0)
        assert driver.total_trips == initial_trips + 2
        assert driver.total_distance == initial_distance + 300.5
    
    def test_calculate_earnings(self, driver):
        """Тест вычисления заработка"""
        hours = 8
        earnings = driver.calculate_earnings(hours)
        assert earnings == 2000.0 * 8
    
    def test_update_safety_rating(self, driver):
        """Тест обновления рейтинга безопасности"""
        initial_rating = driver.safety_rating
        driver.update_safety_rating(4.5)
        assert driver.safety_rating == (initial_rating + 4.5) / 2
        
        driver.update_safety_rating(5.0)
        assert driver.safety_rating == ((initial_rating + 4.5) / 2 + 5.0) / 2
    
    def test_set_availability(self, driver):
        """Тест установки доступности"""
        driver.set_availability(False)
        assert driver.is_available is False
        
        driver.set_availability(True)
        assert driver.is_available is True



