"""Тесты для класса Attraction"""
import pytest
from datetime import datetime
from Destinations.Attraction import Attraction


class TestAttraction:
    """Тесты для класса Attraction"""
    
    @pytest.fixture
    def attraction(self):
        """Фикстура для создания достопримечательности"""
        return Attraction(
            attraction_id="ATT001",
            name="Эйфелева башня",
            location="Париж",
            description="Знаменитая башня",
            entry_price=25.0,
            opening_hours="09:00-23:00",
            category="monument",
            popularity_score=9.5
        )
    
    def test_init(self, attraction):
        """Тест инициализации"""
        assert attraction.attraction_id == "ATT001"
        assert attraction.name == "Эйфелева башня"
        assert attraction.location == "Париж"
        assert attraction.entry_price == 25.0
        assert attraction.popularity_score == 9.5
        assert attraction.daily_visitors == 0
        assert attraction.max_daily_capacity == 1000
        assert isinstance(attraction.reviews, list)
    
    def test_add_visitor_success(self, attraction):
        """Тест добавления посетителя - успех"""
        initial_count = attraction.daily_visitors
        attraction.add_visitor()
        assert attraction.daily_visitors == initial_count + 1
    
    def test_add_visitor_full(self):
        """Тест добавления посетителя - переполнена"""
        attraction = Attraction(
            attraction_id="ATT002",
            name="Test",
            location="Test",
            description="Test",
            entry_price=10.0,
            opening_hours="09:00-18:00",
            category="monument",
            popularity_score=8.0
        )
        attraction.daily_visitors = 1000
        with pytest.raises(ValueError, match="Достопримечательность переполнена"):
            attraction.add_visitor()
    
    def test_reset_daily_visitors(self, attraction):
        """Тест сброса ежедневных посетителей"""
        attraction.add_visitor()
        attraction.add_visitor()
        attraction.reset_daily_visitors()
        assert attraction.daily_visitors == 0
    
    def test_add_review(self, attraction):
        """Тест добавления отзыва"""
        attraction.add_review("Отличное место!", 5.0)
        assert len(attraction.reviews) == 1
        assert attraction.reviews[0]["text"] == "Отличное место!"
        assert attraction.reviews[0]["rating"] == 5.0
    
    def test_update_popularity_from_reviews(self, attraction):
        """Тест обновления популярности на основе отзывов"""
        initial_score = attraction.popularity_score
        attraction.add_review("Good", 4.0)
        # Проверяем, что популярность обновилась
        assert attraction.popularity_score != initial_score
    
    def test_calculate_revenue(self, attraction):
        """Тест вычисления выручки"""
        attraction.add_visitor()
        attraction.add_visitor()
        revenue = attraction.calculate_revenue()
        assert revenue == 2 * 25.0
    
    def test_is_crowded_true(self):
        """Тест проверки переполненности - да"""
        attraction = Attraction(
            attraction_id="ATT003",
            name="Test",
            location="Test",
            description="Test",
            entry_price=10.0,
            opening_hours="09:00-18:00",
            category="monument",
            popularity_score=8.0
        )
        attraction.daily_visitors = 800  # 80% от 1000
        assert attraction.is_crowded() is True
    
    def test_is_crowded_false(self, attraction):
        """Тест проверки переполненности - нет"""
        attraction.daily_visitors = 700
        assert attraction.is_crowded() is False
