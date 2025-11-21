"""Тесты для класса Bus"""
import pytest
from datetime import datetime, timedelta
from Transport.Bus import Bus


class TestBus:
    """Тесты для класса Bus"""
    
    @pytest.fixture
    def bus(self):
        """Фикстура для создания автобуса"""
        return Bus(
            bus_id="BUS001",
            route="Москва-Санкт-Петербург",
            departure_station="Москва",
            arrival_station="Санкт-Петербург",
            departure_time=datetime(2024, 6, 1, 10, 0),
            arrival_time=datetime(2024, 6, 1, 18, 0),
            price=2000.0,
            capacity=50,
            driver_id="DRV001"
        )
    
    def test_init(self, bus):
        """Тест инициализации"""
        assert bus.bus_id == "BUS001"
        assert bus.route == "Москва-Санкт-Петербург"
        assert bus.price == 2000.0
        assert bus.capacity == 50
        assert bus.current_passengers == 0
        assert bus.has_wifi is False
    
    def test_add_passenger_success(self, bus):
        """Тест добавления пассажира - успех"""
        initial_count = bus.current_passengers
        bus.add_passenger()
        assert bus.current_passengers == initial_count + 1
        assert bus.booking_count == initial_count + 1
    
    def test_add_passenger_full(self):
        """Тест добавления пассажира - переполнен"""
        bus = Bus(
            bus_id="BUS002",
            route="Route",
            departure_station="A",
            arrival_station="B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=2),
            price=1000.0,
            capacity=10,
            driver_id="DRV002"
        )
        bus.current_passengers = 10
        with pytest.raises(ValueError, match="Автобус переполнен"):
            bus.add_passenger()
    
    def test_remove_passenger(self, bus):
        """Тест удаления пассажира"""
        bus.add_passenger()
        initial_count = bus.current_passengers
        bus.remove_passenger()
        assert bus.current_passengers == initial_count - 1
    
    def test_calculate_duration(self, bus):
        """Тест вычисления продолжительности в часах"""
        duration = bus.calculate_duration()
        assert duration == 8
    
    def test_calculate_revenue(self, bus):
        """Тест вычисления выручки"""
        bus.add_passenger()
        bus.add_passenger()
        revenue = bus.calculate_revenue()
        assert revenue == 2 * 2000.0
    
    def test_enable_wifi(self, bus):
        """Тест включения WiFi"""
        bus.enable_wifi()
        assert bus.has_wifi is True
    
    def test_get_occupancy_rate(self, bus):
        """Тест получения процента занятости"""
        bus.add_passenger()
        rate = bus.get_occupancy_rate()
        assert rate == 1 / 50
