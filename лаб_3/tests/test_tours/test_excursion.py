"""Тесты для класса Excursion"""
import pytest
from datetime import datetime, timedelta
from Tours.Excursion import Excursion


class TestExcursion:
    """Тесты для класса Excursion"""
    
    @pytest.fixture
    def excursion(self):
        """Фикстура для создания экскурсии"""
        return Excursion(
            excursion_id="EXC001",
            name="Экскурсия по Парижу",
            location="Париж",
            duration_hours=4,
            price=5000.0,
            max_group_size=20,
            language="Русский",
            guide_id="G001"
        )
    
    def test_init(self, excursion):
        """Тест инициализации"""
        assert excursion.excursion_id == "EXC001"
        assert excursion.name == "Экскурсия по Парижу"
        assert excursion.location == "Париж"
        assert excursion.duration_hours == 4
        assert excursion.price == 5000.0
        assert excursion.max_group_size == 20
        assert excursion.language == "Русский"
        assert excursion.guide_id == "G001"
        assert excursion.current_participants == 0
        assert excursion.scheduled_date is None
        assert excursion.difficulty_level == "medium"
    
    def test_schedule(self, excursion):
        """Тест назначения даты экскурсии"""
        scheduled_date = datetime(2024, 7, 1, 10, 0)
        excursion.schedule(scheduled_date)
        assert excursion.scheduled_date == scheduled_date
    
    def test_add_participant_success(self, excursion):
        """Тест добавления участника - успех"""
        initial_count = excursion.current_participants
        excursion.add_participant()
        assert excursion.current_participants == initial_count + 1
    
    def test_add_participant_full(self, excursion):
        """Тест добавления участника - переполнен"""
        excursion.current_participants = 20
        initial_count = excursion.current_participants
        excursion.add_participant()
        # Не добавляется, если переполнен
        assert excursion.current_participants == initial_count
    
    def test_calculate_revenue(self, excursion):
        """Тест вычисления выручки"""
        excursion.add_participant()
        excursion.add_participant()
        revenue = excursion.calculate_revenue()
        assert revenue == 2 * 5000.0
    
    def test_get_group_discount_eligible(self, excursion):
        """Тест получения групповой скидки - есть скидка"""
        excursion.current_participants = 10
        discount = excursion.get_group_discount()
        assert discount == 0.1
    
    def test_get_group_discount_not_eligible(self, excursion):
        """Тест получения групповой скидки - нет скидки"""
        excursion.current_participants = 5
        discount = excursion.get_group_discount()
        assert discount == 0.0
    
    def test_is_full_true(self, excursion):
        """Тест проверки заполненности - да"""
        excursion.current_participants = 20
        assert excursion.is_full() is True
    
    def test_is_full_false(self, excursion):
        """Тест проверки заполненности - нет"""
        assert excursion.is_full() is False



