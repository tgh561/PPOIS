"""Тесты для класса Photographer"""
import pytest
from datetime import datetime
from Users.Photographer import Photographer


class TestPhotographer:
    """Тесты для класса Photographer"""
    
    @pytest.fixture
    def photographer(self):
        """Фикстура для создания фотографа"""
        return Photographer(
            name="Анна",
            surname="Петрова",
            photographer_id="PH001",
            specialization="Свадебная фотография",
            experience_years=5,
            hourly_rate=3000.0,
            equipment=["Canon 5D", "Объектив 50mm"]
        )
    
    def test_init(self, photographer):
        """Тест инициализации"""
        assert photographer.name == "Анна"
        assert photographer.surname == "Петрова"
        assert photographer.photographer_id == "PH001"
        assert photographer.specialization == "Свадебная фотография"
        assert photographer.experience_years == 5
        assert photographer.hourly_rate == 3000.0
        assert photographer.equipment == ["Canon 5D", "Объектив 50mm"]
        assert photographer.sessions_completed == 0
        assert photographer.portfolio_size == 0
        assert photographer.rating == 0.0
        assert photographer.is_available is True
    
    def test_add_equipment(self, photographer):
        """Тест добавления оборудования"""
        photographer.add_equipment("Вспышка")
        assert "Вспышка" in photographer.equipment
        
        photographer.add_equipment("Штатив")
        assert len(photographer.equipment) == 4
    
    def test_add_equipment_duplicate(self, photographer):
        """Тест добавления дублирующегося оборудования"""
        photographer.add_equipment("Оборудование")
        initial_count = len(photographer.equipment)
        photographer.add_equipment("Оборудование")
        assert len(photographer.equipment) == initial_count
    
    def test_complete_session(self, photographer):
        """Тест завершения фотосессии"""
        initial_count = photographer.sessions_completed
        photographer.complete_session()
        assert photographer.sessions_completed == initial_count + 1
    
    def test_calculate_earnings(self, photographer):
        """Тест вычисления заработка"""
        hours = 8
        earnings = photographer.calculate_earnings(hours)
        assert earnings == 3000.0 * 8
    
    def test_add_to_portfolio(self, photographer):
        """Тест добавления в портфолио"""
        initial_size = photographer.portfolio_size
        photographer.add_to_portfolio()
        assert photographer.portfolio_size == initial_size + 1
    
    def test_update_rating(self, photographer):
        """Тест обновления рейтинга"""
        initial_rating = photographer.rating
        photographer.update_rating(4.5)
        assert photographer.rating == (initial_rating + 4.5) / 2
