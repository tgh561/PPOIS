"""Тесты для класса Cruise"""
import pytest
from datetime import datetime, timedelta
from Transport.Cruise import Cruise


class TestCruise:
    """Тесты для класса Cruise"""
    
    @pytest.fixture
    def cruise(self):
        """Фикстура для создания круиза"""
        return Cruise(
            cruise_id="CRU001",
            ship_name="Titanic II",
            departure_port="Санкт-Петербург",
            arrival_port="Хельсинки",
            departure_date=datetime(2024, 7, 1),
            arrival_date=datetime(2024, 7, 5),
            price_per_person=80000.0,
            total_cabins=200,
            route=["Санкт-Петербург", "Таллинн", "Хельсинки"]
        )
    
    def test_init(self, cruise):
        """Тест инициализации"""
        assert cruise.cruise_id == "CRU001"
        assert cruise.ship_name == "Titanic II"
        assert cruise.departure_port == "Санкт-Петербург"
        assert cruise.arrival_port == "Хельсинки"
        assert cruise.price_per_person == 80000.0
        assert cruise.total_cabins == 200
        assert cruise.available_cabins == 200
        assert cruise.has_all_inclusive is True
        assert isinstance(cruise.entertainment_available, list)
    
    def test_book_cabin_success(self, cruise):
        """Тест бронирования каюты - успех"""
        initial_available = cruise.available_cabins
        cruise.book_cabin("luxury")
        assert cruise.available_cabins == initial_available - 1
        assert cruise.booked_cabins == 1
    
    def test_book_cabin_full(self):
        """Тест бронирования каюты - переполнен"""
        cruise = Cruise(
            cruise_id="CRU002",
            ship_name="Ship",
            departure_port="A",
            arrival_port="B",
            departure_date=datetime.now(),
            arrival_date=datetime.now() + timedelta(days=3),
            price_per_person=50000.0,
            total_cabins=10,
            route=["A", "B"]
        )
        cruise.available_cabins = 0
        with pytest.raises(ValueError, match="Нет доступных кают"):
            cruise.book_cabin()
    
    def test_cancel_cabin(self, cruise):
        """Тест отмены каюты"""
        cruise.book_cabin()
        initial_available = cruise.available_cabins
        cruise.cancel_cabin()
        assert cruise.available_cabins == initial_available + 1
    
    def test_calculate_duration(self, cruise):
        """Тест вычисления продолжительности в днях"""
        duration = cruise.calculate_duration()
        assert duration == 4
    
    def test_calculate_revenue(self, cruise):
        """Тест вычисления выручки"""
        cruise.book_cabin()
        cruise.book_cabin()
        revenue = cruise.calculate_revenue()
        assert revenue == 2 * 80000.0
    
    def test_add_entertainment(self, cruise):
        """Тест добавления развлечения"""
        cruise.add_entertainment("Бассейн")
        assert "Бассейн" in cruise.entertainment_available
        
        cruise.add_entertainment("Кинотеатр")
        assert len(cruise.entertainment_available) == 2
    
    def test_add_entertainment_duplicate(self, cruise):
        """Тест добавления дублирующегося развлечения"""
        cruise.add_entertainment("Развлечение")
        cruise.add_entertainment("Развлечение")
        assert cruise.entertainment_available.count("Развлечение") == 1
    
    def test_get_occupancy_rate(self, cruise):
        """Тест получения процента занятости"""
        cruise.book_cabin()
        rate = cruise.get_occupancy_rate()
        assert rate == 1 / 200
