"""Тесты для класса Guide"""
import pytest
from datetime import datetime, timedelta
from Users.Guide import Guide


class TestGuide:
    """Тесты для класса Guide"""
    
    @pytest.fixture
    def guide(self):
        """Фикстура для создания гида"""
        return Guide(
            name="Мария",
            surname="Петрова",
            guide_id="G001",
            languages=["Русский", "Английский"],
            certification_date=datetime(2020, 1, 1),
            rating=4.5,
            hourly_rate=1500.0
        )
    
    def test_init(self, guide):
        """Тест инициализации"""
        assert guide.name == "Мария"
        assert guide.surname == "Петрова"
        assert guide.guide_id == "G001"
        assert guide.languages == ["Русский", "Английский"]
        assert guide.rating == 4.5
        assert guide.hourly_rate == 1500.0
        assert guide.tours_conducted == 0
        assert guide.is_available is True
        assert isinstance(guide.specializations, list)
    
    def test_add_language(self, guide):
        """Тест добавления языка"""
        guide.add_language("Французский")
        assert "Французский" in guide.languages
        assert len(guide.languages) == 3
    
    def test_add_language_duplicate(self, guide):
        """Тест добавления дублирующегося языка"""
        initial_count = len(guide.languages)
        guide.add_language("Русский")
        assert len(guide.languages) == initial_count
    
    def test_calculate_earnings(self, guide):
        """Тест вычисления заработка"""
        hours = 8
        earnings = guide.calculate_earnings(hours)
        assert earnings == 1500.0 * 8
    
    def test_update_rating(self, guide):
        """Тест обновления рейтинга"""
        initial_rating = guide.rating
        guide.update_rating(5.0)
        assert guide.rating == (initial_rating + 5.0) / 2
        
        guide.update_rating(3.0)
        assert guide.rating == ((initial_rating + 5.0) / 2 + 3.0) / 2
    
    def test_increment_tours(self, guide):
        """Тест увеличения счетчика туров"""
        initial_count = guide.tours_conducted
        guide.increment_tours()
        assert guide.tours_conducted == initial_count + 1
        
        guide.increment_tours()
        assert guide.tours_conducted == initial_count + 2
    
    def test_set_availability(self, guide):
        """Тест установки доступности"""
        guide.set_availability(False)
        assert guide.is_available is False
        
        guide.set_availability(True)
        assert guide.is_available is True



