"""Класс: Отзыв"""
from datetime import datetime
from typing import List, Optional


class Review:
    """Класс представляющий отзыв"""
    
    def __init__(self, review_id: str, client_id: str, service_id: str, 
                 service_type: str, rating: float, review_text: str, 
                 review_date: datetime, is_verified: bool = False):
        self.review_id = review_id
        self.client_id = client_id
        self.service_id = service_id
        self.service_type = service_type
        self.rating = rating
        self.review_text = review_text
        self.review_date = review_date
        self.is_verified = is_verified
        self.likes = 0
        self.dislikes = 0
        self.is_approved = True
        
    def validate_rating(self) -> bool:
        """Валидация рейтинга"""
        if self.rating < 1.0 or self.rating > 5.0:
            raise ValueError("Рейтинг должен быть от 1 до 5")
        return True
    
    def add_like(self) -> None:
        """Добавление лайка"""
        self.likes += 1
    
    def add_dislike(self) -> None:
        """Добавление дизлайка"""
        self.dislikes += 1
    
    def verify_review(self) -> None:
        """Верификация отзыва"""
        self.is_verified = True
    
    def approve_review(self) -> None:
        """Одобрение отзыва"""
        self.is_approved = True
    
    def reject_review(self) -> None:
        """Отклонение отзыва"""
        self.is_approved = False
    
    def calculate_helpfulness_score(self) -> float:
        """Вычисление оценки полезности"""
        total = self.likes + self.dislikes
        if total == 0:
            return 0.0
        return self.likes / total
    
    def get_days_since_review(self) -> int:
        """Получение дней с момента отзыва"""
        return (datetime.now() - self.review_date).days
    
    def link_to_turist(self, turist) -> None:
        """Связь с туристом (ассоциация с Turist)"""
        from Users.Turist import Turist
        if isinstance(turist, Turist):
            self.client_id = turist.email
    
    def assign_to_tour(self, tour) -> None:
        """Назначение тура (ассоциация с Tour)"""
        from Tours.Tour import Tour
        if isinstance(tour, Tour):
            if self.service_type == "tour":
                self.service_id = tour.tour_id
    
    def link_to_hotel(self, hotel) -> None:
        """Связь с отелем (ассоциация с Hotel)"""
        from Destinations.Hotel import Hotel
        if isinstance(hotel, Hotel):
            if self.service_type == "hotel":
                self.service_id = hotel.hotel_id


