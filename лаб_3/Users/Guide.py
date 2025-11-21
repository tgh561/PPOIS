"""Класс: Гид"""
from datetime import datetime
from typing import List


class Guide:
    """Класс представляющий гида"""
    
    def __init__(self, name: str, surname: str, guide_id: str, languages: List[str], 
                 certification_date: datetime, rating: float, hourly_rate: float):
        self.name = name
        self.surname = surname
        self.guide_id = guide_id
        self.languages = languages
        self.certification_date = certification_date
        self.rating = rating
        self.hourly_rate = hourly_rate
        self.tours_conducted = 0
        self.specializations = []
        self.is_available = True
        self.working_hours = 0
        
    def add_language(self, language: str) -> None:
        """Добавление языка"""
        if language not in self.languages:
            self.languages.append(language)
    
    def calculate_earnings(self, hours: int) -> float:
        """Вычисление заработка"""
        return hours * self.hourly_rate
    
    def update_rating(self, new_rating: float) -> None:
        """Обновление рейтинга"""
        self.rating = (self.rating + new_rating) / 2
    
    def increment_tours(self) -> None:
        """Увеличение счетчика туров"""
        self.tours_conducted += 1
    
    def set_availability(self, available: bool) -> None:
        """Установка доступности"""
        self.is_available = available


