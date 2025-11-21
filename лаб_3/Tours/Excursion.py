"""Класс: Экскурсия"""
from datetime import datetime
from typing import List, Optional


class Excursion:
    """Класс представляющий экскурсию"""
    
    def __init__(self, excursion_id: str, name: str, location: str, duration_hours: int, 
                 price: float, max_group_size: int, language: str, guide_id: str):
        self.excursion_id = excursion_id
        self.name = name
        self.location = location
        self.duration_hours = duration_hours
        self.price = price
        self.max_group_size = max_group_size
        self.language = language
        self.guide_id = guide_id
        self.current_participants = 0
        self.scheduled_date = None
        self.difficulty_level = "medium"
        
    def schedule(self, date: datetime) -> None:
        """Назначение даты экскурсии"""
        self.scheduled_date = date
    
    def add_participant(self) -> None:
        """Добавление участника"""
        if self.current_participants < self.max_group_size:
            self.current_participants += 1
    
    def calculate_revenue(self) -> float:
        """Вычисление выручки"""
        return self.current_participants * self.price
    
    def get_group_discount(self) -> float:
        """Получение скидки для группы"""
        if self.current_participants >= 10:
            return 0.1
        return 0.0
    
    def is_full(self) -> bool:
        """Проверка заполненности"""
        return self.current_participants >= self.max_group_size


