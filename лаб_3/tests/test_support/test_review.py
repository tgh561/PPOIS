"""Тесты для класса Review"""
import pytest
from datetime import datetime, timedelta
from Support.Review import Review
from Users.Turist import Turist
from Tours.Tour import Tour
from Destinations.Hotel import Hotel


class TestReview:
    """Тесты для класса Review"""
    
    @pytest.fixture
    def review(self):
        """Фикстура для создания отзыва"""
        return Review(
            review_id="REV001",
            client_id="ivan@example.com",
            service_id="T001",
            service_type="tour",
            rating=4.5,
            review_text="Отличный тур!",
            review_date=datetime.now(),
            is_verified=False
        )
    
    def test_init(self, review):
        """Тест инициализации"""
        assert review.review_id == "REV001"
        assert review.client_id == "ivan@example.com"
        assert review.service_id == "T001"
        assert review.service_type == "tour"
        assert review.rating == 4.5
        assert review.review_text == "Отличный тур!"
        assert review.is_verified is False
        assert review.likes == 0
        assert review.dislikes == 0
        assert review.is_approved is True
    
    def test_validate_rating_valid(self, review):
        """Тест валидации валидного рейтинга"""
        result = review.validate_rating()
        assert result is True
    
    def test_validate_rating_too_low(self):
        """Тест валидации слишком низкого рейтинга"""
        review = Review(
            review_id="REV001",
            client_id="test@example.com",
            service_id="S001",
            service_type="service",
            rating=0.5,
            review_text="Test",
            review_date=datetime.now()
        )
        with pytest.raises(ValueError, match="Рейтинг должен быть от 1 до 5"):
            review.validate_rating()
    
    def test_validate_rating_too_high(self):
        """Тест валидации слишком высокого рейтинга"""
        review = Review(
            review_id="REV001",
            client_id="test@example.com",
            service_id="S001",
            service_type="service",
            rating=6.0,
            review_text="Test",
            review_date=datetime.now()
        )
        with pytest.raises(ValueError, match="Рейтинг должен быть от 1 до 5"):
            review.validate_rating()
    
    def test_add_like(self, review):
        """Тест добавления лайка"""
        review.add_like()
        assert review.likes == 1
        
        review.add_like()
        assert review.likes == 2
    
    def test_add_dislike(self, review):
        """Тест добавления дизлайка"""
        review.add_dislike()
        assert review.dislikes == 1
        
        review.add_dislike()
        assert review.dislikes == 2
    
    def test_verify_review(self, review):
        """Тест верификации отзыва"""
        review.verify_review()
        assert review.is_verified is True
    
    def test_approve_review(self, review):
        """Тест одобрения отзыва"""
        review.is_approved = False
        review.approve_review()
        assert review.is_approved is True
    
    def test_reject_review(self, review):
        """Тест отклонения отзыва"""
        review.reject_review()
        assert review.is_approved is False
    
    def test_calculate_helpfulness_score_with_votes(self, review):
        """Тест вычисления оценки полезности - есть голоса"""
        review.add_like()
        review.add_like()
        review.add_dislike()
        score = review.calculate_helpfulness_score()
        assert score == pytest.approx(0.666, rel=0.01)
    
    def test_calculate_helpfulness_score_no_votes(self, review):
        """Тест вычисления оценки полезности - нет голосов"""
        score = review.calculate_helpfulness_score()
        assert score == 0.0
    
    def test_get_days_since_review(self, review):
        """Тест получения дней с момента отзыва"""
        review.review_date = datetime.now() - timedelta(days=5)
        days = review.get_days_since_review()
        assert days == 5
    
    def test_link_to_turist(self, review):
        """Тест связи с туристом (ассоциация)"""
        turist = Turist(
            name="Петр",
            surname="Петров",
            email="petr@example.com",
            phone="+1234567890",
            birth_date=datetime(1990, 1, 1),
            password="password",
            registration_date=datetime.now()
        )
        review.link_to_turist(turist)
        assert review.client_id == "petr@example.com"
    
    def test_assign_to_tour_same_type(self, review):
        """Тест назначения тура - тот же тип сервиса"""
        tour = Tour(
            tour_id="T002",
            name="Test Tour",
            description="Description",
            destination="Paris",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 7),
            price=5000.0,
            max_participants=20
        )
        review.assign_to_tour(tour)
        assert review.service_id == "T002"
    
    def test_assign_to_tour_different_type(self, review):
        """Тест назначения тура - другой тип сервиса"""
        review.service_type = "hotel"
        tour = Tour(
            tour_id="T002",
            name="Test Tour",
            description="Description",
            destination="Paris",
            start_date=datetime(2024, 6, 1),
            end_date=datetime(2024, 6, 7),
            price=5000.0,
            max_participants=20
        )
        initial_id = review.service_id
        review.assign_to_tour(tour)
        assert review.service_id == initial_id
    
    def test_link_to_hotel_same_type(self, review):
        """Тест связи с отелем - тот же тип сервиса"""
        review.service_type = "hotel"
        hotel = Hotel(
            hotel_id="H001",
            name="Test Hotel",
            location="Paris",
            stars=4,
            total_rooms=50,
            price_per_night=5000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
        review.link_to_hotel(hotel)
        assert review.service_id == "H001"
    
    def test_link_to_hotel_different_type(self, review):
        """Тест связи с отелем - другой тип сервиса"""
        hotel = Hotel(
            hotel_id="H001",
            name="Test Hotel",
            location="Paris",
            stars=4,
            total_rooms=50,
            price_per_night=5000.0,
            check_in_time="14:00",
            check_out_time="12:00"
        )
        initial_id = review.service_id
        review.link_to_hotel(hotel)
        assert review.service_id == initial_id



