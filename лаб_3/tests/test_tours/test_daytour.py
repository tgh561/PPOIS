"""Тесты для класса DayTour"""
import pytest
from datetime import datetime, timedelta
from Tours.DayTour import DayTour


class TestDayTour:
    """Тесты для класса DayTour"""
    
    @pytest.fixture
    def day_tour(self):
        """Фикстура для создания однодневного тура"""
        return DayTour(
            tour_id="DT001",
            name="Обзорная экскурсия по городу",
            location="Париж",
            start_time=datetime(2024, 6, 1, 10, 0),
            end_time=datetime(2024, 6, 1, 18, 0),
            price=8000.0,
            max_participants=25,
            includes_meal=True
        )
    
    def test_init(self, day_tour):
        """Тест инициализации"""
        assert day_tour.tour_id == "DT001"
        assert day_tour.name == "Обзорная экскурсия по городу"
        assert day_tour.location == "Париж"
        assert day_tour.price == 8000.0
        assert day_tour.max_participants == 25
        assert day_tour.includes_meal is True
        assert day_tour.current_participants == 0
        assert day_tour.transport_included is False
    
    def test_calculate_duration(self, day_tour):
        """Тест вычисления продолжительности в часах"""
        duration = day_tour.calculate_duration()
        assert duration == 8
    
    def test_add_participant_success(self, day_tour):
        """Тест добавления участника - успех"""
        initial_count = day_tour.current_participants
        day_tour.add_participant()
        assert day_tour.current_participants == initial_count + 1
    
    def test_add_participant_full(self, day_tour):
        """Тест добавления участника - переполнен"""
        day_tour.current_participants = 25
        initial_count = day_tour.current_participants
        day_tour.add_participant()
        # Не добавляется, если переполнен
        assert day_tour.current_participants == initial_count
    
    def test_calculate_revenue(self, day_tour):
        """Тест вычисления выручки"""
        day_tour.add_participant()
        day_tour.add_participant()
        revenue = day_tour.calculate_revenue()
        assert revenue == 2 * 8000.0
    
    def test_is_full_true(self, day_tour):
        """Тест проверки заполненности - да"""
        day_tour.current_participants = 25
        assert day_tour.is_full() is True
    
    def test_is_full_false(self, day_tour):
        """Тест проверки заполненности - нет"""
        assert day_tour.is_full() is False
    
    def test_enable_transport(self, day_tour):
        """Тест включения транспорта"""
        day_tour.enable_transport()
        assert day_tour.transport_included is True



