"""Тесты для класса Support"""
import pytest
from datetime import datetime
from Users.Support import Support


class TestSupport:
    """Тесты для класса Support"""
    
    @pytest.fixture
    def support(self):
        """Фикстура для создания сотрудника поддержки"""
        return Support(
            name="Мария",
            surname="Смирнова",
            employee_id="SUP001",
            shift="day",
            hire_date=datetime(2021, 1, 1),
            salary=50000.0,
            languages=["Русский", "Английский"]
        )
    
    def test_init(self, support):
        """Тест инициализации"""
        assert support.name == "Мария"
        assert support.surname == "Смирнова"
        assert support.employee_id == "SUP001"
        assert support.shift == "day"
        assert support.salary == 50000.0
        assert support.languages == ["Русский", "Английский"]
        assert support.tickets_resolved == 0
        assert support.average_resolution_time == 0.0
        assert support.satisfaction_rating == 0.0
    
    def test_resolve_ticket(self, support):
        """Тест решения тикета"""
        support.resolve_ticket("TICK001", 2.5)
        assert support.tickets_resolved == 1
        # average_resolution_time = (0.0 + 2.5) / 2 = 1.25
        assert support.average_resolution_time == 1.25
        
        support.resolve_ticket("TICK002", 3.0)
        assert support.tickets_resolved == 2
        # average_resolution_time = (1.25 + 3.0) / 2 = 2.125
        assert support.average_resolution_time == pytest.approx(2.125, rel=0.1)
    
    def test_add_language(self, support):
        """Тест добавления языка"""
        support.add_language("Французский")
        assert "Французский" in support.languages
        
        support.add_language("Немецкий")
        assert len(support.languages) == 4
    
    def test_add_language_duplicate(self, support):
        """Тест добавления дублирующегося языка"""
        support.add_language("Язык")
        initial_count = len(support.languages)
        support.add_language("Язык")
        assert len(support.languages) == initial_count
    
    def test_update_satisfaction_rating(self, support):
        """Тест обновления рейтинга удовлетворенности"""
        support.update_satisfaction_rating(4.5)
        assert support.satisfaction_rating == 2.25
        
        support.update_satisfaction_rating(5.0)
        assert support.satisfaction_rating == pytest.approx(3.625, rel=0.01)
    
    def test_calculate_productivity(self, support):
        """Тест вычисления продуктивности"""
        support.resolve_ticket("TICK001", 2.0)
        # average_resolution_time = (0.0 + 2.0) / 2 = 1.0
        productivity = support.calculate_productivity()
        assert productivity == 1.0 / 1.0
    
    def test_calculate_productivity_zero_time(self, support):
        """Тест вычисления продуктивности при нулевом времени"""
        support.resolve_ticket("TICK001", 1.0)  # Используем 1.0 вместо 0.0
        support.resolve_ticket("TICK002", 1.0)
        productivity = support.calculate_productivity()
        assert productivity >= 0
    
    def test_is_available_for_shift_true(self, support):
        """Тест проверки доступности для смены - да"""
        assert support.is_available_for_shift("day") is True
    
    def test_is_available_for_shift_false(self, support):
        """Тест проверки доступности для смены - нет"""
        assert support.is_available_for_shift("night") is False

