"""Класс: Достопримечательность"""
from datetime import datetime
from typing import List, Optional


class Attraction:
    """Класс представляющий достопримечательность"""
    
    def __init__(self, attraction_id: str, name: str, location: str, description: str, 
                 entry_price: float, opening_hours: str, category: str, popularity_score: float):
        self.attraction_id = attraction_id
        self.name = name
        self.location = location
        self.description = description
        self.entry_price = entry_price
        self.opening_hours = opening_hours
        self.category = category
        self.popularity_score = popularity_score
        self.daily_visitors = 0
        self.max_daily_capacity = 1000
        self.reviews = []
        
    def add_visitor(self) -> None:
        """Добавление посетителя"""
        if self.daily_visitors < self.max_daily_capacity:
            self.daily_visitors += 1
        else:
            raise ValueError("Достопримечательность переполнена")
    
    def reset_daily_visitors(self) -> None:
        """Сброс ежедневных посетителей"""
        self.daily_visitors = 0
    
    def add_review(self, review_text: str, rating: float) -> None:
        """Добавление отзыва"""
        self.reviews.append({"text": review_text, "rating": rating, "date": datetime.now()})
        self.update_popularity_from_reviews()
    
    def update_popularity_from_reviews(self) -> None:
        """Обновление популярности на основе отзывов"""
        if self.reviews:
            avg_rating = sum(r["rating"] for r in self.reviews) / len(self.reviews)
            self.popularity_score = (self.popularity_score + avg_rating) / 2
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.daily_visitors * self.entry_price
    
    def is_crowded(self) -> bool:
        """Проверка переполненности"""
        return self.daily_visitors >= self.max_daily_capacity * 0.8


