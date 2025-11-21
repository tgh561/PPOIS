"""Тесты для класса Train"""
import pytest
from datetime import datetime, timedelta
from Transport.Train import Train


class TestTrain:
    """Тесты для класса Train"""
    
    @pytest.fixture
    def train(self):
        """Фикстура для создания поезда"""
        return Train(
            train_id="TRN001",
            train_number="001",
            route="Москва-Казань",
            departure_station="Москва",
            arrival_station="Казань",
            departure_time=datetime(2024, 6, 1, 10, 0),
            arrival_time=datetime(2024, 6, 1, 20, 0),
            price=3000.0,
            total_seats=100
        )
    
    def test_init(self, train):
        """Тест инициализации"""
        assert train.train_id == "TRN001"
        assert train.train_number == "001"
        assert train.price == 3000.0
        assert train.total_seats == 100
        assert train.available_seats == 100
        assert train.has_restaurant is False
        assert train.comfort_class == "economy"
    
    def test_book_seat_success(self, train):
        """Тест бронирования места - успех"""
        initial_available = train.available_seats
        train.book_seat("business")
        assert train.available_seats == initial_available - 1
        assert train.comfort_class == "business"
    
    def test_book_seat_full(self):
        """Тест бронирования места - переполнен"""
        train = Train(
            train_id="TRN002",
            train_number="002",
            route="Route",
            departure_station="A",
            arrival_station="B",
            departure_time=datetime.now(),
            arrival_time=datetime.now() + timedelta(hours=2),
            price=1000.0,
            total_seats=10
        )
        train.available_seats = 0
        with pytest.raises(ValueError, match="Нет доступных мест"):
            train.book_seat()
    
    def test_cancel_seat(self, train):
        """Тест отмены места"""
        train.book_seat()
        initial_available = train.available_seats
        train.cancel_seat()
        assert train.available_seats == initial_available + 1
    
    def test_calculate_duration(self, train):
        """Тест вычисления продолжительности в часах"""
        duration = train.calculate_duration()
        assert duration == 10
    
    def test_calculate_revenue(self, train):
        """Тест вычисления выручки"""
        train.book_seat()
        train.book_seat()
        revenue = train.calculate_revenue()
        assert revenue == 2 * 3000.0
    
    def test_set_comfort_class(self, train):
        """Тест установки класса комфорта"""
        train.set_comfort_class("first")
        assert train.comfort_class == "first"
    
    def test_get_occupancy_rate(self, train):
        """Тест получения процента занятости"""
        train.book_seat()
        rate = train.get_occupancy_rate()
        assert rate == 1 / 100
